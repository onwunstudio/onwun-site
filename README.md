# Onwun website

The Onwun studio website: plain HTML, CSS and JavaScript, with no framework and no build step on the
server. Whatever is in this repository is the website.

The design lives in Figma (file key `mqXy4ijxUtGTShfBYJHcHP`): the home page on "Page 1", the project
pages on "Project Pages", plus "Contact Page" and "About Us". Figma is the design copy; these files are
what gets published, so changes made only in Figma don't appear on the site until the code is updated.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home |
| `about.html` | About us |
| `contact.html` | Contact ("Talk to us") |
| `stuartfox.html`, `denglish.html`, `atlas.html`, `elev8.html`, `rise.html` | Project pages, **generated** (see below) |
| `assets/` | Images and logos |

Each page holds its own styles and scripts. The nav, phone menu, closing statement and footer are
repeated on every page, so a change to one of them needs making on each page (and in the project
template).

## Previewing the site

You need Python 3 (already on most Macs). From this folder, run:

```bash
python3 .claude/serve.py 8765
```

Then open http://localhost:8765. The preview server tells the browser not to cache, so a normal refresh
always shows the latest files. In Claude Code, the "static" preview in `.claude/launch.json` does the
same thing.

To see it on a phone on the same Wi‑Fi, open `http://<this computer's local IP>:8765`.

## Project pages

The five project pages are all built from one template, so **don't edit `stuartfox.html`,
`denglish.html`, `atlas.html`, `elev8.html` or `rise.html` directly**: they are overwritten every time
the pages are rebuilt.

- To change the layout of every project page: edit `_templates/project.html`.
- To change a project's words or images, or add a new project: edit its entry in `build_projects.py`
  (the comments there explain the image options).

Then rebuild the pages:

```bash
python3 build_projects.py
```

A new project also needs a card on the home page (`index.html`) and an entry in the "More projects"
list near the bottom of `build_projects.py`. Give it a `title`, `description` and `og_alt` (its Google
title, Google description and link-preview image text) and a 1200 × 630 preview image at
`assets/og/<slug>.jpg`.

## Search and link previews

Each page's header has its Google title and description, a canonical address on `https://onwun.com`,
and Open Graph tags so shared links show a preview card. The home, About and Contact pages use
`assets/og/onwun.jpg`; each project uses its own image in `assets/og/`. Previews only work once the
site is live on onwun.com.

## House style

- Colours: black background, white text, purple `#6A60F6`; greys `#626675` (labels) and `#C9CAD0`
  (soft text).
- Type: Sora (Light for body and statements, SemiBold or Bold for titles); DM Sans Medium for small
  uppercase labels.
- Layout: 20px page edges; two columns of 660px and 626px with a 40px gap at 1366px wide; 138px of space
  above and below each section.
- Phones (under 900px wide) have their own rules at the bottom of each page's styles, so phone changes
  don't affect desktop.

## Working together

1. Before starting, get the latest version (**Fetch / Pull** in GitHub Desktop).
2. Make your changes and check them in the preview.
3. If you changed a project page, run `python3 build_projects.py`.
4. **Commit** with a short note of what changed, then **Push**. The hosting service publishes the new
   version automatically.

Try not to edit the same page at the same time; if you do, Git will flag the overlap when you pull.

## Still to do

- Connect the contact form to a form service (e.g. Formspree); it doesn't send anything yet.
- Real links for Instagram, LinkedIn, "Book a discovery call" (Calendly), T&Cs and Privacy policy.
- Team photos and the real list of services on the About page.
- Intros for ELEV8 and rise; project images for StuartFox and ATLAS.
- SEO basics still to add: favicon, a main heading on the home page, sitemap and robots file, 404 page.
