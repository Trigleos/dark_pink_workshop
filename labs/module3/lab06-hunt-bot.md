# Lab 6: Hunting the live bot

**Module 3: Telegram C2 and hunting** · [All labs](../README.md) · Previous: [Lab 5](../module2/lab05-backdoor.md) · Next: [Lab 7](lab07-extract-messages.md)

## Goal

Use the bot token you recovered from the backdoor to identify the bot through the Telegram Bot API.

The original Dark Pink token is revoked. The BuildTask you unlocked in Lab 3 was edited by the trainer to talk to a working bot, so the token you recovered is live.

## Tools

- A browser, `curl` or Python (on the host)

## You need

- From Lab 5: the bot token

## Steps

1. On the host, identify the bot:

   ```text
   https://api.telegram.org/bot<TOKEN>/getMe
   ```

2. Note the bot's ID, username and display name.
3. Have a look at how the /getChat API method works.

## Questions

- [ ] What is the bot's username and ID?
- [ ] What is the username and ID of the person present in the chat that the bot communicates with?

## Solution

<details>
<summary>Show solution</summary>

### What is the bot's username and ID?

Visit https://api.telegram.org/bot<TOKEN>/getMe

```json
{"ok":true,"result":{"id":8929583362,"is_bot":true,"first_name":"Dark Pink Workshop","username":"darkpinkworkshopbot","can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false,"supports_guest_queries":false,"can_connect_to_business":false,"has_main_web_app":false,"has_topics_enabled":false,"allows_users_to_create_topics":false,"can_manage_bots":false,"supports_join_request_queries":false}}
```
### What is the username and ID of the person present in the chat that the bot communicates with?

Visit https://api.telegram.org/bot<TOKEN>/getChat?chat_id=<CHATID>

```json
{"ok":true,"result":{"id":6961114674,"first_name":"Suspect","last_name":"1","username":"suspectouno","type":"private","can_send_gift":true,"active_usernames":["suspectouno"],"bio":"I like travelling","accepted_gift_types":{"unlimited_gifts":true,"limited_gifts":true,"unique_gifts":true,"premium_subscription":true,"gifts_from_channels":true},"max_reaction_count":11,"accent_color_id":3}}
```

</details>

## Carry into the next lab

- The bot username, for Lab 7
