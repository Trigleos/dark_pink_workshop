# Lab 2: Analysing wwlib.dll

**Module 1: Initial loader** · [All labs](../README.md) · Previous: [Lab 1](lab01-find-malicious.md) · Next: [Lab 3](lab03-buildtask.md)

## Goal

Work out what `wwlib.dll` does: which files it drops, where it stores them and how it persists. This is the longest lab. Pick one of two routes, or do both.

## Tools

- Route A (fast): Procmon
- Route B (deep): Ghidra and an LLM

## You need

- From Lab 1: the ISO contents, with `wwlib.dll` identified as malicious

## Route A: Procmon

1. Take a snapshot.
2. Copy the ISO contents into a working folder.
3. Start Procmon and set filters:
   - **Process Name** is the `.docx.exe` file name, plus any child processes it starts (use **Tools > Process Tree** afterwards)
   - **Operation** is `CreateFile`, `WriteFile` or `RegSetValue`
4. Run the `.docx.exe` and wait a few seconds, then stop the capture.
5. Read the file writes and registry changes. Note every path.
6. Check the files on disk and the persistence you found, then revert the snapshot.

## Route B: Ghidra and an LLM

1. Import `wwlib.dll` into Ghidra and run auto-analysis.
2. Start from `DllMain` and the exports, and find the two main functions that do the work.
3. Give each function's pseudo-C to an LLM, one at a time, using the prompt pattern from the deck:

   ```text
   Context: what the function is for
   Input:   pseudo-C from Ghidra
   Ask:     explain it; list every file path, registry key and API call it uses
   Verify:  I will check the paths against the strings and the files on disk
   ```

4. Rename the functions and variables in Ghidra as you go.
5. Check each answer: look the paths and keys up in the strings and confirm them.

> TODO: add the names or addresses of the two main functions if you want to give attendees a head start

## Questions

- [ ] What do the two main functions do?
- [ ] Which files are dropped, and where?
- [ ] What happens to the hidden `.doc` from the ISO?
- [ ] How does the malware persist?
- [ ] What is the BuildTask (MSBuild project) file called?
- [ ] What does the victim see while all this happens?

## Hints

<details>
<summary>Hint 1</summary>

> TODO

</details>

## Solution

<details>
<summary>Show solution</summary>

> TODO: add screenshots and notes for both routes

<!-- ![Procmon file writes](img/lab02-procmon.png) -->
<!-- ![Persistence](img/lab02-persistence.png) -->
<!-- ![Ghidra: main function 1](img/lab02-ghidra-1.png) -->
<!-- ![Ghidra: main function 2](img/lab02-ghidra-2.png) -->

</details>

## Carry into the next lab

- The BuildTask file name: it is the password for the BuildTask archive in Lab 3
- The drop paths and the persistence mechanism
