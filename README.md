# Dark Pink workshop deck

Open `index.html` in a browser (needs internet for Google Fonts; falls back to monospace offline).

- Next/previous: arrow keys, Space, PageUp/PageDown, or on-screen buttons. `#N` in the URL opens slide N.
- PDF: the PDF button prints one slide per page (all arcade effects are hidden in print).
- Theme: opens in dark purple; the hamburger menu (top right) switches to a light lavender theme.
- Slides 7, 13, 16 and 21 are animated fight slides between phases; each takes the boss's HP bar down 25%. The boss (a man-eating carnation) loses a limb per phase: snipped off with pruning shears in phases 1, 2 and 4, melted by weed-killer spray in phase 3; slide 21 ends in a K.O. with confetti.
- The player is a weed-killer exterminator in a hazmat suit. Sprites are pixel strings in the `<script>` block (`BOSS` is layered: base, face, four limbs, stumps).
- Slide 2 is the author slide. Slide 6 is a world map: the hero walks the attack chain level by level.
- Arcade layer: CRT scanlines, drifting pixel petals, pixel-dissolve transitions, typed headings, 1UP score in the HUD.
- `M` toggles 8-bit sound effects (off by default), `C` toggles CRT scanlines; both are also in the hamburger menu.
- Reduced-motion users get static slides with no canvas, wipe or flicker.
- There may be a cheat code.
- GitHub Pages: Settings > Pages > deploy from branch, then share `https://<user>.github.io/<repo>/` (Pages on a private repo needs a paid GitHub plan).

The lab sample is the real Dark Pink ISO (Telegram bot token revoked, so no C2). Lab 3 uses a trainer-edited BuildTask with a working bot (separate 7z, password = the BuildTask file name found in Lab 2); Module 3 hunts that bot. The BuildTask archive is `build_task.7z` in the workshop repo. Lab guides (with solutions) are Markdown files in `labs/`, one per lab; screenshots go in each module's `img/` folder.
