### actively_speaking

```
Args:
	actively_speaking (bool)
```

### add_inventory_item

```
Args:
	item_id (str)
	delta (int)
	target_id (str)
```

### ban

```
Args:
	user (str)
```

### block

```
Args:
	blocked_user_id (str)
	blocked (bool)
```

### chat

```
Args:
	chat_recipient (str)
	contents (str)
	local_player_ids (str)
	map_id (str)
	id (str)
	nook_id (str)
```

### chat_message_updated

```
Args:
	id (str)
```

### client_backup_heartbeat

```
Args:
```

### 
client_heartbeat

```
Args:
```

### 
craft

```
Args:
	inputs (InputsEntry)
```

### custom_action

```
Args:
	name (str)
	payload (str)
	recipients (str)
	send_to_all (bool)
```

### enter

```
Args:
	info (PlayerInitInfo)
	spawn_token (str)
	target_id (str)
```

### enter_portal

```
Args:
	target_url (str)
	bypass_prompt (bool)
	target_id (str)
```

### enter_whisper

```
Args:
	recipient_id (str)
	dir (int)
```

### exit

```
Args:
```

### 
fx_shake_camera

```
Args:
	intensity (float)
	duration_ms (float)
	map_id (str)
	target_user_id (str)
```

### fx_shake_object

```
Args:
	map_id (str)
	target_id (str)
	intensity (float)
	duration_ms (float)
	mode (int)
```

### ghost

```
Args:
	ghost (int)
	target_id (str)
```

### high_five

```
Args:
	target_id (str)
	emote (str)
```

### hip_to_be_square

```
Args:
	data (str)
```

### init

```
Args:
	space_id (str)
	token (str)
	api_key (str)
```

### interact

```
Args:
```

### 
interact_with_object

```
Args:
	map_id (str)
	key (str)
	data_json (str)
```

### join_chime_meeting

```
Args:
	media_region (str)
```

### kick

```
Args:
	user (str)
```

### leave_whisper

```
Args:
```

### 
map_add_object

```
Args:
	map_id (str)
	object (WireObject)
```

### map_delete_object

```
Args:
```

### 
map_delete_object_by_id

```
Args:
	map_id (str)
	id (str)
```

### map_delete_object_by_key

```
Args:
	map_id (str)
	key (str)
```

### map_move_object

```
Args:
	map_id (str)
	object_id (str)
	target_x (float)
	target_y (float)
	target_x_offset (float)
	target_y_offset (float)
	duration (float)
	easing (str)
```

### map_set_announcer

```
Args:
	map_id (str)
	announcer (Announcer)
```

### map_set_areas

```
Args:
	map_id (str)
	areas (AreasEntry)
	delete (bool)
```

### map_set_assets

```
Args:
	map_id (str)
	assets (Asset)
	delete (bool)
```

### map_set_background_image_path

```
Args:
	map_id (str)
	background_image_path (str)
```

### map_set_collisions

```
Args:
	map_id (str)
	x (int)
	y (int)
	w (int)
	h (int)
	mask (str)
```

### map_set_decoration

```
Args:
	map_id (str)
	decoration (str)
	delete (bool)
```

### map_set_description

```
Args:
	map_id (str)
	description (str)
	delete (bool)
```

### map_set_dimensions

```
Args:
	map_id (str)
	width (int)
	height (int)
```

### map_set_enabled_chats

```
Args:
	map_id (str)
	enabled_chats (str)
	delete (bool)
```

### map_set_floors

```
Args:
	map_id (str)
	floors (FloorsEntry)
	delete (bool)
```

### map_set_foreground_image_path

```
Args:
	map_id (str)
	foreground_image_path (str)
	delete (bool)
```

### map_set_mini_map_image_path

```
Args:
	map_id (str)
	mini_map_image_path (str)
	delete (bool)
```

### map_set_mute_on_entry

```
Args:
	map_id (str)
	mute_on_entry (bool)
	delete (bool)
```

### map_set_name

```
Args:
	map_id (str)
	name (str)
	delete (bool)
```

### map_set_nooks

```
Args:
	map_id (str)
	nooks (NooksEntry)
	overwrite (bool)
```

### map_set_objects

```
Args:
```

### 
map_set_portals

```
Args:
	map_id (str)
	portals (Portal)
```

### map_set_script

```
Args:
	map_id (str)
	script (str)
	delete (bool)
```

### map_set_spaces

```
Args:
```

### 
map_set_spawn

```
Args:
	map_id (str)
	spawn (WirePoint)
	delete (bool)
```

### map_set_spawns

```
Args:
	map_id (str)
	spawns (SpawnPoint)
```

### map_set_sprites

```
Args:
```

### 
map_set_tutorial_tasks

```
Args:
	map_id (str)
	tutorial_tasks (WireTutorialTasks)
	delete (bool)
```

### map_set_use_drawn_b_g

```
Args:
	map_id (str)
	use_drawn_b_g (bool)
	delete (bool)
```

### map_set_walls

```
Args:
	map_id (str)
	walls (WallsEntry)
	delete (bool)
```

### map_update_objects

```
Args:
	map_id (str)
	objects (ObjectsEntry)
	updates_are_overwrites (bool)
```

### move

```
Args:
	dir (int)
	stopped (bool)
	input_id (int)
	target_id (str)
```

### notify

```
Args:
	notification (str)
```

### play_sound

```
Args:
	src (str)
	volume (float)
	target_id (str)
```

### player_updates_session

```
Args:
```

### 
precompute_enter

```
Args:
	enter_location (MapLocation)
	spawn_token (str)
```

### register_command

```
Args:
	command (str)
```

### remove_inventory_item

