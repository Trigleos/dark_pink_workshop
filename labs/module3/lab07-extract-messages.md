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

## Steps

1. Read through the list of available methods in the Bot API documentation.
2. Find the methods that let a bot read or move messages in a chat it belongs to. Note what each one needs.
3. Rule out methods that would disturb the backdoor or tip off the operator on a real case.
4. Use the method you picked to get the operator's messages into a chat you control.
5. Read the messages in order.

> TODO: add any setup attendees need

## Questions

- [ ] Which methods did you consider, and which did you use?
- [ ] Why did you rule out the others?
- [ ] How many messages did you recover?
- [ ] What did the operator send, and what came back from the victim?

## Hints

<details>
<summary>Hint 1</summary>

Look for a method that copies an existing message from one chat to another, given its message ID.

</details>

<details>
<summary>Hint 2</summary>

> TODO

</details>

## Solution

<details>
<summary>Show solution</summary>

> TODO: add screenshots and notes

<!-- ![First recovered message](img/lab07-first-message.png) -->
<!-- ![Recovered history](img/lab07-history.png) -->

</details>
