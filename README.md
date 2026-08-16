<p align="center">
  <img src="./.github/readme-assets/playground.gif" alt="Animated playground / experience visual for 4-digit-guess" width="100%" />
</p>

<h1 align="center">4-digit-guess</h1>

<p align="center"><strong>Small static client-side web app (CodeBreaker) that assigns a 4-digit secret per player in Firestore and includes a Playwright Python script demonstrating brute-force attempts.</strong></p>

<p align="center"><code>REPO//SIGNAL</code> · <code>PLAYGROUND / EXPERIENCE</code> · <code>LOOPING README EXPERIENCE</code></p>

## Live signal

| Lens | Readout |
| --- | --- |
| Portfolio lane | **PLAYGROUND / EXPERIENCE** |
| Code surface | **7** tracked files observed |
| Primary materials | **HTML, Markdown, Python, JavaScript** |
| Verification | **0** test-related files observed |

> A kinetic frame for interaction, play, and visual craft. The animated frame above is a lightweight visual signature; the sections below remain the source of truth for implementation details.

## Motion map

`DISCOVER` → `INTERACT` → `ITERATE`

Start with the experience surface, follow the main interaction loop, then iterate on feedback, accessibility, and performance. The README is designed as a quick visual entry point before the deeper project dossier.

<details open>
<summary><strong>Open the full project dossier</strong></summary>

## Overview
A minimal, client-only prototype that implements a simple PIN-guessing game using browser code and direct Firestore access. The repository contains three HTML pages (registration, cracking UI, leaderboard), a firebase.js module with Firebase configuration, and a Playwright automation script (crack.py) that demonstrates automated brute-force against a similar UI.

## What it does
- index.html: lets a user register a display name and (client-side) assigns a 4-digit secret code stored in Firestore.
- crack.html: lets a user enter a 4-digit PIN; the client compares/submits attempts and may update the player document (fields like attempts, cracked, crackedAt).
- leaderboard.html: queries Firestore for players with cracked==true and lists them ordered by crackedAt.
- firebase.js: contains the Firebase configuration used by the client (projectId, messagingSenderId, appId and an apiKey line that is malformed in the repository).
- crack.py: a Python Playwright script intended to automate brute-force attempts (evidence shows it uses selectors that differ from crack.html, making it brittle).

## Key capabilities
- Register a name and persist a player document under players/<lowercase name>.
- Client-side generation and storage of a 4-digit secret code (secretCode field).
- Client-side attempt submission and updates to attempts, cracked (bool), and crackedAt (timestamp).
- Leaderboard querying for cracked players ordered by crackedAt.
- Local name persistence via localStorage.
- Client-side modal UI to change the PIN (markup present).
- Playwright (Python) script illustrating brute-force automation.

## Technology
- HTML/CSS/vanilla JavaScript (ES modules)
- Firebase Firestore (used from client SDK v10.x as observed in firebase.js)
- Playwright (Python) for automation/brute-force demo

## Repository structure
Top-level files observed:
- index.html — registration and PIN creation UI.
- crack.html — PIN entry / cracking UI.
- leaderboard.html — leaderboard view querying cracked players.
- firebase.js — Firebase initialization/configuration module (contains project metadata and a malformed apiKey line).
- crack.py — Python Playwright automation script demonstrating brute-force attempts.
- style.css — styles for the static pages.
- README.md — existing file appears corrupted; this file replaces/supplements it.

## Getting started
There are no explicit setup or run instructions, build files, or dependency manifests in the repository. This appears to be a static, client-only prototype.

To inspect and try the project locally (non-speculative, code-review route):
- Open the HTML and JavaScript files (index.html, crack.html, leaderboard.html, firebase.js) in an editor to review behavior and Firebase usage.
- Open the pages in a browser to exercise the UI as-is (the firebase.js apiKey line is malformed and may prevent initialization).
- Inspect crack.py to review the automation approach and the selectors it uses.

Note: There is no documented local dev server, package manifest, or dependency list in the repo.

## Configuration
- The app uses Firestore directly from the browser. firebase.js contains client config values (projectId, messagingSenderId, appId and an apiKey line that is malformed).
- Player documents live in the Firestore collection named "players" and are keyed by the lowercase display name.
- Document fields observed: secretCode (plaintext), cracked (bool), crackedAt (timestamp), attempts (number), displayName.
- No Firebase security rules or server-side code are present in the repository (no rules/ or functions/ directories found).

## Development and quality notes
- All verification and security-related logic runs on the client; secretCode is stored in Firestore in plaintext and is readable/modifyable by any client with DB access.
- No unit tests, CI configuration, or linters are present.
- crack.py is an automation/brute-force demonstration and uses selectors that do not align with the crack.html markup in this repo, making it brittle.
- firebase.js contains a malformed apiKey line which will break initialization as-is.

Recommendations for contributors (based on observed gaps, not prescriptive commands):
- Review firebase.js and the Firestore read/write points in index.html and crack.html.
- Avoid running crack.py against a live project until Firestore rules and project configuration are audited.
- Prioritize moving secret verification to a trusted backend and adding restrictive Firestore rules before using the app with real users or data.

## Safety and responsible use
- The repository demonstrates several security weaknesses: plaintext secret storage in Firestore, predictable document IDs (players/<name.toLowerCase()>), unauthenticated client-side writes, and no rate-limiting. These make brute-force and unauthorized modifications trivial.
- crack.py is a brute-force automation script; running it against a live project can be abusive and may violate acceptable-use or security policies. Do not run attacks against systems you do not own or have explicit permission to test.
- If this code is connected to a live Firebase project, audit and tighten Firestore security rules immediately and rotate credentials if necessary.

## Contributing
- No contribution guidelines are present. Suggested, minimal first steps for contributors:
  - Inspect index.html, crack.html, leaderboard.html, firebase.js, and crack.py to understand current behavior.
  - Open issues describing desired fixes (e.g., move PIN verification server-side, add Firestore rules, fix firebase.js syntax).
  - Propose pull requests that address specific, reviewable changes (e.g., removing client-side secret comparisons, adding server-side endpoints, aligning selectors in crack.py).
- Do not assume existing tests or CI; include changes and rationale in PR descriptions.

(There is no license file explicitly included in the repository evidence.)

</details>

---

<p align="center"><sub>README motion system · visual layer by RepoSignal · implementation details remain project-specific</sub></p>
