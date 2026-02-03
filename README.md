# gramme.rs-python
[gramme.rs](https://github.com/Lonami/grammers)'s Python bindings

# Current status
This project is in the early stage of development.

# Usage
```bash
pip install grammers
```

```python
from grammers import Client

API_ID = ''
API_HASH = ''
client = Client(
    'me',
    API_ID,
    API_HASH,
    # bot_token=BOT_TOKEN,  # Optional
)

async def main():
    print(client.me)
    
    message = await client.get_history_messages(777000, limit=1)
    print(message[0])

client.run(main())
```

# Crates
* [grammers-python](https://github.com/hbcao233/grammers-python/blob/main/grammers-python)
* [grammers-session-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-session-pyo3)
* [grammers-mtsender-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-mtsender-pyo3)
* [grammers-tl-types-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-tl-types-pyo3)
* [grammers-tl-gen-pyo3](https://github.com/hbcao233/grammers-python/blob/main/grammers-tl-gen-pyo3)

# Development
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
pip install maturin
make dev
```
