// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

use pyo3::prelude::*;
use pyo3::import_exception;

use std::collections::HashMap;
use std::sync::Mutex;

use libsql::{named_params, params};
use tokio::sync::Mutex as AsyncMutex;

use crate::sessions::{
    DEFAULT_DC, KNOWN_DC_OPTIONS, PySession, PyChannelKind, PyChannelState, PyDcOption, PyPeerAuth, PyPeerId, PyPeerInfo, PyPeerKind, PyUpdateState,
    PyUpdatesState,
};

const VERSION: i64 = 1;

struct Database(libsql::Connection);

struct Cache {
    pub home_dc: i32,
    pub dc_options: HashMap<i32, PyDcOption>,
}

#[repr(u8)]
enum PeerSubtype {
    UserSelf = 1,
    UserBot = 2,
    UserSelfBot = 3,
    Megagroup = 4,
    Broadcast = 8,
    Gigagroup = 12,
}

import_exception!(sqlite3, DataError);
import_exception!(sqlite3, OperationalError);
import_exception!(sqlite3, ProgrammingError);
import_exception!(sqlite3, NotSupportedError);
import_exception!(sqlite3, InterfaceError);

fn convert_libsql_error(err: libsql::Error) -> PyErr {
    match err {
        // 连接和操作相关错误 -> OperationalError
        libsql::Error::ConnectionFailed(s) => {
            OperationalError::new_err(format!("Connection failed: {}", s))
        }
        libsql::Error::SqliteFailure(code, msg) => {
            OperationalError::new_err(format!("SQLite error (code {}): {}", code, msg))
        }
        libsql::Error::RemoteSqliteFailure(code, extended_code, msg) => {
            OperationalError::new_err(format!(
                "Remote SQLite error (code {}, extended {}): {}",
                code, extended_code, msg
            ))
        }
        libsql::Error::Replication(e) => {
            OperationalError::new_err(format!("Replication error: {}", e))
        }
        libsql::Error::Sync(e) => {
            OperationalError::new_err(format!("Sync error: {}", e))
        }
        libsql::Error::WalConflict => {
            OperationalError::new_err("WAL conflict detected")
        }
        libsql::Error::Hrana(e) => {
            OperationalError::new_err(format!("Hrana protocol error: {}", e))
        }
        libsql::Error::WriteDelegation(e) => {
            OperationalError::new_err(format!("Write delegation error: {}", e))
        }
        libsql::Error::InvalidTlsConfiguration(e) => {
            OperationalError::new_err(format!("Invalid TLS configuration: {}", e))
        }
        libsql::Error::TransactionalBatchError(s) => {
            OperationalError::new_err(format!("Transactional batch error: {}", s))
        }

        // 数据相关错误 -> DataError
        libsql::Error::NullValue => {
            DataError::new_err("Unexpected NULL value")
        }
        libsql::Error::InvalidColumnType => {
            DataError::new_err("Invalid column type")
        }
        libsql::Error::InvalidBlobSize(size) => {
            DataError::new_err(format!("Invalid blob size: {}", size))
        }
        libsql::Error::ToSqlConversionFailure(e) => {
            DataError::new_err(format!("Failed to convert value to SQL: {}", e))
        }
        libsql::Error::Bincode(e) => {
            DataError::new_err(format!("Bincode serialization error: {}", e))
        }
        libsql::Error::InvalidUTF8Path => {
            DataError::new_err("Path contains invalid UTF-8")
        }

        // 编程/使用错误 -> ProgrammingError
        libsql::Error::Misuse(s) => {
            ProgrammingError::new_err(format!("API misuse: {}", s))
        }
        libsql::Error::ExecuteReturnedRows => {
            ProgrammingError::new_err("Execute returned rows, use query instead")
        }
        libsql::Error::QueryReturnedNoRows => {
            ProgrammingError::new_err("Query returned no rows")
        }
        libsql::Error::InvalidColumnName(name) => {
            ProgrammingError::new_err(format!("Invalid column name: {}", name))
        }
        libsql::Error::InvalidColumnIndex => {
            ProgrammingError::new_err("Invalid column index")
        }
        libsql::Error::ColumnNotFound(idx) => {
            ProgrammingError::new_err(format!("Column not found at index: {}", idx))
        }
        libsql::Error::InvalidParserState(s) => {
            ProgrammingError::new_err(format!("Invalid parser state: {}", s))
        }

        // SQL 语法错误 -> ProgrammingError
        libsql::Error::Sqlite3SyntaxError(line, col, msg) => {
            ProgrammingError::new_err(format!(
                "SQL syntax error at line {}, column {}: {}",
                line, col, msg
            ))
        }
        libsql::Error::Sqlite3UnsupportedStatement => {
            ProgrammingError::new_err("Unsupported SQL statement")
        }
        libsql::Error::Sqlite3ParserError(e) => {
            ProgrammingError::new_err(format!("SQL parser error: {}", e))
        }

        // 不支持的功能 -> NotSupportedError
        libsql::Error::SyncNotSupported(s) => {
            NotSupportedError::new_err(format!("Sync not supported: {}", s))
        }
        libsql::Error::LoadExtensionNotSupported => {
            NotSupportedError::new_err("Loading extensions is not supported")
        }
        libsql::Error::AuthorizerNotSupported => {
            NotSupportedError::new_err("Authorizer is not supported")
        }
        libsql::Error::UpdateHookNotSupported => {
            NotSupportedError::new_err("Update hook is not supported")
        }
        libsql::Error::FreezeNotSupported(s) => {
            NotSupportedError::new_err(format!("Freeze not supported: {}", s))
        }
        libsql::Error::ReservedBytesNotSupported => {
            NotSupportedError::new_err("Reserved bytes not supported")
        }
        
        _ => InterfaceError::new_err("Unknown error"),
    }
}
pub trait IntoPyResult<T> {
    fn db_err(self) -> PyResult<T>;
}
impl<T> IntoPyResult<T> for Result<T, libsql::Error> {
    fn db_err(self) -> PyResult<T> {
        self.map_err(|e| convert_libsql_error(e))
    }
}

