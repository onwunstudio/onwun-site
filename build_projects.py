"""Builds the project pages (denglish.html, stuartfox.html, atlas.html, elev8.html, rise.html) from one shared template.

Every project page uses exactly the same layout, from _templates/project.html. To change the layout,
edit the template; to change a project's words or images, edit its entry below. Then run:

    python3 build_projects.py

Text is HTML: write "&amp;" for "&".
"""

from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "_templates" / "project.html"

# The Denglish logo, one span per letter cut from assets/denglish-logo.png (1157 × 259): left edge, width
DENGLISH_LETTERS = [(0, 161), (176, 153), (344, 158), (522, 164), (702, 63), (789, 65), (868, 117), (1002, 155)]
DENGLISH_MARK = (
    '<div class="denglish-mark" role="img" aria-label="Denglish logo">'
    + "".join(f'<span style="--x: {x}; --w: {w}; --i: {i};"></span>' for i, (x, w) in enumerate(DENGLISH_LETTERS))
    + "</div>"
)


def services(*items):
    return ' <span class="sep">/</span> '.join(items)


PROJECTS = {
    "denglish": {
        "name": "Denglish",
        # Page title, Google description and link-preview image text (image: assets/og/denglish.jpg)
        "title": "Denglish Language App Identity &amp; UI | Onwun Case Study",
        "description": "Visual identity, UI and app design for Denglish, a friendly language-learning app helping people build stronger everyday German and English.",
        "og_alt": "The Denglish logo in coral on burgundy",
        # The animated logo on burgundy
        "poster": DENGLISH_MARK,
        "poster_bg": "#440624",
        "intro": "Denglish is a friendly, accessible language-learning app designed to help users build stronger everyday German &amp; English.",
        "client": "Denglish",
        "industry": "Language app",
        "year": "2026",
        "services": services("Visual identity", "UI", "App design", "Social media"),
        "challenges": "The challenge was to turn a functional English-learning tool into a clearer, more engaging learning experience, using intuitive interactions, visible progress and a consistent visual system to make Denglish easier to use and return to every day.",
        "solution": "We created a clear, flexible visual system that makes every interaction feel simple, motivating and recognisably Denglish. A consistent colour palette, type hierarchy, icon set and progress-focused interface bring structure to the learning journey, helping users understand what to do, track improvement and stay engaged day after day.",
        "result": "A complete identity, app UI and launch social system, ready for Denglish’s waitlist launch.",
        # Chapters of images and videos after the info, the challenges and the solution
        # (see "Chapters" below the projects)
        "chapters": {
            "intro": [
                {"full": ("assets/denglish/app-icon-phone-red.webp", "The Denglish app icon on a phone home screen, against a red gradient", {"ratio": "1326 / 746"})},
                {"row": [
                    ("assets/denglish/icon.mp4", "The Denglish app icon: a white d on a red-to-burgundy gradient", {"poster": "assets/denglish/icon-poster.webp"}),
                    ("assets/denglish/palette.mp4", "The Denglish colour palette: Violet #220049, Rose #FF6978 and Burgundy #440624", {"ratio": "16 / 9", "poster": "assets/denglish/palette-poster.webp"}),
                ]},
            ],
            "challenges": [
                {"full": ("assets/denglish/stickers.mp4", "Denglish stickers: the d icon and the wordmark between sound-wave dots, in three colourways", {"ratio": "1326 / 746", "phone_ratio": "6 / 5", "poster": "assets/denglish/stickers-poster.webp"})},
            ],
            "solution": [
                {"row": [
                    ("assets/denglish/website-ipad.webp", "The Denglish website on an iPad"),
                    ("assets/denglish/app-screens.webp", "Three Denglish app screens: coach, vocabulary drill and word trainer"),
                ]},
                {"row": [
                    ("assets/denglish/post-73.mp4", "Denglish social post: Say it out loud! Today: at the cafe", {"ratio": "4 / 5", "poster": "assets/denglish/post-73-poster.webp"}),
                    ("assets/denglish/post-74.mp4", "Denglish social post: Ich hätte gern einen Kaffee, bitte. I’d like a coffee, please.", {"ratio": "4 / 5", "poster": "assets/denglish/post-74-poster.webp"}),
                 ], "caption": "Social — daily phrase series"},
            ],
        },
    },
    "stuartfox": {
        "name": "StuartFox",
        # Page title, Google description and link-preview image text (image: assets/og/stuartfox.jpg)
        "title": "StuartFox Rebrand &amp; Website | Onwun Case Study",
        "description": "A strategy-led rebrand and website for StuartFox, a Cheshire interior finishes company, reflecting the quality and precision of their work.",
        "og_alt": "StuartFox logo embossed in gold on white card",
        "poster": '<img class="poster__image" src="assets/stuartfox-mockup.webp" alt="StuartFox logo embossed in gold on white card">',
        "intro": "A clean, strategy led rebrand and website for an interior finish company based in Cheshire.",
        "client": "StuartFox",
        "industry": "Specialist finishes",
        "year": "2026",
        "services": services("Brand identity", "Social content", "Art direction"),
        "challenges": "Stuart Fox is an established interior finish company, but its previous brand and online presence did not reflect the quality, expertise or premium nature of its work. The challenge was to create a strategy-led brand that clarified its value, elevated its perception and gave potential clients a stronger reason to choose Stuart Fox over competitors. The new identity needed to communicate craft, trust and attention to detail across every touchpoint.",
        "solution": "We gave Stuart Fox a sleek new identity that finally reflects the quality of the work behind the business. We also built a clear, easy-to-use website that shows off completed projects, explains the services simply and makes it straightforward for potential clients to get in touch.",
        "result": "The result is a brand that feels more polished, trustworthy and in line with the high-end finish Stuart Fox delivers.",
    },
    "atlas": {
        "name": "ATLAS",
        # Page title, Google description and link-preview image text (image: assets/og/atlas.jpg)
        "title": "ATLAS Menswear Rental Brand &amp; App | Onwun Case Study",
        "description": "Brand identity, app design and print for ATLAS, a premium menswear rental platform built around travel, culture and Manchester’s textile history.",
        "og_alt": "An ATLAS poster on a wall reading Style rented. Journey owned.",
        "poster": '<img class="poster__image" src="assets/atlas/poster.webp" alt="An ATLAS poster on a wall reading Style rented. Journey owned.">',
        "intro": "A premium menswear rental platform built around travel, culture and Manchester’s textile history.",
        "client": "ATLAS",
        # Not a client commission: the "Client" line reads "Project type: Live brief" instead
        "live_brief": True,
        "industry": "Premium menswear",
        "year": "2026",
        "services": services("Brand identity", "UI", "App design", "Social media"),
        "challenges": "Atlas began as a response to a gap in the sustainable fashion market. The live brief also asked for the project to be grounded in Manchester’s textile history, meaning the brand needed a visual identity that could carry real cultural and historical weight, while still solving a genuine, practical problem around how people pack and dress for travel.",
        "solution": "Atlas, a premium menswear rental platform for travel, structured around the 5-4-3-2-1 packing method. The identity system centres on a logomark, which extends into a stamp system referencing passport stamps and Manchester’s historic textile trademark labels. Destination-specific colour palettes, fabric-pattern-led stickers, and printed travel guides bring each location’s culture into the brand.",
        "result": "Atlas was presented to PUBLIC’s design studio at their London studio, receiving strong feedback on the system and overall concept.",
        # Chapters of images and videos after the info, the challenges, the solution and the result
        # (see "Chapters" below the projects)
        "chapters": {
            "intro": [
                {"row": [
                    ("assets/atlas/logo-animation.mp4", "The ATLAS logo being drawn over its construction grid, on dark green", {"poster": "assets/atlas/logo-animation-poster.webp"}),
                    ("assets/atlas/palette.mp4", "The ATLAS colour palette: Meridian #3B4D4A, Horizon #DBDED1, and destination colours for Japan #221A1A, Morocco #5F1B14 and Santorini #172235", {"poster": "assets/atlas/palette-poster.webp"}),
                ]},
                {"full": ("assets/atlas/loop.mp4", "An animated ATLAS location stamp: Morocco, in terracotta on deep red", {"ratio": "1326 / 746", "poster": "assets/atlas/loop-poster.webp"})},
            ],
            "challenges": [
                {"full": ("assets/atlas/guides.webp", "ATLAS fabric travel guides for Morocco and Japan, open on their Threads of Culture spreads, with destination stickers", {"ratio": "1326 / 937"})},
            ],
            "solution": [
                {"row": [
                    ("assets/atlas/flash.mp4", "ATLAS campaign: a man under a striped beach umbrella, with the ATLAS wordmark and Pack less. Travel more.", {"ratio": "3 / 4", "poster": "assets/atlas/flash-poster.webp"}),
                    ("assets/atlas/hero.mp4", "ATLAS campaign film: Pack less. Travel more. on Meridian green", {"ratio": "16 / 9", "poster": "assets/atlas/hero-poster.webp"}),
                 ], "caption": "Campaign — Pack less. Travel more."},
            ],
        },
    },
    "elev8": {
        "name": "ELEV8",
        # Page title, Google description and link-preview image text (image: assets/og/elev8.jpg)
        "title": "ELEV8 Craft Beer Branding &amp; Packaging | Onwun Case Study",
        "description": "Brand identity and packaging for ELEV8, an electrolyte-infused craft beer reimagining beer for a healthier generation.",
        "og_alt": "ELEV8 electrolyte craft beer cans in grapefruit, mango and kiwi flavours",
        "poster": '<img class="poster__image" src="assets/elev8-mockup.webp" alt="ELEV8 electrolyte craft beer cans in grapefruit, mango and kiwi flavours">',
        # Challenges, solution and result are final; the intro is still placeholder copy
        "intro": "A bold identity and packaging system for an electrolyte craft beer brewed for active, health-aware drinkers.",
        "client": "ELEV8",
        # Not a client commission: the "Client" line reads "Project type: Live brief" instead
        "live_brief": True,
        "industry": "Electrolyte craft beer",
        "year": "2025",
        "services": services("Brand identity", "Packaging"),
        "challenges": "Beer culture is still full of stereotypes, and a new generation is choosing to drink less and live healthier. The challenge was to reimagine beer for them: a brand that feels credible as craft beer, while clearly getting the benefits of an electrolyte-infused beer across.",
        "solution": "We created ELEV8, an electrolyte-infused craft beer designed to fight next-day hangovers. A bold, condensed wordmark, flavour-led colours and a modular system of nutrition callouts put the health benefits front and centre, with playful lines that make hangovers the punchline.",
        "result": "ELEV8 reimagines beer for the next generation: enjoy the night, wake up feeling good.",
        "images": [
            ("assets/elev8/cans-night.webp", "Rows of ELEV8 cans in grapefruit, mango and kiwi flavours on a dark reflective table", {"ratio": "3 / 2"}),
            ("assets/elev8/six-pack-boxes.webp", "Three ELEV8 six-pack carry boxes in kiwi, grapefruit and mango", {"position": "40% 50%"}),
            ("assets/elev8/billboard.webp", "An ELEV8 billboard reading Electrolyte craft beer, same again tomorrow?"),
            ("assets/elev8/poster-drinking.webp", "A poster of someone drinking ELEV8, framed by green molecule shapes"),
            [
                ("assets/elev8/poster-wall.jpg", "A street poster run for ELEV8 with lines like Just beer, without the payback and Hangxiety? Never heard of her", {"ratio": "1870 / 1368"}),
                ("assets/elev8/can-labels.webp", "The ELEV8 can labels in kiwi & lime, grapefruit and mango haze", {"ratio": "1682 / 2000"}),
            ],
        ],
    },
    "rise": {
        "name": "rise",
        # Page title, Google description and link-preview image text (image: assets/og/rise.jpg)
        "title": "rise Insect Granola Branding &amp; Packaging | Onwun Case Study",
        "description": "Brand identity, visual direction and packaging for rise, a sustainable high-protein insect granola made to feel familiar and easy to enjoy.",
        "og_alt": "Three rise insect granola pouches resting on a mossy tree root",
        "poster": '<img class="poster__image" src="assets/rise-mockup.jpg" alt="Three rise insect granola pouches resting on a mossy tree root">',
        # Challenges, solution and result are final; the intro is still placeholder copy
        "intro": "A playful, sustainable identity and packaging for an insect protein granola that makes better breakfasts easy.",
        "client": "rise",
        # Not a client commission: the "Client" line reads "Project type: Live brief" instead
        "live_brief": True,
        "industry": "Insect granola",
        "year": "2025",
        "services": services("Brand identity", "Visual direction", "Packaging"),
        "challenges": "Insects are one of the most sustainable sources of protein, but for most people the idea of eating them is a hard no. rise needed to win over a sceptical audience, reducing the stigma around entomophagy so an insect-powered granola feels like a trusted breakfast, not a novelty.",
        "solution": "We made typography the brand’s main visual language. Soft, wriggling letterforms that echo a worm turn the insect story into something bold, playful and approachable, while warm colours, kraft pouches and honest messaging keep rise familiar and easy to enjoy.",
        "result": "rise makes eating insects feel normal: a high-protein breakfast people actually want to try.",
        "images": [
            ("assets/rise/pouches-pink.webp", "Three rise granola pouches in cacao, apple and coconut flavours on a pink background", {"ratio": "3 / 2"}),
            ("assets/rise/pouch-leaves.webp", "A rise apple and cinnamon pouch seen through green leaves"),
            ("assets/rise/pouches-flatlay.webp", "A flat lay of rise granola pouches, fronts and backs, with nutrition panels"),
            ("assets/rise/pouches-stump.jpg", "rise pouches propped against a tree stump on the forest floor"),
            [
                ("assets/rise/van.webp", "A brown vintage food van branded with the rise logo, menu and patterns", {"ratio": "1940 / 1290"}),
                ("assets/rise/apron.jpg", "A barista wearing a brown rise cap and apron", {"ratio": "547 / 926"}),
            ],
            [
                ("assets/rise/hoarding.jpg", "A row of rise street posters on a hoarding with a passer-by", {"ratio": "1344 / 860"}),
                ("assets/rise/billboard.jpg", "A rooftop rise billboard reading fuel your rise", {"ratio": "567 / 860"}),
            ],
        ],
    },
}