```
Args:
	item_id (str)
	delta (int)
	target_id (str)
```

### request_access_via_check_in

```
Args:
	user_id (str)
	canceled (bool)
	name (str)
	currently_equipped_wearables (DBOutfit)
```

### request_mute

```
Args:
	target (str)
	video (bool)
```

### request_to_join_nook

```
Args:
	nook_id (str)
	map_id (str)
	name (str)
```

### request_to_lead

```
Args:
	target (str)
	snapshot (str)
```

### respawn

```
Args:
```

### 
respawn_at_desk

```
Args:
```

### 
respond_to_access_request

```
Args:
	user_id (str)
	accepted (bool)
	location_type (int)
```

### ring

```
Args:
	user (str)
```

### send_command

```
Args:
	command (str)
	target_id (str)
```

### set_affiliation

```
Args:
	affiliation (str)
	target_id (str)
```

### set_allow_screen_pointer

```
Args:
	allow_screen_pointer (bool)
```

### set_availability

```
Args:
	availability (str)
	end_option (str)
```

### set_away

```
Args:
	away (bool)
	target_id (str)
```

### set_city

```
Args:
	city (str)
	target_id (str)
```

### set_country

```
Args:
	country (str)
	target_id (str)
```

### set_current_area

```
Args:
	current_area (str)
	target_id (str)
```

### set_current_desk

```
Args:
```

### 
set_currently_equipped_wearables

```
Args:
	currently_equipped_wearables (DBOutfit)
	target_id (str)
```

### set_description

```
Args:
	description (str)
	target_id (str)
```

### set_desk_from_next_available_desk

```
Args:
	target_id (str)
	preferred_desk (MapAndDesk)
	desks_to_ignore (MapAndDesk)
```

### set_desk_info

```
Args:
	desk_info (DeskInfoV2)
	target_id (str)
```

### set_display_email

```
Args:
	display_email (str)
	target_id (str)
```

### set_emoji_status

```
Args:
	emoji_status (str)
	target_id (str)
```

### set_emote_v2

```
Args:
	emote (str)
	target_id (str)
	count (int)
```

### set_event_status

```
Args:
	event_status (str)
	target_id (str)
```

### set_focus_mode_end_time

```
Args:
	focus_mode_end_time (str)
	target_id (str)
```

### set_follow_target

```
Args:
	follow_target (str)
	target_id (str)
```

### set_go_kart_id

```
Args:
```

### 
set_image_pointer

```
Args:
	object_id (str)
	x (float)
	y (float)
```

### set_impassable

```
Args:
	map_id (str)
	x (int)
	y (int)
	impassable (bool)
```

### set_in_conversation

```
Args:
	in_conversation (bool)
	target_id (str)
```

### set_is_alone

```
Args:
	is_alone (bool)
	target_id (str)
```

### set_is_mobile

```
Args:
	is_mobile (bool)
```

### set_item_string

```
Args:
	item_string (str)
	target_id (str)
```

### set_manual_video_src

```
Args:
	manual_video_src (str)
	target_id (str)
```

### set_name

```
Args:
	name (str)
	target_id (str)
```

### set_outfit_string

```
Args:
```

### 
set_personal_image_url

```
Args:
	personal_image_url (str)
	target_id (str)
```

### set_phone

```
Args:
	phone (str)
	target_id (str)
```

### set_profile_image_url

```
Args:
	profile_image_url (str)
	target_id (str)
```

### set_pronouns

```
Args:
	pronouns (str)
	target_id (str)
```

### set_screen_pointer

```
Args:
	screen_id (str)
	x (float)
	y (float)
```

### set_space_role_permission_override

```
Args:
	role (str)
	permission (str)
	enabled (bool)
```

### set_speed_modifier

```
Args:
	speed_modifier (float)
	target_id (str)
```

### set_start_date

```
Args:
	start_date (str)
	target_id (str)
```

### set_status

```
Args:
	status (bool)
	target_id (str)
```

### set_subtitle

```
Args:
	subtitle (str)
	target_id (str)
```

### set_text_status

```
Args:
	text_status (str)
	target_id (str)
```

### set_timezone

```
Args:
	timezone (str)
	target_id (str)
```

### set_title

```
Args:
	title (str)
	target_id (str)
```

### set_vehicle_id

```
Args:
	vehicle_id (str)
	target_id (str)
	action (str)
```

### set_work_condition

```
Args:
```

### 
shoot_confetti

```
Args:
	target_id (str)
```

### spawn

```
Args:
	spawn_token (str)
```

### speaker_updates_session

```
Args:
	session_id (str)
	customize_room_enabled (bool)
	chat_enabled (bool)
	qa_enabled (bool)
	approve_questions_enabled (bool)
	mass_mute_enabled (bool)
```

### spotlight

```
Args:
	spotlighted_user (str)
	is_spotlighted (bool)
```

### start_recording

```
Args:
	nook_id (str)
	initializing (bool)
```

### stop_sound

```
Args:
	src (str)
	target_id (str)
```

### teleport

```
Args:
	map_id (str)
	x (int)
	y (int)
	target_id (str)
	direction (int)
```

### trigger_inventory_item

```
Args:
	item_id (str)
	ability_id (str)
```

### trigger_item

```
Args:
```

### 
trigger_object

```
Args:
	map_id (str)
	key (str)
```

### update_nook_permission

```
Args:
	player_id (str)
	nook_id (str)
	granted (bool)
```

### update_space_items

```
Args:
	items (ItemsEntry)
```

### update_subscriptions

```
Args:
	subscriptions (SubscriptionsEntry)
	map_update_ids (MapUpdateIdsEntry)
```

### wave

```
Args:
	user (str)
	is_reply (bool)
```

### 