/// SQLite-based storage. This is the recommended option.
#[pyclass(
    name = "SqliteSession",
    module = "grammers.sessions",
    extends = PySession
)]
pub struct PySqliteSession {
    database: AsyncMutex<Database>,
    cache: Mutex<Cache>,
}

#[pymethods]
impl PySqliteSession {
    #[pyo3(signature = (path=":memory:"))]
    async fn open(path: String) -> PyResult<Self> {
        let conn = libsql::Builder::new_local(path)
            .build()
            .await
            .db_err()?
            .connect()
            .db_err()?;
        let db = Database(conn);
        db.init().await.db_err()?;
        
        let home_dc = db
            .fetch_one("SELECT * FROM dc_home LIMIT 1", named_params![], |row| {
                Ok(row.get::<i32>(0)?)
            })
            .await
            .db_err()?
            .unwrap_or(DEFAULT_DC);

        let dc_options = db
            .fetch_all("SELECT * FROM dc_option", named_params![], |row| {
                Ok(DcOption {
                    id: row.get::<i32>(0)?,
                    ipv4: row.get::<String>(1)?.parse()?,
                    ipv6: row.get::<String>(2)?.parse()?,
                    auth_key: row
                        .get::<Option<Vec<u8>>>(3)?
                        .map(|auth_key| auth_key.try_into()?),
                })
            })
            .await
            .db_err()?
            .into_iter()
            .map(|dc_option| (dc_option.id, dc_option))
            .collect();

        Ok(SqliteSession {
            database: AsyncMutex::new(db),
            cache: Mutex::new(Cache {
                home_dc,
                dc_options,
            }),
        })
    }
    
    #[getter(home_dc_id)]
    async fn home_dc_id(&self) -> PyResult<i32> {
        Ok(self.cache.lock()
            .map_err(|_| PyRuntimeError::new_err("Cache corrupted"))?
            .home_dc)
    }
    
    #[pyo3(signature = (dc_id))]
    async fn set_dc_id(&self, dc_id: i32) -> PyResult<()> {
        self.cache.lock()
            .map_err(|_| PyRuntimeError::new_err("Cache corrupted"))?
            .home_dc = dc_id;
        let transaction = self
            .database
            .lock()
            .await
            .begin_transaction()
            .await
            .db_err()?;
        transaction
            .execute("DELETE FROM dc_home", params![])
            .await
            .db_err()?;
        let stmt = transaction
            .prepare("INSERT INTO dc_home VALUES (:dc_id)")
            .await
            .db_err()?;
        stmt.execute(named_params! {":dc_id": dc_id}).await.db_err()?;
        transaction.commit().await.db_err()?;
    }
    
