# Gather WebSocket Client

## Installation
```
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

``` python
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

``` python
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

``` python
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
['client_heartbeat', 'client_backup_heartbeat', 'update_subscriptions', 'move', 'set_affiliation', 'set_status', 'spotlight', 'ring', 'ban', 'kick', 'set_impassable', 'chat', 'interact', 'enter_whisper', 'leave_whisper', 'set_emoji_status', 'actively_speaking', 'set_name', 'set_text_status', 'teleport', 'exit', 'enter', 'set_work_condition', 'respawn', 'spawn', 'ghost', 'init', 'set_outfit_string', 'shoot_confetti', 'set_event_status', 'set_in_conversation', 'set_current_desk', 'set_current_area', 'set_image_pointer', 'set_go_kart_id', 'map_set_dimensions', 'map_set_collisions', 'map_set_background_image_path', 'map_set_foreground_image_path', 'map_set_sprites', 'map_set_spawns', 'map_set_spaces', 'map_set_portals', 'map_set_announcer', 'map_set_assets', 'map_set_objects', 'map_set_name', 'map_set_mute_on_entry', 'map_set_use_drawn_b_g', 'map_set_walls', 'map_set_floors', 'map_set_areas', 'map_add_object', 'map_delete_object', 'map_set_spawn', 'set_is_alone', 'map_set_mini_map_image_path', 'map_set_enabled_chats', 'map_set_description', 'map_set_decoration', 'map_set_tutorial_tasks', 'play_sound', 'map_set_script', 'set_is_mobile', 'set_screen_pointer', 'set_emote_v2', 'set_focus_mode_end_time', 'map_delete_object_by_id', 'custom_action', 'block', 'set_item_string', 'trigger_item', 'notify', 'set_follow_target', 'request_to_lead', 'enter_portal', 'set_manual_video_src', 'set_subtitle', 'player_updates_session', 'map_move_object', 'chat_message_updated', 'fx_shake_object', 'fx_shake_camera', 'register_command', 'send_command', 'speaker_updates_session', 'add_inventory_item', 'remove_inventory_item', 'set_vehicle_id', 'set_speed_modifier', 'high_five', 'update_space_items', 'stop_sound', 'hip_to_be_square', 'craft', 'trigger_inventory_item', 'set_allow_screen_pointer', 'precompute_enter', 'request_mute', 'set_desk_info', 'map_set_nooks', 'request_to_join_nook', 'update_nook_permission', 'wave', 'set_pronouns', 'set_title', 'set_timezone', 'set_phone', 'set_description', 'set_profile_image_url', 'set_personal_image_url', 'set_away', 'set_city', 'set_country', 'set_start_date', 'start_recording']
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
