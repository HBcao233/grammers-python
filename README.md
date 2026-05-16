# gramme.rs-python

Python bindings for the [grammers](https://github.com/Lonami/grammers) Telegram MTProto library.

This project is a community-maintained Python wrapper built with PyO3. It is not affiliated with Telegram, and it is not an official Python client maintained by the `grammers` project.

## Current Status

This project is currently in an early stage of development. APIs may change between releases.

## Installation

```bash
pip install grammers
```

## Getting Telegram API Credentials

Before using this library, you must obtain your own Telegram API credentials:

1. Visit https://my.telegram.org/apps
2. Log in with your Telegram account
3. Create a new application
4. Copy your:
   - `api_id`
   - `api_hash`

These credentials are required for both user accounts and bot accounts.

## Authentication Modes

This library supports two different login methods:

### User Login

User login authenticates a normal Telegram account using your phone number.

Features:
- Full Telegram user capabilities
- Requires an interactive login flow on first run
- Session will be saved locally for future use

Typical flow:
1. Enter phone number
2. Receive login code from Telegram
3. Enter the verification code
4. Optionally enter 2FA password

### Bot Login

Bot login authenticates using a Bot Token obtained from [@BotFather](https://t.me/BotFather).

Features:
- Simpler authentication flow
- No phone number or verification code required
- Limited to bot account capabilities

## Minimal Example

### Bot Login

```python
from grammers import Client

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "123456:ABCDEF..."

client = Client(
    "bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

async def main():
    print(client.me)

    messages = await client.get_history_messages(777000, limit=1)
    print(messages[0])

client.run(main())
```

### User Login

```python
from grammers import Client

API_ID = 123456
API_HASH = "your_api_hash"

client = Client(
    "me",
    API_ID,
    API_HASH,
)

async def main():
    # The first run may require interactive login
    # depending on your local session state.

    print(client.me)

    messages = await client.get_history_messages(777000, limit=1)
    print(messages[0])

client.run(main())
```

## Session Files

The first argument passed to `Client(...)` is the session name:

```python
client = Client("me", API_ID, API_HASH)
```

This creates a local session file that stores authentication data, allowing future runs to reuse the same login session.

## Crates

- [grammers-python](https://github.com/hbcao233/grammers-python/blob/main/grammers-python)
- [grammers-session-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-session-pyo3)
- [grammers-mtsender-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-mtsender-pyo3)
- [grammers-tl-types-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-tl-types-pyo3)
- [grammers-tl-gen-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-tl-gen-pyo3)

## Development

Requirements:
- Rust toolchain
- Python 3.8+
- maturin

Install dependencies:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
pip install maturin
```

Build in development mode:

```bash
make dev
```