# The five image slots, top to bottom: landscape, three squares, landscape.
# Give a project an "images" list of (path, alt text) in that order; leave a slot as None for a placeholder.
# Images fill their slot, cropping the edges. Optional third item, a dict of settings:
#   {"bg": "#ffffff"}  show the whole image instead (centred, nothing cropped) on a matching background
#   {"ratio": "3 / 2"} give this slot a different shape (e.g. taller, to show more of the image), still edge to edge
#   {"position": "40% 50%"} choose which part of a cropped image stays in view (left/right %, top/bottom %)
#   {"phone_ratio": "6 / 5"} a different shape on phones, e.g. squarer, to crop away empty space at the
#                            sides so the subject fills the frame on a narrow screen
# A slot can also hold a video (an .mp4): it plays silently on a loop, like a moving image, while it's on
# screen (it only loads once it's near, so it costs nothing to people who don't scroll that far). Give it
#   {"poster": "assets/....webp"} a still frame to show until it starts
# An optional sixth item adds an image (or pair) under the Result; leave it out and nothing shows there.
# A landscape slot can also hold a pair of images side by side at the same height, filling the full width:
# give a list of two (path, alt text, {"ratio": "width / height"}) entries; each takes its share of the width.
SLOTS = ["landscape", "square", "square", "square", "landscape"]


