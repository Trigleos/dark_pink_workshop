# Lab 1: Find the malicious file

**Module 1: Initial loader** · [All labs](../README.md) · Next: [Lab 2](lab02-wwlib.md)

## Goal

Mount the phishing ISO, look at every file in CFF Explorer, check the hashes, and work out which file is malicious and how it gets loaded.

## Tools

- Windows Explorer (mount), `cmd` or PowerShell
- CFF Explorer
- Ghidra (optional, to see how the DLL is loaded)
- VirusTotal (in the browser on your host)

## You need

- `Proposed Concept Note on the AOIP-based Comprehensive Regional Architecture.iso`
- SHA-256 `f9f2ff85bb4523a5ebd6e3e66f2d768596d0b52f5e03db62af70b7136c0f9d81`

## Steps

1. Check the SHA-256 of the ISO matches the one above.
2. Right-click the ISO and choose **Mount**. Note the drive letter.
3. Look at the drive in Explorer first: what would a victim see?
4. List everything, including hidden files:

   ```cmd
   dir /a D:\
   ```

5. Open each file in CFF Explorer. For each one note the file type, the MD5 and SHA-1 on the main page, and the version information.
6. Look up each hash on VirusTotal from your host. Which files are known and legitimate, and which are not?
7. Look at the imports of the `.docx.exe` in CFF Explorer (**Import Directory**). Is the suspicious DLL there?
8. If it is not, work out how the EXE loads it anyway.

## Questions

- [ ] Which files are visible, and which are hidden?
- [ ] What is the `.docx.exe` really?
- [ ] Which file is malicious?

## Hints

<details>
<summary>Hint 1</summary>

Compare the `.docx.exe` hash and version information with a real Microsoft Word install.

</details>

<details>
<summary>Hint 2</summary>

A DLL does not have to be in the import table to be loaded. Search the EXE for the DLL name as a string, and look for `LoadLibrary` in its imports.

</details>

## Solution

<details>
<summary>Show solution</summary>

### Which files are visible, and which are hidden?

- Visible: .docx.exe and .pdf
- Hidden: .doc and .dll

### What is the `.docx.exe` really?

Search the hashes on VirusTotal to find out that the docx.exe file is only a renamed winword.exe file:

![Executable Signature](img/signed.PNG)

### Which file is malicious?

wwlib.dll is. You can look at the imports of the .docx.exe file but it does not directly import the library. To find out how it is loaded, you need to open the executable in Ghidra and search for the string "wwlib.dll" to find out where it's used by searching for references to the string (CTRL + SHIFT + F for Ghidra/X for Ida).

![wwlib.dll](img/wwlib.PNG)

This function uses the wwlib.dll string and calls LoadLibraryExW to set up the DLL and use it.

![LoadLibrary](img/LoadLibrary.PNG)


Alternatively, simply google wwlib.dll and see that it's used in conjunction with winword.

</details>

## Carry into the next lab

- `wwlib.dll`, the malicious file
- The hidden `.doc`, which you will see again in Lab 2
