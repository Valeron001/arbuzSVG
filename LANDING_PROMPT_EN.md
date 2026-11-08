# LANDING PAGE BUILD PROMPT — "ARBUZ" SHOPPING & LOGISTICS HUB, SOVETSKAYA GAVAN
### English-language investor landing page · single-page web build · for Claude Code

> **How to use:** paste this whole file into Claude Code as the build instruction, or save it
> as `CLAUDE.md` in the project root and then say "build the landing page".
> Everything needed is inline: sources, hard rules, measured design tokens, section-by-section
> copy, verified numbers, vector-art recipes, chart specs, and acceptance criteria.

---

## 0. THE TASK

Build a **single-page, English-language investor landing page** for a commercial real
estate asset in the Russian Far East. The page must persuade a professional CRE buyer
(mall operator, family office, regional fund, co-investor) that the asset deserves a
second look — and it must survive a sceptical analyst reading the numbers.

**Sources of truth (do not re-derive, do not re-OCR):**

| File | What it is |
|---|---|
| `Презентация_368м ТЕКСТ.pdf` | Investment memorandum, 6 blocks, Russian. The copy and figure source. |
| `Комплекс_Сов.Гавань_368м.pdf` | 15-slide visual deck (image-only raster, no text layer). The design language source. |
| `Комплекс_Сов.Гавань_368м_1.png` … `_15.png` | The 15 slides as flattened rasters, 1686×933 px. **Usable as images on the page — but never crop them. See rule R1.** |

**Deliverable:** one self-contained `index.html` with embedded CSS and JS. No build step,
no framework, no bundler, no npm dependencies. It must open by double-click from disk,
work offline, and be responsive from 375 px to 1920 px, with a clean A4 print stylesheet.

---

## 1. HARD RULES (violating any of these fails the build)

**R1 — DO NOT CROP PHOTOGRAPHS OUT OF THE SLIDE PNGs.**
This is the **only** image-provenance rule in this prompt. Each of the 15 PNGs is a
flattened slide raster: the deck's design language, its annotation layer and its Russian
text are all baked into the same image.

- ❌ The one prohibited operation: **cutting a photo region out of a slide PNG and using
  that cut-out as a picture on the page** — a facade, an interior, a floor plan, a map, a
  warehouse, anything photographic.

Everything else about the slide images is permitted:

- ✅ embedding a whole slide PNG on the page as an image;
- ✅ using a whole slide PNG as the visual for a section — it shows the real asset with
  the deck's own annotation layer, which is a legitimate and self-consistent choice;
- ✅ taking the deck's palette, geometry, proportions and layout as the design reference.
  That is exactly what they are for.

One practical note if you embed a slide PNG: it is a 1686×933 raster with Russian text
baked in, so it reads as a deck slide rather than as a photograph. Use it where the deck's
own annotated slide is the better answer (a floor-plan slide, the discount slide), and use
the §6 vector art where the page needs a clean English graphic. Never crop it to make it
look like a photo.

**R2 — The one permitted exception.** If a section genuinely needs a photograph and no
vector substitute is acceptable, leave a clearly-labelled empty frame — a dashed
1px `#CBD5CC` border, a `#F4F7F5` fill, a centred caption in 14px muted type reading
`PHOTO — <what belongs here>` — and list it in the changelog as a slot for the owner to
fill with original photography. Fill that slot with original photography of this asset,
not with stock imagery of a generic shopping centre, and never by cropping a slide PNG.

**R3 — Do not fabricate.** Every figure on the page comes from §5 of this prompt. No
invented testimonials, no fake bidder logos, no fabricated "typical ROI" claims, no
made-up tenant names beyond those listed in the memorandum.

**R4 — No generic stock imagery.** No free-stock mall photos, no map tiles from external
services, no icon fonts from CDNs. Any image on the page must show this asset — either
drawn as vector art (§6), taken from the deck's own slide rasters (R1), or drawn live on
a canvas as the 3D watermelon (§7 of this prompt).

**R5 — No external runtime dependencies.** No CDN chart library, no CDN icon set, no CDN
webfont as a hard requirement. If you use a Google Font, it must degrade gracefully to
the system stack and the page must be fully readable without it.

**R6 — Numbers must be honest.** Where the source memorandum is internally inconsistent,
the corrected value in §5 wins, and the deck's erroneous value must not be printed.

---

## 2. AUDIENCE, TONE, PAGE TYPE

- **Primary audience:** professional CRE buyers in the Russian Far East and Siberia — mall
  owner-operators, heads of asset management, boutique CRE brokers, local family offices,
  ЗПИФ/SPV platforms. Secondary: co-investors bringing capital who want the land bank
  redeveloped.
- **They are numerate and sceptical.** They know a 6.27% cap rate is below their screen.
  Do not hide it — *explain* it, and show the operating gap that creates the upside.
- **Page type: Decide / Learn.** A hero is correct here, but only in the first screen.
  Every later section must land exactly one idea.
- **Tone:** factual, institutional, plain English. No marketing superlatives. No
  "unbeatable", "guaranteed", "risk-free", "once-in-a-lifetime". Numbers do the work.
- **Density:** this is an investor document, not a SaaS product page. Numbers, footnotes
  and source labels are expected. Skeletons and placeholder blocks are not.

---

## 3. DESIGN SYSTEM — measured from the actual slide pixels

These values were sampled programmatically from the 15 PNGs. Use them as the palette.

```
--ink:        #14261C   primary text, near-black green
--green:      #36761D   BRAND GREEN — headings, key figures, section titles
--green-deep: #395F4F   deep slate-green — dark banner backgrounds
--green-mid:  #2F6B45   darker accent for emphasis bars
--lime:       #8FD331   bright accent — spot highlights, zone fills on plans
--mint:       #ECFDF5   pale mint — card fills, alternating section backgrounds
--mint-2:     #D9EAD3   pale sage — second-level fills, map land
--lime-pale:  #DCF8C4   pale lime — zone fills
--sky:        #90CAF5   sky blue — gradient top, links on dark
--sky-pale:   #C4E9FA   pale cyan — chip fills, connectors
--cyan:       #19DAEC   ACCENT CYAN — arrows, callouts, one chart series
--yellow:     #FFE59A   yellow highlight block
--yellow-lt:  #FEF2CB   pale yellow — the discount slide's full-bleed ground
--gold:       #FED966   gold — bar series, price markers
--peach:      #FCE5CD   soft peach — secondary highlight
--cream:      #E8E1D4   cream — map ground, card accents
--grey-bg:    #EEEEEE   slide ground on most slides
--grey-line:  #CBD5CC   hairline borders
--red:        #C62828   deadlines, warnings, the 127-FZ block
```

**Type.** One geometric/neutral sans for everything: `Manrope, "Segoe UI", system-ui,
-apple-system, sans-serif`. Headings tight-tracked (`letter-spacing:-.02em`), weight
700–800. Body 16–17 px, line-height 1.55, colour `--ink`. Every number uses
`font-variant-numeric: tabular-nums` so columns align. Footnotes 13–14 px, colour
`#6B7A72`. Never below 13 px.

**Geometry.** The deck's signature is large soft radii. Measured corner radius on the
deck's card system is ≈24 px at 1686 px slide width → use **24 px** on cards and media
frames, 16 px on chips, 999 px on pills. Borders are 1 px, tinted `--grey-line`. Shadows
are extremely soft: `0 1px 2px rgba(20,38,28,.05), 0 8px 24px rgba(20,38,28,.05)`.