    #[pyo3(signature = (dc_id))]
    async fn dc_option(&self, dc_id: i32) -> PyResult<Option<PyDcOption>> {
        self.cache
            .lock()
            .map_err(|_| PyRuntimeError::new_err("Cache corrupted"))?
            .dc_options
            .get(&dc_id)
            .cloned()
            .or_else(|| {
                KNOWN_DC_OPTIONS
                    .iter()
                    .find(|dc_option| dc_option.id == dc_id)
                    .cloned()
            })
    }
    
    #[pyo3(signature = (dc_option))]
    async fn set_dc_option(&self, dc_option: &PyDcOption) -> PyResult<()> {
        self.cache
            .lock()
            .map_err(|_| PyRuntimeError::new_err("Cache corrupted"))?
            .dc_options
            .insert(dc_option.id, dc_option.clone());

        let dc_option = dc_option.clone();
        let db = self.database.lock().await;
        db.0.execute(
            "INSERT OR REPLACE INTO dc_option VALUES (:dc_id, :ipv4, :ipv6, :auth_key)",
            named_params! {
                ":dc_id": dc_option.id,
                ":ipv4": dc_option.ipv4.to_string(),
                ":ipv6": dc_option.ipv6.to_string(),
                ":auth_key": dc_option.auth_key.map(|k| k.to_vec()),
            },
        )
        .await
        .db_err()?;
    }
    
    #[pyo3(signature = (peer))]
    async fn peer(&self, peer: &PeerIdLike) -> PyResult<Option<PyPeerInfo>> {
        let db = self.database.lock().await;
        let map_row = |row: libsql::Row| {
            let subtype = row.get::<Option<i64>>(2)?.map(|s| s as u8);
            Ok(match peer.kind() {
                PyPeerKind::User | PyPeerKind::UserSelf => PyPeerInfo::User {
                    id: PyPeerId::user(row.get::<i64>(0)?).bare_id(),
                    auth: row.get::<Option<i64>>(1)?.map(PyPeerAuth::from_hash),
                    bot: subtype.map(|s| s & PeerSubtype::UserBot as u8 != 0),
                    is_self: subtype.map(|s| s & PeerSubtype::UserSelf as u8 != 0),
                },
                PyPeerKind::Chat => PyPeerInfo::Chat { id: peer.bare_id() },
                PyPeerKind::Channel => PeerInfo::Channel {
                    id: peer.bare_id(),
                    auth: row.get::<Option<i64>>(1)?.map(PyPeerAuth::from_hash),
                    kind: subtype.and_then(|s| {
                        if (s & PeerSubtype::Gigagroup as u8) == PeerSubtype::Gigagroup as u8 {
                            Some(PyChannelKind::Gigagroup)
                        } else if s & PeerSubtype::Broadcast as u8 != 0 {
                            Some(PyChannelKind::Broadcast)
                        } else if s & PeerSubtype::Megagroup as u8 != 0 {
                            Some(PyChannelKind::Megagroup)
                        } else {
                            None
                        }
                    }),
                },
            })
        };

        if peer.kind() == PyPeerKind::UserSelf {
            db.fetch_one(
                "SELECT * FROM peer_info WHERE subtype & :type LIMIT 1",
                named_params! {":type": PeerSubtype::UserSelf as i64},
                map_row,
            )
            .await
            .db_err()?
        } else {
            db.fetch_one(
                "SELECT * FROM peer_info WHERE peer_id = :peer_id LIMIT 1",
                named_params! {":peer_id": peer.bot_api_dialog_id()},
                map_row,
            )
            .await
            .db_err()?
        }
    }
    
