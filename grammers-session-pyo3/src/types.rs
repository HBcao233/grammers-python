// Copyright 2020 - developers of the `grammers` project.
//
// Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
// https://www.apache.org/licenses/LICENSE-2.0> or the MIT license
// <LICENSE-MIT or https://opensource.org/licenses/MIT>, at your
// option. This file may not be copied, modified, or distributed
// except according to those terms.

//! Session type definitions.
use pyo3::prelude::*;
use pyo3::types::PyBytes;
use pyo3::exceptions::PyTypeError;

use std::net::{Ipv4Addr, Ipv6Addr, SocketAddr, SocketAddrV4, SocketAddrV6};
use std::str::FromStr;

use grammers_session::types::{ChannelState, UpdatesState};

/// A datacenter option.
///
/// This is very similar to Telegram's own `dcOption` type, except it also
/// contains the permanent authentication key and serves as a stable interface.
#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "DcOption", module = "grammers.sessions")]
pub struct PyDcOption {
    /// Datacenter identifier.
    ///
    /// The primary datacenters have IDs from 1 to 5 inclusive, and are known statically by the session.
    /// ```
    /// let data = grammers_session::SessionData::default();
    /// assert_eq!(data.dc_options.len(), 5);
    /// (1..=5).for_each(|dc_id| assert!(data.dc_options.contains_key(&dc_id)));
    /// ```
    #[pyo3(get, set)]
    pub id: i32,
    /// IPv4 address corresponding to this datacenter.
    #[pyo3(get, set)]
    pub ipv4: PySocketAddrV4,
    /// IPv6 address corresponding to this datacenter. May actually be embedding the [`Self::ipv4`] address.
    #[pyo3(get, set)]
    pub ipv6: PySocketAddrV6,
    /// Permanent authentication key generated for encrypted communication with this datacenter.
    ///
    /// A logged-in user may or not be bound to this authentication key.
    #[pyo3(get, set)]
    pub auth_key: Option<[u8; 256]>,
}
#[pymethods]
impl PyDcOption {
    #[new]
    #[pyo3(signature = (id, ipv4=None, ipv6=None, auth_key=None))]
    fn new(
        id: i32, 
        ipv4: Option<String>, 
        ipv6: Option<String>, 
        auth_key: Option<[u8; 256]>,
    ) -> PyResult<Self> {
        let (ipv4, ipv6) = match (ipv4, ipv6) {
            (None, None) => return Err(PyTypeError::new_err(
                "At least one of ipv4 and ipv6 must be provided."
            )),
            (Some(ipv4), Some(ipv6)) => {
                let ipv4: SocketAddrV4 = ipv4.parse().map_err(|_| PyTypeError::new_err(
                    "fail to parse ipv4 string"
                ))?;
                let ipv6: SocketAddrV6 = ipv6.parse().map_err(|_| PyTypeError::new_err(
                    "fail to parse ipv6 string"
                ))?;
                (ipv4, ipv6)
            },
            (Some(ipv4), None) => {
                let ipv4: SocketAddrV4 = ipv4.parse().map_err(|_| PyTypeError::new_err(
                    "fail to parse ipv4 string"
                ))?;
                let ipv6 = SocketAddrV6::new(ipv4.ip().to_ipv6_compatible(), ipv4.port(), 0, 0);
                (ipv4, ipv6)
            },
            (None, Some(ipv6)) => {
                let ipv6: SocketAddrV6 = ipv6.parse().map_err(|_| PyTypeError::new_err(
                    "fail to parse ipv6 string"
                ))?;
                let ipv4 = SocketAddrV4::new(
                    ipv6.ip().to_ipv4_mapped().unwrap_or(Ipv4Addr::new(0, 0, 0, 0)),
                    ipv6.port(),
                );
                (ipv4, ipv6)
            },
        };
        Ok(Self {
            id,
            ipv4: ipv4.into(),
            ipv6: ipv6.into(),
            auth_key,
        })
    }
    
    fn __repr__(&self) -> PyResult<String> {
        let auth_key = match self.auth_key {
            None => "None".to_string(),
            Some(x) => Python::attach(|py| -> PyResult<String> {
                Ok(PyBytes::new(py, &x).repr()?.to_string())
            })?,
        };
        Ok(format!(
            "DcOption(\n  id={},\n  ipv4={},\n  ipv6={},\n  auth_key={}\n)",
            self.id,
            self.ipv4.__repr__(),
            self.ipv6.__repr__(),
            auth_key,
        ))
    }
}

#[derive(FromPyObject)]
enum Ipv4Like {
    Tuple([u8; 4]),
    Str(String)
}

#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "SocketAddrV4")]
pub struct PySocketAddrV4 {
    #[pyo3(get, set)]
    pub a: u8,
    #[pyo3(get, set)]
    pub b: u8,
    #[pyo3(get, set)]
    pub c: u8,
    #[pyo3(get, set)]
    pub d: u8,
    #[pyo3(get, set)]
    pub port: u16,
}
impl PySocketAddrV4 {
    pub fn ip(&self) -> Ipv4Addr {
        Ipv4Addr::new(self.a, self.b, self.c, self.d)
    }
    