**Backgrounds.** Sections alternate between `--grey-bg`, `--mint` and white. Section
transitions are soft, never hard rules. Gradients run sky → mint → white.

**Graphic language.** The deck uses flat blocks, generous negative space, a strong yellow
"finding" block and a strong cyan "upside" block. Reproduce that hierarchy.

**Explicitly avoid:** glassmorphism, neon gradients, violet/indigo accents, emoji,
icon-above-heading tiles, centred-everything layouts, oversized numbers with no context,
drop shadows on text, dark-mode auto-inversion.

---

## 4. PAGE ARCHITECTURE

Eleven blocks, in this order. Every section gets an `id` for the nav.

| # | Section | `id` | Purpose |
|---|---|---|---|
| 0 | Sticky top bar | — | Wordmark, nav, one persistent CTA |
| 1 | Hero | `hero` | The one persuasion moment |
| 2 | Executive summary | `summary` | Four reasons, four proofs |
| 3 | Financial passport | `economics` | The section that must convince |
| 4 | The discount | `discount` | Waterfall + per-sqm table |
| 5 | The asset, floor by floor | `asset` | Vector plans + specs |
| 6 | Location & regional tailwinds | `location` | Schematic map + drivers |
| 7 | Engineering & autonomy | `engineering` | One-line schematic diagram |
| 8 | Land & warehouse | `land` | Parcel schematic + monetisation |
| 9 | Upside levers | `upside` | Cyan flow diagram |
| 10 | Process, legal, tax | `process` | The trust section |
| 11 | **Contact footer** | `contact` | **Owner placeholders — see §10** |

---

## 5. CONTENT — VERIFIED FIGURES AND COPY

**Every number below was recomputed from the memorandum and the 2025 appraisal. Use them
exactly. Where the deck prints a different (wrong) number, this list wins.**

### 5.1 Asset and deal