    #[pyo3(signature = (peer_info))]
    async fn cache_peer(&self, peer_info: &PyPeerInfo) -> PyResult<()> {
        let peer = peer.clone();
        let db = self.database.lock().await;
        let stmt =
            db.0.prepare("INSERT OR REPLACE INTO peer_info VALUES (:peer_id, :hash, :subtype)")
                .await
                .db_err()?;
        let subtype = match peer {
            PyPeerInfo::User { bot, is_self, .. } => {
                match (bot.unwrap_or_default(), is_self.unwrap_or_default()) {
                    (true, true) => Some(PeerSubtype::UserSelfBot),
                    (true, false) => Some(PeerSubtype::UserBot),
                    (false, true) => Some(PeerSubtype::UserSelf),
                    (false, false) => None,
                }
            }
            PyPeerInfo::Chat { .. } => None,
            PyPeerInfo::Channel { kind, .. } => kind.map(|kind| match kind {
                PyChannelKind::Megagroup => PeerSubtype::Megagroup,
                PyChannelKind::Broadcast => PeerSubtype::Broadcast,
                PyChannelKind::Gigagroup => PeerSubtype::Gigagroup,
            }),
        };
        let mut params = vec![];
        let peer_id = peer.id().bot_api_dialog_id();
        params.push((":peer_id".to_owned(), peer_id));
        let hash = peer.auth().unwrap_or_default().hash();
        if peer.auth().is_some() {
            params.push((":hash".to_owned(), hash));
        }
        let subtype = subtype.map(|s| s as i64);
        if subtype.is_some() {
            params.push((":subtype".to_owned(), subtype.unwrap()));
        }
        stmt.execute(params).await.db_err()?;
    }
    
    #[pyo3(signature = ())]
    async fn updates_state(&self) -> PyResult<PyUpdatesState> {
        let db = self.database.lock().await;
        let mut state = db
            .fetch_one(
                "SELECT * FROM update_state LIMIT 1",
                named_params![],
                |row| {
                    Ok(PyUpdatesState {
                        pts: row.get(0)?,
                        qts: row.get(1)?,
                        date: row.get(2)?,
                        seq: row.get(3)?,
                        channels: Vec::new(),
                    })
                },
            )
            .await
            .db_err()?
            .unwrap_or_default();
        state.channels = db
            .fetch_all("SELECT * FROM channel_state", named_params![], |row| {
                Ok(PyChannelState {
                    id: row.get(0)?,
                    pts: row.get(1)?,
                })
            })
            .await
            .db_err()?;
        state
    }
    
    #[pyo3(signature = (update))]
    async fn set_update_state(&self, update: PyUpdateState) -> PyResult<()> {
        let db = self.database.lock().await;
        let transaction = db.begin_transaction().await.unwrap();

        match update {
            PyUpdateState::All(updates_state) => {
                transaction
                    .execute("DELETE FROM update_state", params![])
                    .await
                    .db_err()?;
                transaction
                    .execute(
                        "INSERT INTO update_state VALUES (:pts, :qts, :date, :seq)",
                        named_params! {
                            ":pts": updates_state.pts,
                            ":qts": updates_state.qts,
                            ":date": updates_state.date,
                            ":seq": updates_state.seq,
                        },
                    )
                    .await
                    .db_err()?;

                transaction
                    .execute("DELETE FROM channel_state", params![])
                    .await
                    .db_err()?;
                for channel in updates_state.channels {
                    transaction
                        .execute(
                            "INSERT INTO channel_state VALUES (:peer_id, :pts)",
                            named_params! {
                                ":peer_id": channel.id,
                                ":pts": channel.pts,
                            },
                        )
                        .await
                        .db_err()?;
                }
            }
            PyUpdateState::Primary { pts, date, seq } => {
                let previous = db
                    .fetch_one(
                        "SELECT * FROM update_state LIMIT 1",
                        named_params![],
                        |_| Ok(()),
                    )
                    .await
                    .db_err()?;

                if previous.is_some() {
                    transaction
                        .execute(
                            "UPDATE update_state SET pts = :pts, date = :date, seq = :seq",
                            named_params! {
                                ":pts": pts,
                                ":date": date,
                                ":seq": seq,
                            },
                        )
                        .await
                        .db_err()?;
                } else {
                    transaction
                        .execute(
                            "INSERT INTO update_state VALUES (:pts, 0, :date, :seq)",
                            named_params! {
                                ":pts": pts,
                                ":date": date,
                                ":seq": seq,
                            },
                        )
                        .await
                        .db_err()?;
                }
            }
            PyUpdateState::Secondary { qts } => {
                let previous = db
                    .fetch_one(
                        "SELECT * FROM update_state LIMIT 1",
                        named_params![],
                        |_| Ok(()),
                    )
                    .await
                    .db_err()?;

                if previous.is_some() {
                    transaction
                        .execute(
                            "UPDATE update_state SET qts = :qts",
                            named_params! {":qts": qts},
                        )
                        .await
                        .db_err()?;
                } else {
                    transaction
                        .execute(
                            "INSERT INTO update_state VALUES (0, :qts, 0, 0)",
                            named_params! {":qts": qts},
                        )
                        .await
                        .db_err()?;
                }
            }
            PyUpdateState::Channel { id, pts } => {
                transaction
                    .execute(
                        "INSERT OR REPLACE INTO channel_state VALUES (:peer_id, :pts)",
                        named_params! {
                            ":peer_id": id,
                            ":pts": pts,
                        },
                    )
                    .await
                    .db_err()?;
            }
        }

        transaction.commit().await.db_err()?;
    }
}

