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

> TODO: add any other steps

## Questions

- [ ] What is the bot's username and ID?
- [ ] On a real case, which of these calls could disrupt the backdoor or tip off the operator?

## Hints

<details>
<summary>Hint 1</summary>

> TODO

</details>

## Solution

<details>
<summary>Show solution</summary>

> TODO: add screenshots and notes

<!-- ![getMe response](img/lab06-getme.png) -->

</details>

## Carry into the next lab

- The bot username, for Lab 7