    pub fn port(&self) -> u16 {
        self.port
    }
}
#[pymethods]
impl PySocketAddrV4 {
    #[new]
    fn new(ip: Ipv4Like, port: u16) -> PyResult<Self> {
        let ip = match ip {
            Ipv4Like::Tuple(x) => x,
            Ipv4Like::Str(s) => Ipv4Addr::from_str(&s)
                .map_err(|_| PyTypeError::new_err(format!("Can't parse '{}' as ipv4", s)))?
                .octets(),
        };
        Ok(Self {
            a: ip[0],
            b: ip[1],
            c: ip[2],
            d: ip[3],
            port,
        })
    }
    
    #[getter(ip)]
    fn get_ip(&self) -> String {
        self.ip().to_string()
    }
    
    #[setter(ip)]
    fn set_ip(&mut self, ip: Ipv4Like) -> PyResult<()> {
        let ip = match ip {
            Ipv4Like::Tuple(x) => x,
            Ipv4Like::Str(s) => Ipv4Addr::from_str(&s)
                .map_err(|_| PyTypeError::new_err(format!("Can't parse '{}' as ipv4", s)))?
                .octets(),
        };
        self.a = ip[0];
        self.b = ip[1];
        self.c = ip[2];
        self.d = ip[3];
        Ok(())
    }
    
    fn __repr__(&self) -> String {
        format!("SocketAddrV4(ip={}, port={})", self.get_ip(), self.port)
    }
    
    fn __str__(&self) -> String {
        format!("{}:{}", self.get_ip(), self.port)
    }
}
impl From<SocketAddrV4> for PySocketAddrV4 {
    fn from(x: SocketAddrV4) -> Self {
        let ip = x.ip().octets();
        Self {
            a: ip[0],
            b: ip[1],
            c: ip[2],
            d: ip[3],
            port: x.port(),
        }
    }
}
impl From<PySocketAddrV4> for SocketAddrV4 {
    fn from(x: PySocketAddrV4) -> Self {
        Self::new(
            Ipv4Addr::new(x.a, x.b, x.c, x.d),
            x.port,
        )
    }
}
impl From<PySocketAddrV4> for SocketAddr {
    fn from(x: PySocketAddrV4) -> Self {
        let x: SocketAddrV4 = x.into();
        x.into()
    }
}

#[derive(FromPyObject)]
enum Ipv6Like {
    Tuple([u16; 8]),
    Str(String)
}

#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "SocketAddrV6", module = "grammers.sessions")]
pub struct PySocketAddrV6 {
    a: u16,
    b: u16,
    c: u16,
    d: u16,
    e: u16,
    f: u16,
    g: u16,
    h: u16,
    port: u16,
}
impl PySocketAddrV6 {
    pub fn ip(&self) -> Ipv6Addr {
        Ipv6Addr::new(
            self.a,
            self.b,
            self.c,
            self.d,
            self.e,
            self.f,
            self.g,
            self.h,
        )
    }
    
    pub fn port(&self) -> u16 {
        self.port
    }
}
#[pymethods]
impl PySocketAddrV6 {
    #[new]
    fn new(ip: Ipv6Like, port: u16) -> PyResult<Self> {
        let ip = match ip {
            Ipv6Like::Tuple(x) => x,
            Ipv6Like::Str(s) => Ipv6Addr::from_str(&s)
                .map_err(|_| PyTypeError::new_err(format!("Can't parse '{}' as ipv6", s)))?
                .segments(),
        };
        Ok(Self {
            a: ip[0],
            b: ip[1],
            c: ip[2],
            d: ip[3],
            e: ip[4],
            f: ip[5],
            g: ip[6],
            h: ip[7],
            port,
        })
    }
    
    #[getter(ip)]
    fn get_ip(&self) -> String {
        self.ip().to_string()
    }
    
    #[setter(ip)]
    fn set_ip(&mut self, ip: Ipv6Like) -> PyResult<()> {
        let ip = match ip {
            Ipv6Like::Tuple(x) => x,
            Ipv6Like::Str(s) => Ipv6Addr::from_str(&s)
                .map_err(|_| PyTypeError::new_err(format!("Can't parse '{}' as ipv6", s)))?
                .segments(),
        };
        self.a = ip[0];
        self.b = ip[1];
        self.c = ip[2];
        self.d = ip[3];
        self.e = ip[4];
        self.f = ip[5];
        self.g = ip[6];
        self.h = ip[7];
        Ok(())
    }
    
    fn __repr__(&self) -> String {
        format!("SocketAddrV6(ip={}, port={})", self.get_ip(), self.port)
    }
    
