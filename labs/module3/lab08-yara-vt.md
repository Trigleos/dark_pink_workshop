# Lab 8: Hunting with YARA on VirusTotal

**Module 3: Telegram C2 and hunting** · [All labs](../README.md) · Previous: [Lab 7](lab07-extract-messages.md)

## Goal

Fill a starter YARA rule with candidate strings from your own analysis, decide which are worth hunting on, and test your rule on VirusTotal.

## Tools

- YARA (in the VM)
- VirusTotal (in the browser on your host)

## You need

- The starter rule (below)
- Your notes and samples from Labs 1 to 7

> TODO: note which VirusTotal features attendees need (e.g. content search, Retrohunt) and what to do without a VirusTotal Intelligence account

## Starter rule

Save this as `starter.yar`. The strings are only examples showing the different string types: replace them with strings from your own analysis in Labs 1 to 7.

```yara
rule DarkPink_KamiKakaBot_Starter
{
    meta:
        description = "Lab 8 starter rule: replace the example strings with your own"

    strings:
        $s1 = "ExampleUniqueString" ascii wide     // text string, ASCII and UTF-16
        $s2 = "Hello World" ascii                  // a very common string: keep it?
        $s3 = { 4D 5A 90 00 }                      // hex bytes
        $s4 = /example[0-9]{2}\.txt/ nocase        // regular expression

    condition:
        any of them
}
```

Also think about the condition: `any of them` is a starting point, not an answer.

## Steps

1. Replace the example strings with candidates from Labs 1 to 7. For each one, ask whether the author is likely to change it between samples.
2. Check each string against clean files in the VM:

   ```cmd
   yara64 -r -s starter.yar C:\Windows\System32
   ```

3. Search for each string on VirusTotal. Too many hits means too generic, one hit means too specific.
4. Fill in the table and trim the rule to the strings you keep.
5. Check that your rule still matches the payloads from Lab 3.

| String | Stable across samples? | In clean files? | VirusTotal hits | Keep? |
|--------|------------------------|-----------------|-----------------|-------|
| | | | | |

## Questions

- [ ] Which strings are best to hunt on, and why?
- [ ] Which strings did you drop, and why?
- [ ] What does your final rule find on VirusTotal?

## Hints

<details>
<summary>Hint 1</summary>

> TODO

</details>

## Solution

<details>
<summary>Show solution</summary>

> TODO: add the reference rule, screenshots and notes

```yara
// TODO: reference rule
```

<!-- ![VirusTotal results](img/lab08-vt.png) -->

</details>

## Next

You have followed the chain from the ISO to a hunt on VirusTotal. That is the whole workshop.