def media_pair(images):
    items = []
    for i, (src, alt, opts) in enumerate(images):
        w, h = (float(n) for n in opts["ratio"].split("/"))
        style = f' style="--ratio: {w / h:.4f};{" --i: " + str(i) + ";" if i else ""}"'
        items.append(f'<div class="media media--pair-item reveal"{style}><img src="{src}" alt="{alt}" loading="lazy"></div>')
    return '<div class="media-pair">' + "".join(items) + "</div>"


def media_block(image, classes, stagger=0):
    """One image or video in its frame: image = (path, alt text) or (path, alt text, settings)."""
    src, alt, *rest = image
    opts = rest[0] if rest else {}
    props = [f"--i: {stagger}"] if stagger else []
    if "bg" in opts:
        classes += " media--whole"
        props.append(f"--media-bg: {opts['bg']}")
    if "ratio" in opts:
        props.append(f"aspect-ratio: {opts['ratio']}")
    if "share" in opts:
        props.append(f"--ratio: {opts['share']}")
    if "phone_ratio" in opts:
        classes += " media--phone-ratio"
        props.append(f"--phone-ratio: {opts['phone_ratio']}")
    style = f' style="{"; ".join(props)};"' if props else ""
    img_style = f' style="object-position: {opts["position"]};"' if "position" in opts else ""
    if src.endswith(".mp4"):
        poster = f' poster="{opts["poster"]}"' if "poster" in opts else ""
        return (f'<div class="{classes} reveal"{style}><video src="{src}"{poster} muted loop playsinline '
                f'preload="none" aria-label="{alt}"{img_style}></video></div>')
    return f'<div class="{classes} reveal"{style}><img src="{src}" alt="{alt}" loading="lazy"{img_style}></div>'


