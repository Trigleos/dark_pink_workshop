# Dark Pink workshop: lab guides

Seven hands-on labs that follow the attack chain from the phishing ISO to the operator's messages on the live bot. Each lab builds on the previous one, so work through them in order.

## Before you start

- Work only inside the Flare VM, on a host-only or disconnected network.
- Take a snapshot before every lab and revert afterwards.
- The sample is the **real Dark Pink malware** from the wild, not a modified copy. Its Telegram bot token has been revoked, so it can no longer reach C2. Still treat it as live malware.
- No real credentials or personal accounts in the VM.
- The only live C2 is the trainer's own bot in the edited BuildTask (Lab 3). Query it from the host through the Telegram Bot API.
- Never open a sample on your host machine. Read these guides and use VirusTotal in the host browser; keep the samples in the VM.

## Getting the sample

1. Copy `workshop.7z` into the Flare VM.
2. Extract it with 7-Zip. Password: given in the session.
3. Check the hash before you start:

```powershell
Get-FileHash -Algorithm SHA256 '.\Proposed Concept Note on the AOIP-based Comprehensive Regional Architecture.iso'
```

Expected: `f9f2ff85bb4523a5ebd6e3e66f2d768596d0b52f5e03db62af70b7136c0f9d81`

## The BuildTask archive (Lab 3)

The original bot token is revoked, so Lab 3 uses a BuildTask edited by the trainer that talks to a working bot. It comes in a separate archive, `build_task.7z`. The password is the BuildTask file name you find in Lab 2, including the extension.

SHA-256 `24a09c8f281ad20ff9a13e4a94110c74ad73de26319f8f19a34a4da8cf47448e`

## Labs

| Lab | Module | Topic |
|-----|--------|-------|
| [1](module1/lab01-find-malicious.md) | 1: Initial loader | Find the malicious file with CFF Explorer and hashes |
| [2](module1/lab02-wwlib.md) | 1: Initial loader | Analysing wwlib.dll: drops and persistence (Procmon or Ghidra + LLM) |
| [3](module1/lab03-buildtask.md) | 1: Initial loader | The BuildTask: rebuild the two KamiKakaBot payloads |
| [4](module2/lab04-infostealer.md) | 2: KamiKakaBot | The infostealer: which browsers it targets |
| [5](module2/lab05-backdoor.md) | 2: KamiKakaBot | The backdoor: the bot token and chat ID |
| [6](module3/lab06-hunt-bot.md) | 3: Telegram C2 and hunting | Hunting the live bot: identify it with the token |
| [7](module3/lab07-extract-messages.md) | 3: Telegram C2 and hunting | Extracting the messages through the Bot API |

## Layout

Each lab has the same sections: goal, tools, what you need from earlier labs, steps, questions, hints, solution and what to carry into the next lab. Hints and solutions are folded; click to open them.

Screenshots live in each module's `img/` folder, named `labNN-<what>.png`.