impl Database {
    async fn init(&self) -> libsql::Result<()> {
        let mut user_version: i64 = self
            .fetch_one("PRAGMA user_version", params![], |row| row.get(0))
            .await?
            .unwrap_or(0);
        if user_version == VERSION {
            return Ok(());
        }

        if user_version == 0 {
            self.migrate_v0_to_v1().await?;
            user_version += 1;
        }
        if user_version == VERSION {
            // Can't bind PRAGMA parameters, but `VERSION` is not user-controlled input.
            self.0
                .execute(&format!("PRAGMA user_version = {VERSION}"), params![])
                .await?;
        }
        Ok(())
    }

    async fn migrate_v0_to_v1(&self) -> libsql::Result<()> {
        let transaction = self.begin_transaction().await?;
        transaction
            .execute(
                "CREATE TABLE dc_home (
                dc_id INTEGER NOT NULL,
                PRIMARY KEY(dc_id))",
                params![],
            )
            .await?;
        transaction
            .execute(
                "CREATE TABLE dc_option (
                dc_id INTEGER NOT NULL,
                ipv4 TEXT NOT NULL,
                ipv6 TEXT NOT NULL,
                auth_key BLOB,
                PRIMARY KEY (dc_id))",
                params![],
            )
            .await?;
        transaction
            .execute(
                "CREATE TABLE peer_info (
                peer_id INTEGER NOT NULL,
                hash INTEGER,
                subtype INTEGER,
                PRIMARY KEY (peer_id))",
                params![],
            )
            .await?;
        transaction
            .execute(
                "CREATE TABLE update_state (
                pts INTEGER NOT NULL,
                qts INTEGER NOT NULL,
                date INTEGER NOT NULL,
                seq INTEGER NOT NULL)",
                params![],
            )
            .await?;
        transaction
            .execute(
                "CREATE TABLE channel_state (
                peer_id INTEGER NOT NULL,
                pts INTEGER NOT NULL,
                PRIMARY KEY (peer_id))",
                params![],
            )
            .await?;

        transaction.commit().await?;
        Ok(())
    }

    async fn begin_transaction(&self) -> libsql::Result<libsql::Transaction> {
        self.0.transaction().await
    }

    async fn fetch_one<
        T,
        P: libsql::params::IntoParams,
        F: FnOnce(libsql::Row) -> libsql::Result<T>,
    >(
        &self,
        statement: &str,
        params: P,
        select: F,
    ) -> libsql::Result<Option<T>> {
        let mut statement = self.0.prepare(statement).await?;
        let result = statement.query_row(params).await;
        match result {
            Ok(value) => Ok(Some(select(value)?)),
            Err(libsql::Error::QueryReturnedNoRows) => Ok(None),
            Err(e) => Err(e),
        }
    }

    async fn fetch_all<
        T,
        P: libsql::params::IntoParams,
        F: FnMut(libsql::Row) -> libsql::Result<T>,
    >(
        &self,
        statement: &str,
        params: P,
        mut select: F,
    ) -> libsql::Result<Vec<T>> {
        let statement = self.0.prepare(statement).await?;
        let mut rows = statement.query(params).await?;
        let mut result = Vec::new();
        while let Some(row) = rows.next().await? {
            result.push(select(row)?);
        }
        Ok(result)
    }
}
