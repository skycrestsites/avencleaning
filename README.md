# Aven Cleaning Co. — Website

Static marketing site for **Aven Cleaning Co.**, a residential and commercial cleaning company serving Las Vegas, NV and surrounding areas.

- Owner: Kasey Rivera
- Email: info@avencleaningco.com
- Online booking: BookingKoala (embedded on `/book/`)

## Pages (clean URLs, no `.html`)

Every page lives in its own folder as `index.html`, so URLs have no file extension on any static host.

| URL | File |
| --- | --- |
| `/` | `index.html` |
| `/services/` | `services/index.html` |
| `/services/standard-cleaning/` | `services/standard-cleaning/index.html` |
| `/services/deep-cleaning/` | `services/deep-cleaning/index.html` |
| `/services/recurring-cleaning/` | `services/recurring-cleaning/index.html` |
| `/services/move-in-move-out-cleaning/` | `services/move-in-move-out-cleaning/index.html` |
| `/services/commercial-cleaning/` | `services/commercial-cleaning/index.html` |
| `/services/post-construction-cleaning/` | `services/post-construction-cleaning/index.html` |
| `/services/vacation-rental-cleaning/` | `services/vacation-rental-cleaning/index.html` |
| `/services/add-on-services/` | `services/add-on-services/index.html` |
| `/about/` | `about/index.html` |
| `/contact/` | `contact/index.html` |
| `/book/` | `book/index.html` |
| `/privacy-policy/`, `/terms/` | legal pages |
| `404.html` | custom not-found page (GitHub Pages / Netlify pick it up automatically) |

Also included: `sitemap.xml`, `robots.txt`, `site.webmanifest`, `favicon.ico` + PNG icons, `images/og-image.jpg` for social sharing.

## Deploying

The site is plain HTML/CSS/JS with no build step required. Push to GitHub and enable **GitHub Pages** (branch `main`, folder `/`), or drop the folder on Netlify / Vercel / Cloudflare Pages.

All internal links are relative, so the site works at the repo sub-path **and** on a custom domain.

### Domain

Canonical URLs, Open Graph tags, `sitemap.xml` and `robots.txt` assume **https://avencleaningco.com**. If the final domain is different, search and replace `https://avencleaningco.com` across the HTML files (or change `SITE_URL` in `_build/build.py` and rebuild). For GitHub Pages on a custom domain, add a `CNAME` file containing the domain.

## Booking embed (`/book/`)

The BookingKoala form is embedded as a plain `<iframe>` **without** BookingKoala's `embed.js` (iframe-resizer). The frame has a fixed, viewport-based height and `scrolling="yes"`, so:

- the form scrolls internally like a normal browser viewport (works natively on iOS),
- BookingKoala's modals appear inside the frame where the user is looking,
- nothing resizes the page or forces `scrolling="no"`.

A fallback link opens the booking form in a new tab if the frame fails to load.

## Editing

Two options:

1. **Edit the HTML directly.** Shared parts (header, footer, nav) are repeated in each file, so change them everywhere.
2. **Edit `_build/build.py` and rebuild** (`python _build/build.py`, requires Python 3 + Pillow). All copy, services, FAQs, reviews and service areas live in that one file. **Rebuilding overwrites every HTML page**, so do not mix the two approaches.

Styling uses Tailwind CSS via CDN with the brand palette (navy `#2f3b69`, gold `#c5a059`, cream `#fafaff`) and the fonts Playfair Display + Inter.

## Not deployed

`Stock images/`, `style 3/`, the questionnaire CSV and the original logo are source material and are excluded by `.gitignore`. Optimized copies of the images used on the site are in `images/`.