| Item | Figure |
|---|---|
| Shopping centre "Arbuz" | 4 floors, 11,520 sqm |
| Capital warehouse | 1 floor, 1,500 sqm |
| **Total built area** | **13,020 sqm** |
| Land, freehold, 3 parcels | 15,812 sqm (1.58 ha) — 8,503 / 4,500 / 2,809 sqm |
| Price (auction threshold) | **RUB 368,376,909** (≈ USD 4.50 M at 81.7947 USD/RUB, Bank of Russia, 06.11.2026) |
| 2015 construction cost | RUB 900,000,000+ |
| 2025 independent appraisal | RUB 528,971,000 (RUB 40,628 / sqm of built area) |
| Saving vs. appraisal | RUB 160,594,091 — **30.4%** |
| Price vs. build cost | RUB 531,623,091 — **59.1% below** (i.e. **40.9% of** the 2015 cost; 2.44× cheaper than building) |
| Application deadline (public auction, 127-FZ) | **25 November 2026** |
| Price per sqm of built area | RUB 28,293 / sqm |
| Price per sqm incl. land | RUB 12,777 / sqm |
| Gross revenue (base) | RUB 70,800,000 / yr (5.9 M / month) |
| Gross revenue (memo's optimisation case) | RUB 75,600,000 / yr (+6.8%) |
| NOI (base) | RUB 23,080,800 / yr (1.92 M / month) |
| NOI (memo's optimisation case) | RUB 27,492,000 / yr (2.29 M / month) — +19.1% NOI |
| NOI margin | 33% base → 36% in the memo's case → 55–65% district-mall norm |
| Cap rate | 6.27% base → 7.46% in the memo's case |
| Gross yield | 19.22% |
| Operating expenses | RUB 47,719,200 / yr = **67.4% of gross revenue** |
| Payback | 15.96 yrs base → 13.4 yrs optimised |
| GRM | 5.20 base → 4.87 optimised |
| Occupancy | 95.5% (4.5% vacancy) |
| Rent per sqm per month | RUB 453 gross · RUB 148 NOI |

### 5.2 Tenant mix (use these names only)

Over 70% of income from federal and regional chains: **Samburi** (regional supermarket,
anchor, 1,900 sqm), **KARI**, **OZON**, **MTS**, **MegaFon**, **Tele2**, **Sberbank**,
**VTB**. Floor 1 also carries a jewellery store "Zolotaya Rus" and a pharmacy.

### 5.3 Technical

Seismic rating 9 (Dalgiprotrans project, rock foundation). Dedicated 10 kV line, own
substation, 300 kW diesel generator with automatic start, own heating point with
metering, 4 lifts + escalators + goods lifts, tufoblok walls, multi-zone ventilation
with heat recovery. **No capital expenditure required for the next 15 years.**

### 5.4 Location

Sovetskaya Gavan is the eastern terminus of the Baikal-Amur Mainline, an operating point
on the Northern Sea Route, 10 km from the deep-water port of Vanino. Catchment: Sovetskaya
Gavan city 23,232 + Vaninsky District 33,201 = **56,433**; Sovetsko-Gavansky District
total 35,915. It is the only large shopping centre serving the two districts.

**TGMK — state it exactly this way, never "opens in 2027":**
*"Polymetal has returned to pre-feasibility work on the Pacific Hydro-Metallurgical
Complex (TGMK) in Sovetskaya Gavan after the project was paused in 2022. In June 2026 the
company, the Khabarovsk regional government and Rosvodokanal signed a three-party
agreement covering modern wastewater treatment (3,500 m³/day, first phase targeted 2031).
Planned capacity 250–300 kt of third-party gold concentrate per year, previously
estimated at RUB 60 bn."* Label it **planned**.

---

## 6. VECTOR ART RECIPES — the diagrams, plans and schematics

This is the preferred treatment for the page's diagrams: redrawn inline SVG, so they
scale, print, stay crisp, and carry every area and label in English. A whole slide raster
may also be used where the deck's own annotated slide is the better answer (see R1).
Each recipe states the **semantics that must survive** (so the drawing is truthful to
the asset), the **suggested SVG construction**, and the **label/annotation** the drawing
must carry. Draw them as inline SVG so they scale, print, and stay crisp.

### V1 — Floor plan, ground floor  ·  *(preferred; whole slide 7 is an acceptable alternative)*
*Semantics:* gallery ~2,900 sqm; anchor tenant **Samburi 1,900 sqm**; telecom salons
(MTS, MegaFon, Tele2); OZON; jewellery "Zolotaya Rus"; pharmacy; food court.
*Construction:* outer rounded rect (r=12, fill `#ECFDF5`, stroke `#36761D` 2px);
anchor zone as a large `--lime-pale` rect labelled `SAMBURI · 1 900 sqm`; gallery as a
`--sky-pale` band labelled `GALLERY ~2 900 sqm`; a row of small `--yellow` cells for
retail units each labelled with its tenant; dashed `--green` line for the escalator/lift
core labelled `VERTICAL CORE`; north arrow.
*Rules:* every zone labelled with its area or tenant; no invented areas; the plan is
schematic and must say so — caption under the figure: *"Schematic zoning diagram, not to
scale. Areas per the investment memorandum."*

### V2 — Floor plan, second floor  ·  *(preferred; whole slide 8 is an acceptable alternative)*
*Semantics:* fashion retail, a cinema/family-entertainment unit, jewellery and home-goods
group, open-plan floor with an open gallery loop, escalators and public WCs, goods lifts.
*Construction:* same frame language as V1; `--mint-2` gallery loop; `--yellow` retail
cells; `--cyan` entertainment unit; annotate `OPEN SPACE`, `ESCALATORS`, `GOODS LIFTS`.

### V3 — Floors 3–4 plan  ·  *(preferred; whole slide 9 is an acceptable alternative)*
*Semantics:* floor 3 — retail and café, **KARI 557.2 sqm**; floor 4 — offices **1,899 sqm**,
banquet hall, "Kafe Manna" with kitchen and open terrace.
*Construction:* two stacked plan frames side by side, labelled `LEVEL 3` / `LEVEL 4`;
`--lime-pale` for retail cells, `--peach` for café/food, `--sky-pale` for office block,
`--mint` for the banquet hall; a terrace strip as a dashed hatched band at the edge
labelled `OPEN TERRACE`.

### V4 — Site / parcel plan  ·  *(preferred; whole slide 11 is an acceptable alternative)*
*Semantics:* three freehold parcels on the red line — 8,503 sqm (mall zone + front
parking), 4,500 sqm (warehouse plot), 2,809 sqm (street frontage) = 15,812 sqm = 1.58 ha.
*Construction:* cream `#E8E1D4` ground; three adjacent polygons with white fill and 2px
`--green` stroke, each labelled with its area; the mall footprint and warehouse
footprint drawn as `--grey-bg` blocks with `--green` outline; a **dashed `--red` line**
labelled `RED LINE (красная линия)` running along one edge; a north arrow and a scale bar
reading `0 — 50 m`; a labelled dashed `STREET FRONTAGE` band on the 2,809 sqm parcel.
*Caption:* *"Schematic parcel diagram. Parcel areas per the memorandum: 8 503 + 4 500 +
2 809 = 15 812 sqm (1.58 ha)."*

### V5 — Regional map  ·  *(preferred; whole slides 2 and 6 are acceptable alternatives)*
*Semantics:* Sovetskaya Gavan as the eastern terminus of the BAM; Trans-Sib connection;
Vanino deep-water port 10 km away; the Northern Sea Route running north; the city as the
serving point for two districts.
*Construction:* pale-blue `--sky-pale` sea field on the right, cream land on the left;
a bold 4px `--green` line running west→east labelled `BAIKAL–AMUR MAINLINE` terminating
in a filled green dot labelled `SOVETSKAYA GAVAN`; a thinner `--gold` line branching
north-east to a port marker labelled `VANINO DEEP-WATER PORT · 10 km`; a dashed `--cyan`
arrow running north from the city labelled `NORTHERN SEA ROUTE`; a small annotation
`TERMINUS OF THE BAM`; a callout box `ONLY LARGE SHOPPING CENTRE SERVING THE TWO
DISTRICTS · 56 433 people`.
*Rules:* no real coastline, no place names other than the ones above, no raster basemap.

### V6 — Facade elevation  ·  *(preferred; whole slides 1 and 15 are acceptable alternatives)*
*Semantics:* a 4-storey mall block on the red line, with the anchor supermarket's
double-height glazed entrance at ground level and a green/yellow panel band.
*Construction:* an abstract elevation — four stacked rounded horizontal bands, each
labelled `LEVEL 4` … `LEVEL 1` on the left; the ground band in `--mint` with a wide
glazed shopfront grid in `--sky-pale`; upper bands as a regular window grid of small
`--white`/`--grey-bg` rectangles on a `--cream` facade; a `--green` cornice line at the
top; two `--yellow` panel accents; a low `--lime-pale` ground band labelled `PUBLIC
FRONTAGE / PARKING`; small cars as simple 22×10 px rounded rects in `--grey-line` for
scale.
*Label it honestly:* the caption reads *"Schematic elevation — illustrative, not an
architectural drawing."*

### V7 — Warehouse block  ·  *(preferred; whole slide 10 is an acceptable alternative)*
*Semantics:* one-storey capital warehouse 1,499.9 sqm on a 4,500 sqm plot, 6 m clear
height, heated, ventilated, sprinklered, multi-purpose.
*Construction:* a simple axonometric box (three parallelograms) in `--cream` and
`--grey-bg` with `--green` edges; a `--green` roof plane; three loading-dock rectangles
on the front face; a vertical dimension arrow labelled `6 m CLEAR HEIGHT`; a small
annotation block `HEATED · VENTILATED · SPRINKLERED · MULTI-PURPOSE`.

### V8 — Engineering one-line diagram  ·  *(preferred; whole slides 12 and 13 are acceptable alternatives)*
*Semantics:* own 10 kV line → own substation/transformer → switchboard → the building's
loads (lifts, escalators, ventilation with heat recovery, heating point, lighting);
a 300 kW diesel generator on automatic start as a **backup** supply, not a primary one;
seismic rating 9.
*Construction:* a left-to-right schematic — a `--green` pylon glyph → a transformer
square labelled `OWN SUBSTATION · 10 kV` → a vertical bus → three load branches, each a
rounded rect: `VENTILATION + HEAT RECOVERY`, `HEATING POINT · METERED`, `4 LIFTS +
ESCALATORS`; a generator glyph in `--gold` below, connected to the bus with a **dashed**
`--gold` line labelled `300 kW DIESEL · AUTOMATIC START` and the word `RESERVE` on the
connection; a `--cyan` loop arrow between the ventilation branch and itself labelled `HEAT
RECOVERY`; a badge in the corner: `SEISMIC 9 · DALTGIPROTRANS · ROCK FOUNDATION`.
*This diagram is the section's hero visual — draw it carefully. If you prefer to embed
the deck's own slides 12 and 13 instead, use them whole, uncropped.*

### V9 — Upside flow diagram  ·  *(preferred; whole slide 14 is an acceptable alternative)*
*Semantics:* five owner-side levers feeding one outcome.
*Construction:* a `--cyan` ground (the deck's cyan slide, used here as the accent field for
this section only) with five `--mint` rounded cards connected by `--cyan`/white arrows
into a single outcome node: `NOI 23.1 → 27.5 M RUB/yr`, `CAP 6.27% → 7.46%`.


---

## 7. THE 3D WATERMELON — scroll-driven ornament

*(This is §7 of the prompt — the document's sections. The eleven sections of the **page**
itself are listed in §4 and written in §9; they are a different numbering.)*

**What it is.** A photorealistic 3D watermelon that floats in a **reserved gutter on the
right edge** of the page. It drifts smoothly while the user scrolls, rolls gently as it
goes, and **parks itself at a fixed resting position the moment scrolling stops** — so it
never sits on top of the text. It is the brand mascot of the asset ("Арбуz" = the
mall's own name), rendered live, not a picture.

**What it must never do.** Cover text. Not at rest, not mid-scroll, not on any viewport
width. This is the hard requirement and it is checked explicitly below.

### 7.1 Layout contract — the gutter is reserved, not measured

The page reserves a fixed gutter on the right; the melon lives inside it and nothing else
ever may.

```css
:root{ --rail: clamp(130px, 13vw, 200px); }   /* the melon gutter   */
.page{ padding-right: calc(var(--gutter) + var(--rail)); max-width:1120px; margin:0 auto; }
```

- The gutter is **reserved via the page's `padding-right`** — this is what guarantees the
  content column can never reach the melon. Do not measure free space and place the melon
  in whatever is left over; leftover space changes with every section.
- A section that must span the full width (the per-sqm table in §4 of the page) breaks
  out of the gutter deliberately:
  ```css
  .bleed{ margin-right: calc(-1 * var(--rail)); padding-right: var(--gutter); }
  ```
  Such a section is the one case where content *can* enter the gutter — which is exactly
  why the runtime guard below exists.
- Below 900 px the melon is switched off entirely (`display:none`). It is decoration; on a
  phone the screen belongs to the numbers.

### 7.2 The guard — hide the melon if it would cover text

The guard is the part that makes the requirement true. It runs **every frame** and is
band-local: it only cares about the melon's *current vertical band*.

1. On scroll (throttled to ~220 ms) and on resize, cache every text block's geometry:
   `p, h1..h5, li, td, th, dd, dt, blockquote, .card, figcaption, label`. Store
   `left, right` and `top/bottom + scrollY` (document coordinates).
2. Each frame, compute the melon's viewport rect and test it against the cached blocks:
   - if a block's vertical span overlaps the melon's band **and** its horizontal span
     overlaps the melon's rect → the melon is **hidden** (`opacity:0; visibility:hidden`)
     for that band;
   - otherwise it is shown.
3. While hidden, **skip the render call entirely** — there is no point drawing a melon
   nobody can see.

```js
function bandBlocked(mRect){
  var sy = window.scrollY;
  for (var i = 0; i < textBlocks.length; i++){
    var b = textBlocks[i];
    var vt = b.top - sy, vb = b.bottom - sy;
    if (vb <= mRect.top || vt >= mRect.bottom) continue;    // no vertical overlap
    if (b.right > mRect.left && b.left < mRect.right) return true;
  }
  return false;
}
```

Cache the blocks in **document coordinates** (`+ window.scrollY`), not viewport
coordinates — otherwise the guard compares against stale positions while scrolling.

### 7.3 Motion — drift on scroll, park on stop

Two states, switched by an idle timer:

- **Scrolling** (`idleSince` older than 260 ms → moving): the melon travels the full
  height of the viewport in step with scroll progress, entering from below and exiting
  above. It also **rolls faster** — the spin rate is driven by scroll velocity, so it
  visibly accelerates while you scroll and slows when you stop.
- **Stopped** (idle): the melon **parks** at one of four fixed slots —
  `SLOT = [0.16, 0.40, 0.64, 0.85]` of the viewport height. The slot is chosen by scroll
  progress, so as you move down the page the melon settles in a *different* place each
  time and never sits still in one place. This is the "rests in a clear spot" behaviour:
  it is always between text blocks when it stops.

```js
var SLOT = [0.16, 0.40, 0.64, 0.85];
// moving:  targetY = -D*0.2 + prog*(vh + D*0.2);
// parked:  targetY = vh*SLOT[Math.round(prog*(SLOT.length-1))] - D/2;
y += (targetY - y) * 0.10;                    // eased, never snapping
stage.style.transform = 'translate3d(0,' + y.toFixed(1) + 'px,0)';
```

Scroll position itself is also smoothed (`scrollCurrent += (scrollTarget - scrollCurrent)
* 0.12`) so the melon glides instead of jittering with the scroll wheel.

### 7.4 The melon itself — photoreal, drawn per pixel

The melon is rendered **per-pixel on a `<canvas>`**, not with CSS gradients and not with
an image. Each pixel is shaded as a point on a sphere:

- **Silhouette:** a pixel is inside the fruit when `(x-CX)² + (y-CY)² ≤ R²`; outside it
  is fully transparent.
- **Stripes:** the stripes radiate from the poles, so they are computed from the
  **longitude** `atan2(z, x)` — not from the screen x. Rotate the sphere by the current
  spin angle around Y and tilt it around X, then take the longitude of the rotated point.
  Use 13 bands, make the dark stripes narrow (`pow(tri, 3.0)`), and wobble each band with
  a couple of sine terms plus a per-band random jitter so no two are identical.
- **Light:** one key light from the upper-left-front and one **fill light** from the
  lower-right — without the fill the shadow side goes black and the fruit reads as flat.
  Use a *wrapped* diffuse term `(ndl + 0.28) / 1.28` for a soft terminator.
- **Finish:** a broad waxy specular (`pow(sd,16)`), a tight highlight (`pow(sd,54)`), a
  Fresnel rim at the silhouette, and gentle occlusion under the belly.
- **Micro-relief:** perturb the normal slightly with two sine waves so the rind is not
  perfectly smooth, then renormalise.
- **Details:** a dried **curly stem** drawn on the canvas above the top pole (a stalk plus
  a bezier tendril, olive-brown), and a pale **blossom scar** disc at the bottom pole.
- The canvas is sized to `min(rail) - 12 px` at `devicePixelRatio` (capped at 2), and the
  sphere is placed at `R = D*0.375`, `CY = D*0.575` to leave headroom for the stem.

### 7.5 The code

Paste this as-is. It is the verified implementation.

**CSS** (add to the existing `<style>`; merge the `--rail` custom property into `:root`):

```css
  .wm{position:fixed;right:0;top:0;width:var(--rail);height:100vh;
      pointer-events:none;z-index:40;display:flex;align-items:center;justify-content:center;
      overflow:visible}
  .wm__stage{position:relative;width:100%;max-width:calc(var(--rail) - 12px);
             aspect-ratio:1/1;transform-style:preserve-3d}
  .wm__canvas{width:100%;height:100%;display:block;
              filter:drop-shadow(0 18px 26px rgba(8,32,14,.30))}
  .wm__shadow{position:absolute;left:50%;bottom:-7%;width:72%;height:9%;transform:translateX(-50%);
      background:radial-gradient(ellipse at 50% 50%, rgba(12,42,18,.42), rgba(12,42,18,0) 70%);
      filter:blur(5px)}
  @media (max-width:900px){ .wm{display:none} }
  @media (prefers-reduced-motion:reduce){ .wm__canvas{filter:none} }
  @media print{ .wm{display:none} }
```

**HTML** (add once, before the page content):

```html
<div class="wm" id="wm" aria-hidden="true">
  <div class="wm__stage" id="stage">
    <canvas class="wm__canvas" id="cv"></canvas>
    <div class="wm__shadow"></div>
  </div>
</div>
```

**JavaScript** (add before `</body>`; it needs `.page` to be the content wrapper and
`#wm`, `#stage`, `#cv` to exist):

```js
(function(){
  "use strict";
  var cv   = document.getElementById('cv');
  var ctx  = cv.getContext('2d');
  var wm   = document.getElementById('wm');
  var stage= document.getElementById('stage');
  var D = 190, img = null, buf = null;
  var R = 1, CX = 1, CY = 1;
  var ang = 0, spin = 0.5, tilt = 0.20;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function sizeCanvas(){
    var rect = stage.getBoundingClientRect();
    var css = Math.max(80, Math.min(rect.width, rect.height) - 16);
    var dpr = Math.min(2, window.devicePixelRatio || 1);
    cv.width = Math.round(css*dpr); cv.height = Math.round(css*dpr);
    D = cv.width; img = ctx.createImageData(D,D); buf = new Uint32Array(img.data.buffer);
    cv.style.width = css+'px'; cv.style.height = css+'px';
    R = D*0.375; CX = D/2; CY = D*0.575;      // sphere, with headroom above for the stem
    render();
  }

  function hash(n){ var s = Math.sin(n)*43758.5453; return s - Math.floor(s); }

  function render(){
    var i = 0;
    // key light: upper-left-front
    var lx=-0.46, ly=-0.60, lz=0.66;
    var ln=Math.sqrt(lx*lx+ly*ly+lz*lz); lx/=ln; ly/=ln; lz/=ln;
    // fill light: lower-right-front (bounce), keeps the dark side readable
    var fx=0.52, fy=0.18, fz=0.83;
    var fn=Math.sqrt(fx*fx+fy*fy+fz*fz); fx/=fn; fy/=fn; fz/=fn;
    var ct=Math.cos(tilt), st=Math.sin(tilt);
    var ca=Math.cos(ang), sa=Math.sin(ang);
    var hx=lx, hy=ly, hz=lz+1, hn=Math.sqrt(hx*hx+hy*hy+hz*hz); hx/=hn; hy/=hn; hz/=hn;
    var BANDS = 13.0;
    for (var y=0; y<D; y++){
      var ny=(y-CY)/R;
      for (var x=0; x<D; x++){
        var nx=(x-CX)/R;
        var d2=nx*nx+ny*ny;
        if (d2>1){ buf[i++]=0; continue; }
        var nz=Math.sqrt(1-d2);
        var ry=ny*ct-nz*st, rz=ny*st+nz*ct;
        var rx=nx*ca+rz*sa, rzz=-nx*sa+rz*ca;
        // micro-relief so the rind is not perfectly smooth
        var bump=0.030*Math.sin(nx*21.0+ny*13.0+ang*0.7)+0.022*Math.sin(nx*37.0-ny*29.0);
        rx+=bump; ry+=bump*0.6; rzz+=bump*0.4;
        var nl=Math.sqrt(rx*rx+ry*ry+rzz*rzz); rx/=nl; ry/=nl; rzz/=nl;
        // ---- stripe pattern (longitude), irregular like a real melon ----
        var lon=Math.atan2(rzz,rx);
        var wobble = 0.14*Math.sin(lon*3.0+0.7) + 0.08*Math.sin(lon*7.0+2.1);
        var s=(lon/(Math.PI*2)+0.5)*BANDS + wobble*BANDS*0.12;
        var f=s-Math.floor(s);
        var tri=Math.abs(f-0.5)*2;                     // 0 centre of band, 1 at edge
        var dark=Math.pow(tri, 3.0);                   // narrow dark stripes
        var jitter=hash(Math.floor(s)*37.0)*0.30;
        dark=Math.max(0,Math.min(1,dark+jitter*tri));
        var baseR=88-58*dark, baseG=176-104*dark, baseB=74-42*dark;
        var mott=0.93+0.14*hash(Math.floor(s*2.0)*91.0+Math.floor(ny*16.0)*13.0);
        baseR*=mott; baseG*=mott; baseB*=mott;
        var lat=Math.abs(ry);
        var pole=1-0.18*Math.pow(lat,3.0);
        baseR*=pole; baseG*=pole*1.02; baseB*=pole*0.94;
        // ---- lighting: wrapped diffuse key + fill + ambient ----
        var ndl=rx*lx+ry*ly+rzz*lz;
        var diff=Math.max(0,(ndl+0.28)/1.28);
        var ndf=rx*fx+ry*fy+rzz*fz;
        var fill=Math.max(0,(ndf+0.45)/1.45);
        var k=0.40+0.62*Math.pow(diff,0.90)+0.20*Math.pow(fill,1.5);
        var rr=baseR*k, gg=baseG*k, bb=baseB*k;
        // waxy broad specular
        var sd=Math.max(0, rx*hx+ry*hy+rzz*hz);
        var bw=Math.pow(sd,16);
        rr+=bw*46; gg+=bw*52; bb+=bw*44;
        // tight highlight
        var spec=Math.pow(sd,54)*225;
        rr+=spec; gg+=spec; bb+=spec;
        // fresnel rim (cool green bounce at the silhouette)
        var fres=Math.pow(1-Math.max(0,nz),3.0)*46;
        rr+=fres*0.55; gg+=fres*0.95; bb+=fres*0.68;
        // gentle occlusion under the belly
        var ao=1-0.18*Math.max(0,ny);
        rr*=ao; gg*=ao; bb*=ao;
        // blossom scar: pale cream disc at the bottom pole
        if (ry > 0.78){
          var scar=Math.min(1,(ry-0.78)/0.16);
          var sk=scar*scar*scar;
          rr=rr*(1-sk)+228*sk; gg=gg*(1-sk)+221*sk; bb=bb*(1-sk)+170*sk;
        }
        buf[i++]=(255<<24)|(Math.min(255,bb|0)<<16)|(Math.min(255,gg|0)<<8)|Math.min(255,rr|0);
      }
    }
    ctx.putImageData(img,0,0);
    drawStem();
  }

  // dried curly stem rising from the top pole
  function drawStem(){
    var top = CY - R, cx = CX;
    ctx.save();
    ctx.lineCap='round'; ctx.lineJoin='round';
    ctx.globalAlpha=0.28; ctx.fillStyle='#132a10';
    ctx.beginPath(); ctx.ellipse(cx, top+R*0.02, R*0.11, R*0.05, 0, 0, Math.PI*2); ctx.fill();
    ctx.globalAlpha=1;
    ctx.strokeStyle='#4b5a2a'; ctx.lineWidth=Math.max(2, R*0.045);
    ctx.beginPath();
    ctx.moveTo(cx, top+R*0.03);
    ctx.quadraticCurveTo(cx+R*0.05, top-R*0.10, cx+R*0.13, top-R*0.20);
    ctx.stroke();
    ctx.strokeStyle='#6d7738'; ctx.lineWidth=Math.max(1.4, R*0.026);
    ctx.beginPath();
    ctx.moveTo(cx+R*0.13, top-R*0.20);
    ctx.bezierCurveTo(cx+R*0.30, top-R*0.30, cx+R*0.22, top-R*0.44, cx+R*0.09, top-R*0.38);
    ctx.bezierCurveTo(cx+R*0.03, top-R*0.34, cx+R*0.11, top-R*0.27, cx+R*0.18, top-R*0.30);
    ctx.stroke();
    ctx.restore();
  }

  // ---------- layout guard -------------------------------------------------
  // The rail is reserved by the page's padding, so normal content can never
  // reach it. A full-bleed section (the per-sqm table) can. The guard therefore
  // checks the melon's CURRENT vertical band against real text blocks: if any
  // text would be covered, the melon is hidden for that band only.
  var railTimer = 0, textBlocks = [];
  var TEXT_SEL = 'p,h1,h2,h3,h4,h5,li,td,th,dd,dt,blockquote,.card,figcaption,label';
  function updateRail(){
    // the gutter width is a CSS constant (--rail) — nothing to measure here
    sizeCanvas();
  }
  // cache the text blocks once: their horizontal edge is stable while scrolling
  function refreshText(){
    textBlocks = [];
    var els = document.querySelectorAll(TEXT_SEL);
    for (var i = 0; i < els.length; i++){
      var el = els[i];
      if (!el.offsetWidth && !el.offsetHeight) continue;
      var r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      textBlocks.push({
        right: r.right,
        left: r.left,
        top: r.top + window.scrollY,
        bottom: r.bottom + window.scrollY
      });
    }
  }
  // does anything overlap the melon's current band?
  function bandBlocked(mRect){
    var sy = window.scrollY;
    for (var i = 0; i < textBlocks.length; i++){
      var b = textBlocks[i];
      var vt = b.top - sy, vb = b.bottom - sy;
      if (vb <= mRect.top || vt >= mRect.bottom) continue;   // no vertical overlap
      if (b.right > mRect.left && b.left < mRect.right) return true;
    }
    return false;
  }

  // ---------- scroll motion ----------
  var scrollTarget=0, scrollCurrent=0, lastScroll=0, vel=0;
  var y=0, idleSince=performance.now(), targetY=0;
  var SLOT=[0.16,0.40,0.64,0.85];

  function onScroll(){
    scrollTarget = window.scrollY || window.pageYOffset;
    var d = scrollTarget - lastScroll;
    lastScroll = scrollTarget;
    vel = vel*0.7 + d*0.3;
    if (Math.abs(d) > 0.5) idleSince = performance.now();
  }

  window.addEventListener('scroll', function(){
    onScroll();
    var now = performance.now();
    if (now - railTimer > 220){ railTimer = now; updateRail(); refreshText(); }
  }, {passive:true});
  window.addEventListener('resize', function(){ updateRail(); refreshText(); onScroll(); });

  function tick(now){
    scrollCurrent += (scrollTarget - scrollCurrent) * 0.12;
    var vh = window.innerHeight, vw = window.innerWidth;
    var max = Math.max(1, document.documentElement.scrollHeight - vh);
    var prog = Math.min(1, Math.max(0, scrollCurrent / max));
    var idle = (now - idleSince) > 260;

    if (reduced){
      // static: parked mid-right, no spin, no travel
      spin = 0;
      targetY = vh*0.5 - D/2;
    } else {
      spin = idle ? 0.32 : 0.32 + Math.min(7, Math.abs(vel)*0.05);
      ang += spin * 0.016;
      if (idle) targetY = vh*SLOT[Math.round(prog*(SLOT.length-1))] - D/2;
      else     targetY = -D*0.2 + prog*(vh + D*0.2);
    }
    y += (targetY - y) * 0.10;
    stage.style.transform = 'translate3d(0,' + y.toFixed(1) + 'px,0)';

    // hard safety: hide the melon whenever it would cover any text
    var mRect = stage.getBoundingClientRect();
    var fits = !bandBlocked(mRect);
    wm.style.opacity = fits ? '1' : '0';
    wm.style.visibility = fits ? 'visible' : 'hidden';
    if (!fits) return requestAnimationFrame(tick);   // no point rendering a hidden melon

    render();
    requestAnimationFrame(tick);
  }

  updateRail();
  refreshText();
  sizeCanvas();
  scrollTarget = scrollCurrent = window.scrollY || 0;
  idleSince = performance.now();
  requestAnimationFrame(tick);
})();
```

**The `aria-hidden="true"` on the wrapper is required** — the melon is decorative and
must not be announced by a screen reader.

### 7.6 Performance, accessibility and print

- Cap the canvas at `devicePixelRatio` 2 and the fruit at 200 px — the melon is ~200×200
  device pixels, which is cheap. Do not add a second canvas, a second layer, or a blur
  filter on the fruit itself.
- **The drop shadow must be CSS**, not a canvas blur: `filter: drop-shadow(...)` on the
  canvas plus a radial-gradient ellipse under it. Blurring the canvas every frame is
  what will drop the frame rate.
- `prefers-reduced-motion: reduce` → **stop the spin and the travel entirely**. Park the
  melon at mid-height and leave it there. Do not merely slow it down.
- `@media print` → hide the melon completely; it has no meaning on paper.
- Hide it below 900 px.

### 7.7 Acceptance criteria for the melon

- [ ] The melon never overlaps a single text element, in **any** of: the moving state,
      the parked state, and after a hard jump to an arbitrary scroll position.
- [ ] **Verify it, do not eyeball it.** Add this temporary hook to the page, run it, then
      remove it before delivery:

      ```js
      window.__wmTest = async function () {
        var vh = window.innerHeight, vw = window.innerWidth;
        var max = Math.max(1, document.documentElement.scrollHeight - vh);
        var violations = [], hidden = 0, shown = 0;
        var sels = 'p,h1,h2,h3,li,td,th,.card';
        function check(sy) {
          var m = document.getElementById('stage').getBoundingClientRect();
          var hid = getComputedStyle(document.getElementById('wm')).visibility === 'hidden';
          var els = document.querySelectorAll(sels), out = [];
          for (var i = 0; i < els.length; i++) {
            var t = els[i].getBoundingClientRect();
            if (!t.width && !t.height) continue;
            if (t.bottom < 0 || t.top > vh) continue;
            if (hid) continue;
            var ix = Math.min(m.right, t.right) - Math.max(m.left, t.left);
            var iy = Math.min(m.bottom, t.bottom) - Math.max(m.top, t.top);
            if (ix > 1 && iy > 1) out.push({ scroll: sy, tag: els[i].tagName,
              text: (els[i].textContent || '').trim().slice(0, 40),
              overlap: [Math.round(ix), Math.round(iy)] });
          }
          return { out: out, hid: hid };
        }
        for (var s = 0; s <= 24; s++) {
          var sy = Math.round(max * s / 24);
          window.scrollTo(0, sy); window.dispatchEvent(new Event('scroll'));
          await new Promise(function (r) { var c = 0; (function f() {
            if (c++ >= 3) return r(); requestAnimationFrame(f); })(); });
          var r1 = check(sy); violations = violations.concat(r1.out);
          if (r1.hid) hidden++; else shown++;
        }
        window.scrollTo(0, 0);
        return { violations: violations, hidden: hidden, shown: shown };
      };
      ```

      Then run `await window.__wmTest()` in the console at 375 / 768 / 1440 / 1920 px.
      **`violations` must be empty at every width.** Report the result in the changelog.
- [ ] The melon parks at a *different* height in different parts of the page (4 slots),
      and never rests over text.
- [ ] The melon is hidden on screens below 900 px and in print.
- [ ] `prefers-reduced-motion` stops the spin and the travel.
- [ ] The frame rate holds 60 fps while scrolling (check with the DevTools Performance
      panel). If it does not, the cause is almost always a `filter: blur()` on the canvas
      or a `getImageData`/`putImageData` call that runs more than once per frame.
- [ ] The melon is `aria-hidden` and has `pointer-events:none` — it must never swallow a
      click on a link or button behind it.

---

## 8. CHARTS AND DATA TABLES — all values pre-verified

Build every chart as **inline SVG**. No chart library — it would pull in a CDN dependency
and impose a generic dashboard look. Label every axis. Use `--gold` for historical/
benchmark bars, `--green` for the subject asset, `--cyan` for one highlighted series,
`--grey-line` for gridlines.

1. **Discount waterfall** (in §4 of the page): three horizontal bars —
   **900 M** (2015 construction cost, `--grey-line` fill, hatch) → **528.97 M** (2025
   independent appraisal, `--gold`) → **368.38 M** (auction price, `--green`, bold
   outline). Annotate each with its label and year. Callouts: *40.9% of 2015 build cost*,
   *30.4% below appraisal*, *RUB 160,594,091 saving*, *2.44× cheaper than building*.
   ⚠️ Do **not** print "69%" — the deck's "530 млн руб от себестоимости строительства
   (69%)" is arithmetically wrong. Correct value: **RUB 531,623,091 = 59.1% below cost**.
   Keep the two discounts as separate labelled statements, never merged into one phrase.

2. **Per-sqm comparison table** — full-width, not a card. Subject row highlighted in
   `--mint`.

   | Location / category | RUB per sqm | vs. this asset |
   |---|---|---|
   | Vladivostok, primary market | 189,000 | 6.7× higher |
   | Khabarovsk, prime offices | 125,000 | 4.4× higher |
   | Khabarovsk, commercial | 110,200 – 118,900 | 3.9–4.2× higher |
   | **Sovetskaya Gavan, this asset** | **28,293** | — |

   Footnote: *"Comparison based on total built area of the subject asset."*

3. **Financial passport — two scenario cards** side by side: "Base case — as currently
   operated" vs "Optimisation case — after repricing and filling the 4.5% vacancy",
   each with gross revenue, NOI, NOI margin, cap rate, payback, GRM.

4. **The margin-gap block** (yellow `--yellow` fill, the deck's "finding" block):
   *"Where the upside actually comes from."* Explain that 33% is far below the 55–65%
   district-mall norm; the memo's optimisation case captures only +6.8% of revenue, so the
   asset is *unmanaged, not weak*. State plainly: at current operating costs, a 55% margin
   requires RUB 106,042,667 of revenue — **+49.8%**. Add the quick check: filling the
   vacancy alone takes NOI to RUB 26,416,926 and the cap rate to 7.17%.

5. **Five-year operating path** — grouped bars + a cap-rate line on a secondary axis:
   - Years 1–5, revenue +10%/yr: 77.9 / 85.7 / 94.2 / 103.7 / 114.0 M RUB
   - NOI, opex flat: 30.2 / 37.9 / 46.5 / 55.9 / 66.3 M RUB → cap 8.2 / 10.3 / 12.6 /
     15.2 / 18.0%
   - NOI, opex +5%/yr: 27.8 / 33.1 / 39.0 / 45.7 / 53.1 M RUB → cap 7.5 / 9.0 / 10.6 /
     12.4 / 14.4%
   - Axes in RUB million; state the price denominator (RUB 368,376,909) in the caption.
   - Caption: *"Indexation of 10% p.a. reaches a market margin by year 4–5 if operating
     costs are held flat. With costs inflating at 5% p.a. the target margin is not reached
     within five years — cost discipline, not rent, drives the return."*

6. **Cap-rate screen table** — "the price you are paying vs. the price a screen implies".

   | Cap rate | Implied value at base NOI 23.08 M | At optimised NOI 27.49 M |
   |---|---|---|
   | 8% | 288,510,000 | 343,650,000 |
   | 9% | 256,453,333 | 305,466,667 |
   | 10% | 230,808,000 | 274,920,000 |
   | 12% | 192,340,000 | 229,100,000 |

7. **Rent economics strip** — RUB 453 / sqm / month gross, RUB 148 / sqm / month NOI,
   RUB 12,777 / sqm land-inclusive effective price.

---

## 9. SECTION-BY-SECTION COPY

Write in this voice: institutional, plain English, every bold claim backed by a number
that appears on the same screen.

### §0 — Top bar
Wordmark `ARBUZ · SOVETSKAYA GAVAN`. Nav anchors: Asset, Economics, Location, Upside,
Process. One persistent CTA: **Request data room**. 64 px tall, translucent white with a
hairline bottom border, becomes solid on scroll.

### §1 — Hero
Eyebrow: `PUBLIC AUCTION · FAR EASTERN DISTRICT · 127-FZ`.
Headline: **"A ready-made income-producing asset at 40.9% of its 2015 build cost."**
Sub-line: *"Shopping centre 'Arbuz' and a capital warehouse with 1.58 ha of freehold
land, on the red line in the logistics hub of Sovetskaya Gavan, Khabarovsk Krai."*
Lot-composition card: shopping centre 11,520 sqm / 4 floors · capital warehouse 1,500 sqm
· land 15,812 sqm (1.58 ha) in 3 parcels. Price line **RUB 368,376,909**, deadline in
`--red`: *"Applications until 25 November 2026"*.
Right column: **V6 facade elevation** in a rounded frame.
Below, a full-width strip of five metric tiles: 13,020 sqm total built area · RUB 28,293
per sqm · NOI from RUB 23.1 M / yr · Cap rate 6.27% · payback 13–16 yrs.
Honest note under the strip, 13px: *"Price per sqm is calculated on total built area, not
leasable area (GLA). See the Asset section."*

### §2 — Executive summary
Asymmetric: left = **V5 regional map**, right = heading **"Why this asset, why now"** and
four cards, each with a green heading, one supporting sentence, and one figure that proves
it: *Inflation hedge* (hard walls and land revalue with inflation; fixed deposit rates do
not) · *No systemic exposure* (rent flows in locally; no freeze risk, no deposit limits) ·
*Monopoly position* (the only large mall serving both districts — 56,433 people — 4.5%
vacancy) · *Basis discount* (30.4% below the 2025 independent appraisal, RUB 160.59 M
saving).

### §3 — Financial passport
Two scenario cards → the yellow margin-gap block → four KPI tiles (NOI target RUB 27.5 M ·
cap target 7.46% · GRM 4.9 · payback 13 yrs) → the five-year path chart.

### §4 — The discount
The waterfall, then the per-sqm table full width, then a one-line honest note: *"The 2015
construction cost is a benchmark for what this asset would cost to build today at 2015
prices; the 2025 appraisal is an independent market opinion. The 40.9% and 30.4% figures
are measured against different benchmarks and are not additive."*

### §5 — The asset, floor by floor
V1, V2, V3 plans with their short facts blocks:
- **Floor 1 — supermarket & services.** Gallery ~2,900 sqm. Anchor tenant: regional
  supermarket **Samburi, 1,900 sqm**. Telecom salons (MTS, MegaFon, Tele2), OZON,
  jewellery "Zolotaya Rus", pharmacy, food court.
- **Floor 2 — fashion retail & entertainment.** Open gallery loop, cinema/family unit,
  jewellery and home-goods group, escalators, goods lifts.
- **Floor 3 — retail & café.** KARI 557.2 sqm.
- **Floor 4 — offices & banquet.** Offices 1,899 sqm, banquet hall, "Kafe Manna" with
  open terrace.
- **Warehouse — 1,500 sqm.** 1,499.9 sqm on a 4,500 sqm plot, 6 m clear height, heated,
  sprinklered, one storey. Use: regional distribution hub for the two districts, or lease
  to a federal logistics operator or marketplace (Ozon, Wildberries).
- **Land — 1.58 ha freehold on the red line.** Three parcels 8,503 / 4,500 / 2,809 sqm.
- **Area check to display:** 8,503 + 4,500 + 2,809 = 15,812 sqm = 1.58 ha.
- **Footnote (required):** *"Documented leasable areas total ~5,356 sqm (floor 1 ~2,900;
  floor 3 557.2; floor 4 1,899; floor 2 not stated); the remainder is common areas. On GLA
  of ~5,400–7,000 sqm the effective price is RUB 52,000–68,000 / sqm. Anchor tenant
  Samburi is ~33% of GLA."*

### §6 — Location & regional tailwinds
V5 map. Bullets: only large mall serving the two districts · eastern terminus of the BAM ·
freight infrastructure linking to Komsomolsk-on-Amur and the rest of Russia · a modern CHP
plant serving the transport hub · port and logistics zone with new coal and container
terminals, ship-repair centres and fish-processing.
TGMK paragraph exactly as written in §5.4, labelled **planned**.
Population footnote: *"Sovetskaya Gavan city 23,232 + Vaninsky District 33,201 (2025)."*

### §7 — Engineering & operating autonomy
**V8 one-line diagram** as the hero. Facts list beside it: seismic 9 (Dalgiprotrans
project, rock foundation) · own 10 kV line · own substation · 300 kW diesel generator ·
4 lifts + escalators · tufoblok walls · ventilation with heat recovery · own heating point
and metering. Closing banner in `--yellow`: **"100% engineering autonomy — no capital
expenditure for 15 years."**

### §8 — Land & warehouse
**V4 parcel schematic** + V7 warehouse block. Monetisation list: build-materials store,
car dealership, car wash, drive-thru QSR or fuel station, paid parking, bus terminal, or
sell parcels to developers.

### §9 — Upside levers
**V9 flow diagram.** Five levers: (1) reserve for asset capitalisation — professional
management and merchandising; (2) lease optimisation — operating costs have never been
benchmarked; (3) rent indexation — leases have not been indexed, **15–20% revenue uplift
available** (present as an estimate, not a guarantee); (4) OPEX reduction — 67.4% of revenue
goes to operating costs; (5) warehouse development + land monetisation.
Honest note: *"All five levers are owner-side actions and require no capital from the
tenant base. The memo's optimisation case assumes only +6.8% revenue. The gap between that
and a 55% margin is where the asset's value is created."*

### §10 — Process, legal cleanliness, tax
Three green-bordered cards: (1) **Legal cleanliness guaranteed** — under Federal Law
No. 127-FZ on insolvency, the seller's tax debts, pledges, attachments and encumbrances
are extinguished on purchase and the price is protected from challenge; (2) **Purchase
procedure** — public auction, open bidding, at the threshold price; (3) **Applications
accepted until 25 November 2026** (red date).
Tax note, precisely: *"Sale of a bankrupt debtor's property is not subject to VAT
(Clause 15, Sub-clause 2, Article 146 of the Russian Tax Code). For a buyer with no right
to deduct input VAT this is worth 16.7% of the price (RUB 368,376,909 vs. RUB 442,052,291
with VAT)."* And: *"Free-port (SPV) and Advanced Development Territory (TOR) preferences —
zero property tax for 5 years, zero land tax for 5 years, reduced social contributions from
30% to 7.6% — require registration of the asset under a dedicated project, resident status,
and a tax opinion. They are a regime for a resident, not an automatic entitlement of the
buyer."*

### §11 — Contact footer + disclaimer
→ the exact block, placeholders and markup is specified in **§10 CONTACT FOOTER** below.

---

## 10. CONTACT FOOTER — owner placeholders (REQUIRED)

Close the page with a full-width contact block on a `--green-deep` (#395F4F) ground, white
type, and a thin `--cyan` rule above it. It must contain a **placeholder row for the
owner's details**, clearly marked so the owner can overwrite it without touching the
layout. Use these literal tokens **in the markup**, each with a visible sample value and
an HTML comment naming the field:

```
{{OWNER_NAME}}      — Owner / Company / Broker
{{OWNER_ROLE}}      — e.g. Head of Asset Management
{{TELEGRAM_HANDLE}} — e.g. @your_handle
{{WHATSAPP_NUMBER}} — e.g. +7 900 000-00-00
{{EMAIL_ADDRESS}}   — e.g. name@example.com
```

Layout and content requirements:

- **Heading:** *"Request the data room."* with the sub-line *"Rent roll, operating
  accounts, cadastral and engineering documentation and the 2025 appraisal report are
  available under NDA."*
- **Owner identity block:** the wordmark `ARBUZ · SOVETSKAYA GAVAN`, then
  `{{OWNER_NAME}}` and `{{OWNER_ROLE}}` on two lines.
- **Four contact items, each with a small hand-drawn inline-SVG glyph (16–20 px, currentColor
  stroke, no icon font, no emoji):**
  1. Telegram → `{{TELEGRAM_HANDLE}}`, rendered as a `https://t.me/{{TELEGRAM_HANDLE}}` link
     (href with the handle minus the `@`);
  2. WhatsApp → `{{WHATSAPP_NUMBER}}`, rendered as a `https://wa.me/<digits only>` link;
  3. Email → `{{EMAIL_ADDRESS}}`, rendered as a `mailto:` link;
  4. Address / location → the asset address line in plain text: *"Sovetskaya Gavan,
     Khabarovsk Krai, Russian Far East"* — this one is real, not a placeholder.
- **One primary CTA button** on the left of the block: *"Request the data room"* and a
  secondary ghost button: *"NDA and financial model on request"*. Both must be real
  `<a>` elements — wire the primary to a `mailto:` containing a pre-filled subject line
  (`Request for data room — Arbuz, Sovetskaya Gavan`) and a body containing the asset
  name and the auction date. Keep the placeholder tokens in the href so the owner updates
  one place.
- **Legal footer line below the block, 13px, muted:** *"This page summarises an investment
  memorandum prepared for a public auction. Figures are taken from the memorandum and the
  2025 independent appraisal; forward-looking statements are projections. This is not a
  public offer."*
- Keep the placeholders visually obvious in the delivered file (for example, the token
  text is what renders) so nobody ships placeholder contact details by accident — and
  list every placeholder in the changelog.

---

## 11. ACCEPTANCE CRITERIA

- [ ] Single self-contained `index.html`; opens from disk; **no console errors**; no
      network requests required to render.
- [ ] **No photo cropped out of a slide PNG.** Check every image on the page: it must be
      a whole slide raster, an original owner photograph, or vector art — never a cut-out
      taken from inside a slide. Verify by grepping the output for image references and
      confirming each one resolves to a full slide file, not a crop of one.
- [ ] All eleven sections present, in the order of §4, with the copy of §9 unless
      deliberately shortened — the copy *is* the persuasion.
- [ ] Every figure traceable to §5; zero invented numbers.
- [ ] All seven charts/tables of §8 rendered with the stated values and labelled axes.
- [ ] Vector art V1–V9 all present, each labelled schematic, each carrying its required
      annotations and areas — or, where a whole slide raster is used instead, that slide
      must carry the same information.
- [ ] Required footnotes present: price per sqm is built area not GLA · GLA caveat ·
      population components · TGMK status · VAT condition · TOR/SPV condition · USD rate
      and date.
- [ ] "69%" appears nowhere; "40.9% of build cost" and "30.4% below appraisal" appear as
      separate statements.
- [ ] The date is exactly **25 November 2026**, rendered in `--red`.
- [ ] Contact footer contains all five tokens (`{{OWNER_NAME}}`, `{{OWNER_ROLE}}`,
      `{{TELEGRAM_HANDLE}}`, `{{WHATSAPP_NUMBER}}`, `{{EMAIL_ADDRESS}}`), four working
      links, and the disclaimer.
- [ ] Responsive at 375 / 768 / 1440 / 1920; no horizontal scroll; tap targets ≥ 44px.
- [ ] `prefers-reduced-motion` respected; no layout shift on load.
- [ ] The 3D watermelon is present, photoreal, and passes the no-text-overlap proof in
      **§7.7** at every width — verified by running the test, not by looking at it.
- [ ] Print stylesheet produces a clean A4 memo (charts print, nav and buttons hidden).
- [ ] Copy passes the sceptical-analyst test: every bold claim has a number behind it and
      no number appears without its basis.

---

## 12. DELIVERY

Deliver:

1. `index.html` — self-contained CSS and JS. If you embed any slide PNG, either copy it
   into an `assets/` folder next to `index.html` and reference it relatively, or inline
   it as a base64 data-URI. The page must depend on nothing but its own files.
   The watermelon (§7 of this prompt) is drawn on a `<canvas>` at runtime — it is **not**
   a file and must not be added to `assets/`.
2. `README.md` — how to open it, how to fill in the five contact placeholders, and how to
   swap a placeholder frame for a real photo later without breaking the layout.
3. A two-line changelog: **what was built**, and **every place you deviated from this
   prompt and why**. If you deviated from a number or a rule, say so explicitly.

### A note on what to build first

If you want to sequence the work: build §1 hero + §3 economics + §4 discount + §11
contact first — they carry the argument — then §5–§9 (the diagrams, which is the labour),
then §2, §6, §10. Do not skip the diagrams: a plan drawn as a rectangle with no labels is
worth less to this audience than the honest sentence above it.