def media(slot, index, image):
    if isinstance(image, list):
        return media_pair(image)
    stagger = [0, 0, 1, 2, 0][index]
    style = f' style="--i: {stagger};"' if stagger else ""
    if image:
        return media_block(image, f"media media--{slot}", stagger)
    return f'<div class="filler filler--{slot} dm reveal"{style}>Coming soon</div>'


# Chapters: a project can list "chapters" instead of "images", for a freer layout (ATLAS and Denglish do). Each of
# "intro" (after the project info), "challenges", "solution" and "result" (after that text) is a list of
# blocks, stacked 20px apart, on the 20px-gutter grid:
#   {"full": image}                  one image or video across the full width (give it a "ratio")
#   {"row": [image, image]}          two side by side, half width each (square unless given a "ratio");
#                                    if they're different shapes, they share the width at the same height
#   {"row": [...], "caption": "…"}   the same, with a small caption underneath
#   {"media": image, "caption": "…", "media_side": "left" or "right"}
#                                    half-width image or video, with a small caption at the foot of the other half
# Videos get a fine border, as in the design.
def ratio_of(image):
    opts = image[2] if len(image) > 2 else {}
    return opts.get("ratio", "1")


def chapter_item(image, stagger=0, share=None):
    classes = "media media--video" if image[0].endswith(".mp4") else "media"
    opts = {**(image[2] if len(image) > 2 else {}), "ratio": ratio_of(image)}
    if share:
        opts["share"] = share  # this item's width / height, so the row's items line up at one height
    return media_block((image[0], image[1], opts), classes, stagger)