    fn __str__(&self) -> String {
        format!("[{}]:{}", self.get_ip(), self.port)
    }
}
impl From<SocketAddrV6> for PySocketAddrV6 {
    fn from(x: SocketAddrV6) -> Self {
        let ip = x.ip().segments();
        Self {
            a: ip[0],
            b: ip[1],
            c: ip[2],
            d: ip[3],
            e: ip[4],
            f: ip[5],
            g: ip[6],
            h: ip[7],
            port: x.port(),
        }
    }
}
impl From<PySocketAddrV6> for SocketAddrV6 {
    fn from(x: PySocketAddrV6) -> Self {
        Self::new(
            Ipv6Addr::new(
                x.a, x.b, x.c, x.d,
                x.e, x.f, x.g, x.h,
            ),
            x.port,
            0,
            0,
        )
    }
}
impl From<PySocketAddrV6> for SocketAddr {
    fn from(x: PySocketAddrV6) -> Self {
        let x: SocketAddrV6 = x.into();
        x.into()
    }
}

/// Full update state needed to process updates in order without gaps.
#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "UpdatesState")]
pub struct PyUpdatesState {
    /// Primary persistent timestamp value.
    pub pts: i32,
    /// Secondary persistent timestamp value.
    pub qts: i32,
    /// Auxiliary date value.
    pub date: i32,
    /// Auxiliary sequence value.
    pub seq: i32,
    /// Persistent timestamp of each known channel.
    pub channels: Vec<PyChannelState>,
}
#[pymethods]
impl PyUpdatesState {
    #[new]
    fn new(pts: i32, qts: i32, date: i32, seq: i32, channels: Vec<PyChannelState>) -> Self {
        Self {
            pts,
            qts,
            date,
            seq,
            channels,
        }
    }
    
    fn __repr__(&self) -> String {
        let channels = self.channels.clone()
            .into_iter()
            .map(|x| x.__repr__())
            .collect::<Vec<String>>()
            .join(",\n");
        let channels = channels.split('\n')
            .map(|line| format!("  {}", line))
            .collect::<Vec<String>>()
            .join("\n");
        let channels = format!("[\n{}\n]", channels);
        format!(
            "UpdatesState(\n  pts: {},\n  qts: {},\n  date: {},\n  seq: {},\n  channels: {}\n)",
            self.pts,
            self.qts,
            self.date,
            self.seq,
            channels,
        )
    }
}
impl From<UpdatesState> for PyUpdatesState {
    fn from(x: UpdatesState) -> Self {
        Self {
            pts: x.pts,
            qts: x.qts,
            date: x.date,
            seq: x.seq,
            channels: x.channels.into_iter().map(Into::into).collect(),
        }
    }
}
impl From<PyUpdatesState> for UpdatesState {
    fn from(x: PyUpdatesState) -> Self {
        Self {
            pts: x.pts,
            qts: x.qts,
            date: x.date,
            seq: x.seq,
            channels: x.channels.into_iter().map(Into::into).collect(),
        }
    }
}

/// Update state for a single channel.
#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "ChannelState")]
pub struct PyChannelState {
    /// The [`PeerId::bare_id`] of the channel.
    pub id: i64,
    /// Persistent timestamp value.
    pub pts: i32,
}
#[pymethods]
impl PyChannelState {
    #[new]
    fn new(id: i64, pts: i32) -> Self {
        Self {
            id,
            pts,
        }
    }
    
    pub fn __repr__(&self) -> String {
        format!("ChannelState(\n  id: {},\n  pts: {},\n)", self.id, self.pts)
    }
}
impl From<ChannelState> for PyChannelState {
    fn from(x: ChannelState) -> Self {
        Self {
            id: x.id,
            pts: x.pts,
        }
    }
}
impl From<PyChannelState> for ChannelState {
    fn from(x: PyChannelState) -> Self {
        Self {
            id: x.id,
            pts: x.pts,
        }
    }
}

/// Used in [`crate::Session::set_update_state`] to update parts of the overall [`UpdatesState`].
#[derive(Clone, Debug, PartialEq, Eq)]
#[pyclass(name = "UpdateState")]
pub enum PyUpdateState {
    /// Updates the entirety of the state.
    All(PyUpdatesState),
    /// Updates only what's known as the "primary" state of the account.
    Primary {
        /// New [`UpdatesState::pts`] value.
        pts: i32,
        /// New [`UpdatesState::date`] value.
        date: i32,
        /// New [`UpdatesState::seq`] value.
        seq: i32,
    },
    /// Updates only what's known as the "secondary" state of the account.
    Secondary {
        /// New [`UpdatesState::qts`] value.
        qts: i32,
    },
    /// Updates the state of a single channel.
    Channel {
        /// The [`PeerId::bare_id`] of the channel.
        id: i64,
        /// New [`ChannelState::pts`] value.
        pts: i32,
    },
}
#[pymethods]
impl PyUpdateState {
    #[staticmethod]
    fn all(update: PyUpdatesState) -> Self {
        Self::All(update)
    }
    
    #[staticmethod]
    fn primary(pts: i32, date: i32, seq: i32) -> Self {
        Self::Primary {
            pts,
            date,
            seq,
        }
    }
    
    #[staticmethod]
    fn secondary(qts: i32) -> Self {
        Self::Secondary {
            qts,
        }
    }
    
    #[staticmethod]
    fn channel(id: i64, pts: i32) -> Self {
        Self::Channel {
            id, 
            pts,
        }
    }
}