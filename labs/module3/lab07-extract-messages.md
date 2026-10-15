# Lab 7: Extracting the messages

**Module 3: Telegram C2 and hunting** · [All labs](../README.md) · Previous: [Lab 6](lab06-hunt-bot.md) · Next: [Lab 8](lab08-yara-vt.md)

## Goal

Get the operator's messages out of the C2 chat and into a chat you control, using the Telegram Bot API.

## Tools

- The Telegram Bot API documentation: <https://core.telegram.org/bots/api>
- Your Telegram account (on the host)
- A browser, `curl` or Python (on the host)

## You need

- From Lab 5: the bot token and the chat ID
- From Lab 6: the bot username
- A Telegram account

## Steps

1. Read through the list of available methods in the Bot API documentation.
2. Find the methods that let a bot read or move messages in a chat it belongs to. Note what each one needs.
3. Use the method you picked to get the operator's messages into a chat you control.
4. Read the messages in order.

## Questions

- [ ] Which flag is hidden in the C2 channel

## Hints

<details>
<summary>Hint 1</summary>

Look for a method that forwards an existing message from one chat to another, given its message ID.

</details>

## Solution

<details>
<summary>Show solution</summary>

First start a chat with the bot by searching for the bot username you found earlier.

Retrieve your own user ID by starting a chat with @UserIDToBot

Visit https://api.telegram.org/bot8929583362:AAEe5cG_z6Rusg8YGL-vvFJloILbzz-eBCA/forwardMessage?from_chat_id=6961114674&chat_id=your_own_id&message_id=1

The message will be forwarded to your chat with the bot.

Increase the message id to forward the following messages.

</details>