def chapter_row(images):
    ratios = [ratio_of(image) for image in images]
    if len(set(ratios)) == 1:
        items = "".join(chapter_item(image, i) for i, image in enumerate(images))
        return f'<div class="chapter__row">{items}</div>'
    shares = []
    for r in ratios:
        w, h = (float(n) for n in r.split("/")) if "/" in r else (float(r), 1.0)
        shares.append(f"{w / h:.4f}")
    items = "".join(chapter_item(image, i, shares[i]) for i, image in enumerate(images))
    return f'<div class="chapter__row chapter__row--fit">{items}</div>'


def chapter(blocks):
    if not blocks:
        return ""
    parts = []
    for block in blocks:
        if "full" in block:
            parts.append(chapter_item(block["full"]))
        elif "row" in block:
            row = chapter_row(block["row"])
            if "caption" in block:
                row = (f'<div class="chapter__group">{row}'
                       f'<p class="chapter__caption reveal">{block["caption"]}</p></div>')
            parts.append(row)
        else:
            caption = f'<p class="chapter__caption reveal">{block["caption"]}</p>'
            item = chapter_item(block["media"])
            side = block.get("media_side", "left")
            pair = item + caption if side == "left" else caption + item
            parts.append(f'<div class="chapter__row chapter__row--{side}">{pair}</div>')
    inner = "\n          ".join(parts)
    return f'<div class="chapter">\n          {inner}\n        </div>'


