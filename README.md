# Gather WebSocket Client

## Installation

```bash
pip install gather-client-ws
```

## Documentation

### Auth

Generate your `API_KEY` here: [https://gather.town/apiKeys](https://gather.town/apiKeys)

### Basic Usage

``` python
import asyncio

from gather_client_ws import GatherClient


async def producer(client):
    await client.set_text_status("new status text")
    await client.set_emoji_status("😁")


async def main():
    client = GatherClient(api_key=API_KEY, space_id=SPACE_ID)
    await client.run(producer)


asyncio.run(main())

# Output
[2023-03-19 22:44:57,340][INFO] Connected to wss://engine-a00a0.aaa0-.prod.do.gather.town:443/
[2023-03-19 22:44:57,637][INFO] Connected as user USER_ID
```

### Adding extra args and kwargs

```python
import asyncio

from gather_client_ws import GatherClient


async def producer(client, *args, **kwargs):
    await client.set_text_status("new status text")
    await client.set_emoji_status("😁")
    print(args)
    print(kwargs)


async def main():
    client = GatherClient(api_key=API_KEY, space_id=SPACE_ID)
    await client.run(producer, 'arg', k='kwarg')


asyncio.run(main())

# Output
[2023-03-19 22:44:57,340][INFO] Connected to wss://engine-a00a0.aaa0-.prod.do.gather.town:443/
[2023-03-19 22:44:57,637][INFO] Connected as user USER_ID
('arg',)
{'k': 'kwarg'}
```

### Server response callback

A callback function can be defined, this function will receive the `client` and the `ServerClientBatch` message:

```python
...

async def callback(client, server_response):
    for event in server_response.events:
        print(event.WhichOneof("event"))


async def producer(client):
    await asyncio.sleep(30)  # hold the connection for 30 seconds


async def main():
    client = GatherClient(api_key=API_KEY, space_id=SPACE_ID, callback=callback)
    await client.run(producer)


asyncio.run(main())

# Output
[2023-03-19 22:56:33,840][INFO] Connected to wss://engine-a00a0.aaa0-.prod.do.gather.town:443/
[2023-03-19 22:56:34,351][INFO] Connected as user USER_ID
transactionStatus
transactionStatus
serverHeartbeat
serverHeartbeat
serverHeartbeat
```

### Logger level

It is possible to define the client log level.

```python
import logging

...

async def main():
    client = GatherClient(api_key=API_KEY, space_id=SPACE_ID, log_level=logging.DEBUG)
    await client.run(producer)


asyncio.run(main())

# Output
[2023-03-19 23:01:08,274][INFO] Connected to wss://engine-a00a0.aaa0-a.prod.do.gather.town:443/
[2023-03-19 23:01:08,581][INFO] Connected as user USER_ID
[2023-03-19 23:01:08,582][DEBUG] Receiving messages
[2023-03-19 23:01:08,582][DEBUG] Heartbeat sent
[2023-03-19 23:01:08,743][DEBUG] Message received: events {
  transactionStatus {
    txnId: 3675756270
    succeeded: true
  }
}
events {
  transactionStatus {
    txnId: 226152914
    succeeded: true
  }
}

[2023-03-19 23:01:18,514][DEBUG] Message received: events {
  serverHeartbeat {
    lastRTT: 4240423196
  }
}
```

### Actions

Listing the available actions:

```python
...
print(client.available_actions)
# Output
['client_heartbeat', 'client_backup_heartbeat', ..., 'start_recording']
```

Accessing the basic documentation of each action:

```python
...
print(client.set_text_status.__doc__)
# Output
set_text_status
Args:
        text_status (str)
        target_id (str)
```

OR

```python
help(client.craft)
# Output
Help on method method in module gather_client_ws.actions:

async method(*args, **kwargs) method of gather_client_ws.client.GatherClient instance
    craft
    Args:
            inputs (InputsEntry)
```

You can check all available actions [here](ACTIONS.md).