# Cards in each page's "More projects" strip: every project except the one you're on, in home page order
CARDS = [
    ("stuartfox", "StuartFox", "Specialist finishes · 2026", '<div class="more__image"><img src="assets/stuartfox-mockup.webp" alt="StuartFox logo embossed in gold on white card"></div>'),
    ("denglish", "Denglish", "Language app · 2026", '<div class="more__image more__image--denglish"><img src="assets/denglish-logo.png" alt="Denglish logo"></div>'),
    ("atlas", "ATLAS", "Premium menswear · Live brief · 2026", '<div class="more__image"><img src="assets/atlas/poster.webp" alt="An ATLAS poster on a wall reading Style rented. Journey owned."></div>'),
    ("elev8", "ELEV8", "Electrolyte craft beer · Live brief · 2025", '<div class="more__image"><img src="assets/elev8-mockup.webp" alt="ELEV8 electrolyte craft beer cans in grapefruit, mango and kiwi flavours"></div>'),
    ("rise", "rise", "Insect granola · Live brief · 2025", '<div class="more__image"><img src="assets/rise-mockup.jpg" alt="Three rise insect granola pouches resting on a mossy tree root"></div>'),
]


def more_cards(current):
    cards = []
    for slug, title, meta, image in CARDS:
        if slug == current:
            continue
        cards.append(
            f'''          <a class="more__card" href="{slug}.html">
            {image}
            <p class="more__title">{title}</p>
            <p class="more__meta">{meta}</p>
          </a>'''
        )
    return "\n".join(cards)


def build():
    template = TEMPLATE.read_text()
    for slug, project in PROJECTS.items():
        page = template
        poster_bg = project.get("poster_bg")
        fields = {
            **project,
            "poster_style": f' style="--poster-bg: {poster_bg};"' if poster_bg else "",
        }
        fields.pop("poster_bg", None)
        fields["slug"] = slug
        if fields.pop("live_brief", False):
            fields["client_label"], fields["client"] = "Project type", "Live brief"
        else:
            fields["client_label"] = "Client"
        fields["more_cards"] = more_cards(slug)
        chapters = fields.pop("chapters", None)
        images = fields.pop("images", None) or [None] * 5
        if chapters:
            fields["after_info"] = chapter(chapters.get("intro"))
            fields["after_challenges"] = chapter(chapters.get("challenges"))
            fields["after_solution"] = chapter(chapters.get("solution"))
            result = chapter(chapters.get("result"))
            fields["after_result"] = ("        " + result) if result else ""
        else:
            slots = [media(slot, i, images[i]) for i, slot in enumerate(SLOTS)]
            fields["after_info"] = slots[0]
            fields["after_challenges"] = ('<div class="case__squares">\n          ' + slots[1] + "\n          "
                                          + slots[2] + "\n          " + slots[3] + "\n        </div>")
            fields["after_solution"] = slots[4]
            # Optional sixth slot, under the Result: only shown when the project has an image (or pair) for it
            extra = images[5] if len(images) > 5 else None
            fields["after_result"] = ("        " + media("landscape", 4, extra)) if extra else ""
        for key, value in fields.items():
            page = page.replace("{{" + key + "}}", value)
        leftover = [part.split("}}")[0] for part in page.split("{{")[1:]]
        if leftover:
            raise SystemExit(f"{slug}: unfilled template fields: {leftover}")
        (ROOT / f"{slug}.html").write_text(page)
        print(f"built {slug}.html")


if __name__ == "__main__":
    build()
