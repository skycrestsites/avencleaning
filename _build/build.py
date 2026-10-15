# -*- coding: utf-8 -*-
"""Static site generator for Aven Cleaning Co.

Run from anywhere:  python _build/build.py
Regenerates every HTML page, sitemap.xml, robots.txt and site.webmanifest in the repo root.
WARNING: this overwrites hand edits made directly to the HTML files. Edit this file instead, then rebuild.
"""
import os, json, html
from string import Template
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root (this file lives in _build/)
SITE_URL = "https://avencleaningco.com"
BRAND = "Aven Cleaning Co."
EMAIL = "info@avencleaningco.com"
OWNER = "Kasey Rivera"
BOOK_URL = "https://avencleaningco.bookingkoala.com/booknow"
BOOK_EMBED = BOOK_URL + "?embed=true"
TODAY = "2026-10-07"
YEAR = "2026"

AREAS = ["Las Vegas", "Henderson", "North Las Vegas", "Summerlin", "Spring Valley", "Enterprise",
         "Paradise", "Green Valley", "Centennial Hills", "Southern Highlands", "Boulder City"]

_dims = {}
def dims(name):
    if name not in _dims:
        with Image.open(os.path.join(ROOT, "images", name)) as im:
            _dims[name] = im.size
    return _dims[name]

def img(name, alt, cls="", lazy=True, sizes=None):
    w, h = dims(name)
    return (f'<img src="$root$images/{name}" alt="{html.escape(alt)}" width="{w}" height="{h}" '
            f'class="{cls}" {"loading=\"lazy\"" if lazy else "fetchpriority=\"high\""} decoding="async">')

# --------------------------------------------------------------------------- services
SERVICES = [
    dict(
        slug="standard-cleaning", name="Standard Cleaning", short="Standard",
        icon="cleaning_services",
        card="Routine cleaning that keeps your home fresh and maintained: dusting, vacuuming, mopping, kitchen surfaces, bathrooms and general tidying.",
        hero="standard-cleaning.jpg",
        hero_alt="Bright, clean kitchen with a granite island after a standard cleaning",
        gallery=[("standard-cleaning-2.jpg", "Cleaner wiping down a white kitchen counter"),
                 ("standard-cleaning-3.jpg", "Mopping a hardwood floor"),
                 ("bright-kitchen.jpg", "Spotless modern kitchen with marble counters")],
        lead="A reliable, consistent clean for homes across Las Vegas and the surrounding valley. We take care of the routine so your home always feels fresh and ready for company.",
        overview=[
            "Our Standard Cleaning covers the rooms you live in every day. Kitchens, bathrooms, bedrooms and living areas are dusted, wiped, vacuumed and mopped by a background-checked cleaner who follows the same detailed checklist on every visit.",
            "It is the right fit for homes that are already in good shape and simply need regular upkeep. If it has been a while since your last professional clean, we recommend starting with a Deep Cleaning and then maintaining with Standard visits.",
        ],
        includes=["Dust all reachable surfaces, shelves and decor", "Wipe kitchen counters, backsplash and appliance exteriors",
                  "Clean and sanitize sinks, faucets and fixtures", "Scrub toilets, tubs and showers",
                  "Clean mirrors and glass surfaces", "Vacuum carpets, rugs and upholstery",
                  "Sweep and mop hard floors", "Make beds and tidy common areas",
                  "Empty trash and replace liners", "Spot clean doors, switches and handles"],
        benefits=[("schedule", "Flexible scheduling", "Book a single visit or set up a recurring plan that fits your calendar."),
                  ("checklist", "Consistent checklist", "Every visit follows the same room-by-room checklist, so nothing is missed."),
                  ("verified_user", "Background-checked team", "Every cleaner who enters your home has been screened and trained.")],
        faqs=[("How long does a standard cleaning take?", "Most homes take two to four hours depending on size and condition. You will see an estimated duration when you book online."),
              ("Do I need to be home?", "No. Many clients provide a door code or lockbox. We will confirm access details before your first visit."),
              ("Do you bring your own supplies?", "Yes. Our team arrives with professional equipment and cleaning products. If you prefer we use a specific product, just let us know in your booking notes."),
              ("What is the difference between a standard and a deep cleaning?", "Standard Cleaning maintains a home that is already in good shape. Deep Cleaning adds detail work such as baseboards, inside appliances, vents, blinds and buildup removal.")],
        related=["deep-cleaning", "recurring-cleaning", "add-on-services"],
        meta="Standard house cleaning in Las Vegas, Henderson and surrounding areas. Dusting, vacuuming, mopping, kitchens and bathrooms by background-checked cleaners. Book online.",
    ),
    dict(
        slug="deep-cleaning", name="Deep Cleaning", short="Deep Clean",
        icon="auto_awesome",
        card="A detailed, top-to-bottom clean that targets buildup, hard-to-reach areas, baseboards, fixtures and other commonly overlooked surfaces.",
        hero="deep-cleaning.jpg",
        hero_alt="Cleaner steam cleaning a radiator during a deep cleaning",
        gallery=[("deep-cleaning-2.jpg", "Professional extracting a carpet"),
                 ("bathroom-2.jpg", "Spotless bathroom with glass shower"),
                 ("about-cleaner.jpg", "Cleaner wiping down window shutters")],
        lead="Dust, grime and hard-water buildup collect fast in the desert. Our Deep Cleaning resets your home from ceiling to baseboard so every surface looks and feels new.",
        overview=[
            "Deep Cleaning includes everything in our Standard Cleaning plus the detail work that is easy to put off: baseboards, door frames, light fixtures, ceiling fans, vents, blinds, cabinet fronts and the buildup behind and under furniture that we can safely move.",
            "It is ideal before hosting, after a long stretch without professional help, for seasonal resets, or as the first visit before starting a recurring plan. Many Las Vegas homeowners book one each spring and fall to stay ahead of the dust.",
        ],
        includes=["Everything in a Standard Cleaning", "Baseboards, door frames and trim wiped by hand",
                  "Ceiling fans, light fixtures and vents dusted", "Blinds and window sills cleaned",
                  "Cabinet and drawer fronts wiped", "Soap scum and hard-water buildup removed",
                  "Grout and tile scrubbed in bathrooms", "Behind and under movable furniture",
                  "Appliance exteriors detailed, including stovetop and range hood", "Interior windows available as an add-on"],
        benefits=[("restart_alt", "A true reset", "The perfect starting point before a recurring plan or a big event."),
                  ("water_drop", "Built for Las Vegas", "We know desert dust and hard water, and we bring the right products for both."),
                  ("thumb_up", "Satisfaction first", "If something is missed, tell us within 24 hours and we will make it right.")],
        faqs=[("How often should I book a deep cleaning?", "Most homes benefit from a deep cleaning two to four times per year, with standard or recurring cleanings in between."),
              ("How long does it take?", "Plan for four to eight hours depending on the size and condition of the home. Larger homes may be scheduled with two cleaners."),
              ("Is inside the oven or fridge included?", "Those are available as add-ons so you only pay for what you need. You can select them when you book online."),
              ("Can you move furniture?", "We move light furniture such as chairs, side tables and small rugs. For safety we do not move heavy items like beds, dressers or appliances.")],
        related=["standard-cleaning", "move-in-move-out-cleaning", "add-on-services"],
        meta="Deep cleaning services in Las Vegas and Henderson. Baseboards, fixtures, buildup removal and detail work by background-checked cleaners. Instant online pricing.",
    ),
    dict(
        slug="recurring-cleaning", name="Recurring Cleaning", short="Recurring",
        icon="event_repeat",
        card="Weekly, bi-weekly or monthly visits designed to keep your home consistently clean without the hassle of scheduling each time.",
        hero="recurring-cleaning.jpg",
        hero_alt="Cleaner vacuuming a tidy bedroom during a recurring visit",
        gallery=[("family-living-room.jpg", "Clean family living room with a dog relaxing on the floor"),
                 ("standard-cleaning-3.jpg", "Mopping a hardwood floor"),
                 ("hero-living-room.jpg", "Bright, airy living room after cleaning")],
        lead="Set it once and come home to a clean house on a schedule that works for you. Recurring clients enjoy the same cleaner whenever possible, priority scheduling and our best rates.",
        overview=[
            "Choose weekly, bi-weekly or monthly visits and we handle the rest. Each visit follows our Standard Cleaning checklist, and we rotate in extra detail tasks so your home never slips back to needing a deep clean.",
            "Recurring plans are flexible. Skip a visit when you travel, add an extra clean before guests arrive, or change your frequency any time from your online account. There are no contracts and no cancellation fees with 24 hours notice.",
        ],
        includes=["Weekly, bi-weekly or monthly frequency", "Discounted recurring rates",
                  "Same cleaner whenever possible", "Priority scheduling and easy rescheduling",
                  "Full Standard Cleaning checklist every visit", "Rotating detail tasks to prevent buildup",
                  "Online account to manage, skip or add visits", "Add-ons available on any visit",
                  "No contracts, cancel any time", "Automatic reminders before each visit"],
        benefits=[("savings", "Best rates", "Recurring plans are our most affordable way to keep a consistently clean home."),
                  ("sync", "Easy to manage", "Reschedule, skip or add services online in a few taps."),
                  ("favorite", "Know your cleaner", "We match you with a consistent cleaner who learns your home and preferences.")],
        faqs=[("Which frequency is right for me?", "Weekly works well for busy families and homes with pets. Bi-weekly is our most popular plan. Monthly suits smaller households or homes that stay tidy between visits."),
              ("Do I need a deep cleaning first?", "If your home has not been professionally cleaned in the last month or two, we recommend starting with a Deep Cleaning so your recurring visits can focus on maintenance."),
              ("Can I skip a visit?", "Yes. Skip or reschedule from your online account with at least 24 hours notice at no charge."),
              ("Will I have the same cleaner each time?", "We do our best to send the same cleaner or team to every visit. If they are unavailable, we send another trained team member with your home notes.")],
        related=["standard-cleaning", "deep-cleaning", "add-on-services"],
        meta="Weekly, bi-weekly and monthly recurring house cleaning in Las Vegas and surrounding areas. Discounted rates, consistent cleaners, no contracts. Book online.",
    ),
    dict(
        slug="move-in-move-out-cleaning", name="Move-In / Move-Out Cleaning", short="Move In / Out",
        icon="local_shipping",
        card="Thorough cleaning for empty or transitioning homes, preparing the space for new occupants, landlords or property managers.",
        hero="move-in-move-out-cleaning.jpg",
        hero_alt="Two cleaners dusting and mopping an empty apartment before move-in",
        gallery=[("move-in-move-out-cleaning-2.jpg", "Homeowner packing moving boxes with a small dog"),
                 ("vacation-rental-cleaning-3.jpg", "Empty, freshly cleaned modern living room"),
                 ("bright-kitchen.jpg", "Clean kitchen ready for new occupants")],
        lead="Moving is stressful enough. Whether you are handing back keys or unpacking into a new place, we make sure the home is spotless, inspection-ready and welcoming.",
        overview=[
            "Our Move-Out Cleaning is designed around what landlords and property managers check: inside cabinets and drawers, inside the oven and refrigerator, baseboards, window tracks, closets, light fixtures and every floor. We help you leave the property in the condition your lease requires.",
            "Move-In Cleaning gives you a fresh start in a new home. We clean and sanitize the entire space before your boxes arrive, so the only fingerprints in your new kitchen are yours. Perfect for buyers, renters, landlords and real estate agents preparing a listing.",
        ],
        includes=["Everything in a Deep Cleaning", "Inside all cabinets, drawers and closets",
                  "Inside oven, refrigerator and microwave", "Window tracks and sills detailed",
                  "Baseboards, doors and trim wiped", "Light fixtures, fans and vents dusted",
                  "Bathrooms scrubbed, including grout and fixtures", "All floors vacuumed and mopped",
                  "Garage sweep-out available", "Interior windows and walls available as add-ons"],
        benefits=[("key", "Inspection ready", "Built around what landlords and property managers look for at a walk-through."),
                  ("inventory_2", "Empty-home pricing", "Pricing is based on the size of the home, with instant quotes online."),
                  ("apartment", "Landlords and agents welcome", "We work with property managers and realtors on fast turnarounds between tenants.")],
        faqs=[("Should the home be empty?", "Ideally, yes. An empty home lets us reach every surface. If some items will remain, note it in your booking and we will plan accordingly."),
              ("Do you need utilities on?", "Yes. We need working water and electricity to clean effectively. Please make sure both are on for your appointment."),
              ("How far in advance should I book?", "We recommend booking at least a few days ahead, especially at the end of the month. Same-week availability is often possible, so check the online calendar."),
              ("Can you clean before my closing or final walk-through?", "Absolutely. Let us know your deadline and we will schedule the clean to finish ahead of it.")],
        related=["deep-cleaning", "post-construction-cleaning", "add-on-services"],
        meta="Move-in and move-out cleaning in Las Vegas, Henderson and surrounding areas. Inspection-ready cleaning for renters, landlords, buyers and property managers. Book online.",
    ),
    dict(
        slug="commercial-cleaning", name="Commercial Cleaning", short="Commercial",
        icon="apartment",
        card="Customized cleaning for offices, retail spaces and other commercial properties to maintain a clean, professional environment.",
        hero="commercial-cleaning.jpg",
        hero_alt="Commercial cleaners wiping glass partitions and vacuuming an office",
        gallery=[("commercial-cleaning-2.jpg", "Floor machine polishing a commercial tile floor"),
                 ("commercial-cleaning-3.jpg", "Clean, modern office lounge"),
                 ("sanitizing.jpg", "Sanitizing a desk surface with disinfectant spray")],
        lead="A clean workplace says a lot about your business. We keep offices, showrooms, studios and retail spaces across Las Vegas spotless, on a schedule that never interrupts your day.",
        overview=[
            "We build a cleaning plan around your space, your hours and your traffic. Daily, weekly or custom frequencies are available, with after-hours and weekend visits so your team always walks into a fresh environment.",
            "Our commercial clients include small offices, medical and professional suites, salons, boutiques, fitness studios and short-term event spaces. Every visit follows a written scope of work and is performed by the same background-checked team whenever possible.",
        ],
        includes=["Reception, lobbies and common areas", "Desks, workstations and conference rooms",
                  "Restroom cleaning, sanitizing and restocking", "Break rooms and kitchenettes",
                  "Trash and recycling removal", "Glass doors, partitions and interior windows",
                  "Vacuuming, sweeping and mopping all floors", "High-touch surface disinfecting",
                  "After-hours and weekend scheduling", "Custom scope of work and checklists"],
        benefits=[("nights_stay", "After-hours service", "We clean when your business is closed so there is zero disruption."),
                  ("fact_check", "Written scope", "A clear, agreed checklist for every visit, with consistent quality."),
                  ("groups", "Reliable team", "Background-checked cleaners who know your space and your expectations.")],
        faqs=[("What types of businesses do you serve?", "Offices, professional and medical suites, retail boutiques, salons, studios and small venues across the Las Vegas valley. If you have a unique space, reach out and we will build a plan for it."),
              ("Do you offer one-time commercial cleans?", "Yes. One-time deep cleans, post-event cleanups and move-in or move-out cleaning for commercial spaces are all available."),
              ("How is commercial cleaning priced?", "Pricing depends on square footage, frequency and scope. Email us or book a walk-through and we will send a clear quote."),
              ("Are you able to work around our hours?", "Yes. Most commercial clients prefer evening or early-morning visits, and we schedule around your business hours.")],
        related=["post-construction-cleaning", "deep-cleaning", "recurring-cleaning"],
        meta="Commercial and office cleaning in Las Vegas and Henderson. Custom scopes, after-hours scheduling and background-checked teams for offices, retail and studios.",
    ),
    dict(
        slug="post-construction-cleaning", name="Post-Construction Cleaning", short="Post-Construction",
        icon="construction",
        card="Detailed removal of construction dust, debris and residue to get newly built or renovated spaces ready for use.",
        hero="post-construction-cleaning.jpg",
        hero_alt="Floor machine cleaning a newly finished tile floor after construction",
        gallery=[("post-construction-cleaning-2.jpg", "Vacuuming construction dust from a concrete floor"),
                 ("vacation-rental-cleaning-3.jpg", "Finished modern interior ready for move-in"),
                 ("bathroom.jpg", "Newly built bathroom with glass shower, fully cleaned")],
        lead="Renovations leave behind a fine layer of dust on everything. We remove it from every vent, cabinet and corner so your new space is ready to enjoy or show.",
        overview=[
            "Post-construction cleaning is a specialized service. Drywall dust, paint overspray, adhesive residue and sticker marks require different tools and more time than a standard clean. Our team works methodically from the top down so dust is not simply pushed around.",
            "We serve homeowners finishing a remodel, contractors preparing for a final walk-through, and builders and investors getting a property ready to list. Rough, final and touch-up phases are all available.",
        ],
        includes=["Dust removal from ceilings, walls, fans and vents", "Inside and outside all cabinets and drawers",
                  "Window interiors, tracks and frames", "Stickers, labels and paint overspray removed",
                  "Fixtures, hardware and appliances detailed", "Bathrooms and kitchens sanitized",
                  "Baseboards, doors and trim wiped", "Floors vacuumed with HEPA filtration and mopped",
                  "Debris bagged and removed", "Final walk-through touch-up available"],
        benefits=[("engineering", "Contractor friendly", "We coordinate with your builder or GC to clean at exactly the right stage."),
                  ("air", "HEPA filtration", "Fine dust is captured, not recirculated, for a healthier finished space."),
                  ("done_all", "Show ready", "Ideal before a final walk-through, a listing photo shoot or move-in day.")],
        faqs=[("When should post-construction cleaning happen?", "After the last trade has finished and all debris is removed. For large projects we can do a rough clean mid-project and a final clean at completion."),
              ("Do you remove construction debris?", "We bag and remove small debris and dust. Large materials, lumber and drywall scraps should be removed by your contractor before we arrive."),
              ("How is it priced?", "Post-construction pricing is based on square footage and the condition of the space. Email us with details or photos for a quote."),
              ("Can you clean a single remodeled room?", "Yes. Kitchen and bathroom remodels are among our most common post-construction jobs.")],
        related=["move-in-move-out-cleaning", "deep-cleaning", "commercial-cleaning"],
        meta="Post-construction cleaning in Las Vegas and surrounding areas. Dust, debris and residue removal for remodels, new builds and renovations. Request a quote today.",
    ),
    dict(
        slug="vacation-rental-cleaning", name="Vacation Rental Cleaning", short="Airbnb / STR",
        icon="king_bed",
        card="Reliable turnover cleaning between guests. We clean, restage and reset your Airbnb or short-term rental so it is ready for the next five-star stay.",
        hero="vacation-rental-cleaning.jpg",
        hero_alt="Beautifully staged vacation rental bedroom with fresh linens",
        gallery=[("vacation-rental-cleaning-2.jpg", "Open-plan vacation rental living and dining area"),
                 ("bathroom-2.jpg", "Hotel-clean bathroom with towels staged"),
                 ("vacation-rental-cleaning-3.jpg", "Modern short-term rental living room")],
        lead="Las Vegas hosts live and die by reviews. Our turnover service keeps your Airbnb, VRBO or corporate rental guest-ready every time, with photo confirmation and restocking built in.",
        overview=[
            "Turnover cleaning is more than a quick tidy. We strip and remake beds, launder or swap linens, sanitize every surface, restage the space to your photos and restock essentials so your next guest walks into a hotel-quality experience.",
            "We sync with your booking calendar so cleanings are scheduled automatically between check-out and check-in. Each visit ends with a damage and inventory check and photos sent to you, so you always know the condition of your property.",
        ],
        includes=["Full clean of every room between guests", "Beds stripped, linens changed and staged",
                  "Towels and linens laundered or swapped", "Kitchen reset, dishes done and fridge cleared",
                  "Bathrooms sanitized and restocked", "Consumables restocked (soap, paper goods, coffee)",
                  "Property restaged to match your listing photos", "Damage, left-items and inventory report",
                  "Photo confirmation after every turnover", "Calendar sync for automatic scheduling"],
        benefits=[("star", "Protect your rating", "Cleanliness is the number-one factor in guest reviews. We make it a sure thing."),
                  ("calendar_month", "Calendar synced", "Turnovers are scheduled automatically from your booking platform."),
                  ("photo_camera", "Photo verified", "Receive photos and a quick report after every clean, wherever you are.")],
        faqs=[("Can you handle same-day turnovers?", "Yes. Same-day turnovers between check-out and check-in are our specialty. We confirm timing from your calendar."),
              ("Do you provide linens and supplies?", "We can launder your linens on site or manage a swap set. Restocking of consumables is available with items billed at cost."),
              ("What if a guest leaves damage?", "Our team documents any damage with photos and notifies you immediately so you can file a claim before the next guest arrives."),
              ("Do you work with property managers?", "Yes. We support individual hosts as well as property managers with multiple units across the valley.")],
        related=["standard-cleaning", "deep-cleaning", "add-on-services"],
        meta="Airbnb and vacation rental turnover cleaning in Las Vegas and Henderson. Linen changes, restocking, restaging and photo verification. Calendar-synced scheduling.",
    ),
    dict(
        slug="add-on-services", name="Add-On Services", short="Add-Ons",
        icon="add_circle",
        card="Inside the fridge, inside the oven, interior windows, cabinets, dishes, laundry and more. Add exactly what you need to any cleaning.",
        hero="add-on-services.jpg",
        hero_alt="Hand wiping down a gas stovetop with a microfiber cloth",
        gallery=[("add-on-services-2.jpg", "Gloved hand spraying cleaner on a wood surface"),
                 ("bright-kitchen.jpg", "Spotless kitchen with clean appliances"),
                 ("deep-cleaning-2.jpg", "Carpet being professionally extracted")],
        lead="Every home is different. Our add-ons let you customize any cleaning so you only pay for the extras you actually want.",
        overview=[
            "Add-ons can be attached to any Standard, Deep, Recurring or Move-In / Move-Out cleaning. Simply select them when you book online and the price updates instantly. You can also add them to a single recurring visit without changing your plan.",
            "Not sure what you need? Add a note to your booking and our team will recommend the right extras for your home.",
        ],
        includes=["Inside refrigerator", "Inside oven", "Inside cabinets and drawers", "Interior windows",
                  "Dishes and loading the dishwasher", "Laundry wash, dry and fold", "Change bed linens",
                  "Interior walls spot cleaned", "Garage sweep-out", "Patio or balcony tidy"],
        benefits=[("tune", "Fully customizable", "Build the exact cleaning your home needs, visit by visit."),
                  ("bolt", "Instant pricing", "Add-on prices appear as you select them in the online booking form."),
                  ("repeat", "One time or every time", "Add an extra to a single visit or to every recurring cleaning.")],
        faqs=[("How do I add extras to my booking?", "Select them in the Extras step of the online booking form. You can also log in to your account and add them to an upcoming visit."),
              ("Can I add something on the day of the cleaning?", "Often, yes. Ask your cleaner and if time allows we will add it and update your invoice."),
              ("Are add-ons included in deep cleaning?", "Deep Cleaning covers detailed surface work. Inside the oven, inside the fridge and interior windows remain optional add-ons so you only pay for what you need."),
              ("Do you offer carpet shampooing?", "Not at this time. We vacuum thoroughly and can recommend a trusted local carpet cleaner for stains and extraction.")],
        related=["standard-cleaning", "deep-cleaning", "recurring-cleaning"],
        meta="Cleaning add-ons in Las Vegas: inside oven, inside fridge, interior windows, cabinets, laundry, dishes and more. Customize any cleaning with instant online pricing.",
    ),
]
BY_SLUG = {s["slug"]: s for s in SERVICES}

REVIEWS = [
    ("Sarah M.", "Super easy to book and the cleaning team did an amazing job. They showed up on time, were professional, and left the entire house looking spotless. I've already signed up for recurring cleanings!"),
    ("Jessica R.", "I've tried a few cleaning companies before and this has easily been the best experience. Communication was great, pricing was straightforward, and my home looked incredible afterward."),
    ("Michael T.", "We booked a deep clean and were extremely impressed. They paid attention to the little details and got areas cleaner than we expected. Definitely using them again."),
    ("Amanda L.", "Having them come every two weeks has been a lifesaver. They're reliable, consistent, and it's so nice coming home to a clean house without having to worry about it."),
    ("David K.", "Great experience from start to finish. Booking was simple, they kept me updated, and the cleaners did a fantastic job. Professional, dependable, and absolutely worth it."),
]

# --------------------------------------------------------------------------- layout
HEAD = Template("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<meta name="description" content="$description">
<link rel="canonical" href="$canonical">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#2f3b69">
<meta name="author" content="Aven Cleaning Co.">
<meta name="geo.region" content="US-NV">
<meta name="geo.placename" content="Las Vegas">
<meta property="og:type" content="$ogtype">
<meta property="og:site_name" content="Aven Cleaning Co.">
<meta property="og:title" content="$title">
<meta property="og:description" content="$description">
<meta property="og:url" content="$canonical">
<meta property="og:image" content="$ogimage">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="$title">
<meta name="twitter:description" content="$description">
<meta name="twitter:image" content="$ogimage">
<link rel="icon" href="${root}favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="${root}favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="${root}favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="${root}apple-touch-icon.png">
<link rel="manifest" href="${root}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,300..600,0..1,0&display=block" rel="stylesheet">
<script src="https://cdn.tailwindcss.com?plugins=forms"></script>
<script>
tailwind.config = {
  theme: { extend: {
    colors: { primary: "#2f3b69", "primary-dark": "#243052", accent: "#c5a059", "accent-light": "#e8d9b5", cream: "#fafaff" },
    fontFamily: { sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"], serif: ["Playfair Display", "Georgia", "serif"] },
    borderRadius: { DEFAULT: "0.125rem", lg: "0.25rem", xl: "0.5rem", "2xl": "0.75rem", full: "9999px" },
  } }
}
</script>
<style>
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
  body { background: #fafaff; }
  .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; line-height: 1; vertical-align: middle; }
  .nav-dropdown { visibility: hidden; opacity: 0; transform: translateY(6px); transition: opacity .15s ease, transform .15s ease, visibility .15s; }
  .nav-dropdown-trigger:hover .nav-dropdown, .nav-dropdown-trigger:focus-within .nav-dropdown, .nav-dropdown-trigger.open .nav-dropdown { visibility: visible; opacity: 1; transform: translateY(0); }
  details > summary { list-style: none; cursor: pointer; }
  details > summary::-webkit-details-marker { display: none; }
  details[open] .faq-icon { transform: rotate(45deg); }
  .faq-icon { transition: transform .2s ease; }
  :focus-visible { outline: 2px solid #c5a059; outline-offset: 3px; }
  .skip-link { position: absolute; left: -999px; top: 8px; z-index: 100; background: #2f3b69; color: #fff; padding: .5rem 1rem; }
  .skip-link:focus { left: 8px; }
  #mobile-menu { max-height: calc(100vh - 100%); overflow-y: auto; }
  @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } * { transition: none !important; } }
</style>
$jsonld
</head>
<body class="bg-cream font-sans text-slate-800 antialiased selection:bg-accent/30">
<a href="#main" class="skip-link">Skip to content</a>
""")

def header(root, active):
    def nav_cls(key):
        return ("text-primary border-b border-primary pb-1 font-bold" if active == key
                else "text-slate-500 hover:text-primary transition-colors font-semibold")
    svc_links = "\n".join(
        f'<a class="block px-5 py-2.5 text-[11px] uppercase tracking-widest {"text-primary font-bold bg-stone-50" if active == s["slug"] else "text-slate-600 hover:bg-stone-50 hover:text-primary"} transition-colors" href="{root}services/{s["slug"]}/">{s["name"]}</a>'
        for s in SERVICES)
    svc_mobile = "\n".join(
        f'<a class="block py-2 text-sm {"text-primary font-semibold" if active == s["slug"] else "text-slate-600"}" href="{root}services/{s["slug"]}/">{s["name"]}</a>'
        for s in SERVICES)
    svc_active = active == "services" or active in BY_SLUG
    lw, lh = dims("logo.png")
    return f"""
<header id="site-header" class="sticky top-0 z-50 border-b border-stone-200 bg-cream/90 backdrop-blur-md">
  <div class="mx-auto flex max-w-7xl items-center justify-between gap-6 px-5 py-4 md:px-10 lg:px-12">
    <a href="{root}" class="flex shrink-0 items-center" aria-label="{BRAND} home">
      <img src="{root}images/logo.png" alt="{BRAND}" width="{lw}" height="{lh}" class="h-10 w-auto md:h-12" decoding="async">
    </a>
    <nav class="hidden items-center gap-8 lg:flex" aria-label="Main">
      <a class="text-xs uppercase tracking-widest {nav_cls('home')}" href="{root}">Home</a>
      <div class="nav-dropdown-trigger relative">
        <button type="button" class="nav-dropdown-btn flex items-center gap-1 text-xs uppercase tracking-widest {('text-primary border-b border-primary pb-1 font-bold' if svc_active else 'text-slate-500 hover:text-primary transition-colors font-semibold')}" aria-haspopup="true" aria-expanded="false">
          Services <span class="material-symbols-outlined text-base" aria-hidden="true">expand_more</span>
        </button>
        <div class="nav-dropdown absolute left-0 top-full z-50 w-72 border border-stone-200 bg-white pt-2 pb-2 shadow-xl">
          <a class="block px-5 py-2.5 text-[11px] uppercase tracking-widest {('text-primary font-bold bg-stone-50' if active == 'services' else 'text-slate-600 hover:bg-stone-50 hover:text-primary')} transition-colors" href="{root}services/">All Services</a>
          <div class="my-1 border-t border-stone-100"></div>
          {svc_links}
        </div>
      </div>
      <a class="text-xs uppercase tracking-widest {nav_cls('about')}" href="{root}about/">About</a>
      <a class="text-xs uppercase tracking-widest {nav_cls('contact')}" href="{root}contact/">Contact</a>
    </nav>
    <div class="flex items-center gap-3">
      <a href="{root}book/" class="hidden h-10 items-center justify-center bg-primary px-6 text-[11px] font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-primary-dark sm:inline-flex">Book Now</a>
      <button id="mobile-menu-btn" type="button" class="-mr-2 inline-flex h-11 w-11 items-center justify-center text-primary lg:hidden" aria-label="Open menu" aria-controls="mobile-menu" aria-expanded="false">
        <span class="material-symbols-outlined text-3xl" id="mobile-menu-icon" aria-hidden="true">menu</span>
      </button>
    </div>
  </div>
  <div id="mobile-menu" class="absolute inset-x-0 top-full hidden border-b border-stone-200 bg-white shadow-xl lg:hidden">
    <nav class="mx-auto flex max-w-7xl flex-col px-5 py-4 md:px-10" aria-label="Mobile">
      <a class="py-3 text-xs font-semibold uppercase tracking-widest {('text-primary' if active == 'home' else 'text-slate-700')}" href="{root}">Home</a>
      <details class="group border-t border-stone-100" {"open" if svc_active else ""}>
        <summary class="flex items-center justify-between py-3 text-xs font-semibold uppercase tracking-widest {('text-primary' if svc_active else 'text-slate-700')}">
          Services <span class="material-symbols-outlined text-xl transition-transform group-open:rotate-180" aria-hidden="true">expand_more</span>
        </summary>
        <div class="pb-3 pl-4">
          <a class="block py-2 text-sm font-semibold {('text-primary' if active == 'services' else 'text-slate-700')}" href="{root}services/">All Services</a>
          {svc_mobile}
        </div>
      </details>
      <a class="border-t border-stone-100 py-3 text-xs font-semibold uppercase tracking-widest {('text-primary' if active == 'about' else 'text-slate-700')}" href="{root}about/">About</a>
      <a class="border-t border-stone-100 py-3 text-xs font-semibold uppercase tracking-widest {('text-primary' if active == 'contact' else 'text-slate-700')}" href="{root}contact/">Contact</a>
      <a href="{root}book/" class="mt-3 inline-flex h-12 items-center justify-center bg-primary px-6 text-[11px] font-bold uppercase tracking-[0.2em] text-white">Book Now</a>
      <a href="mailto:{EMAIL}" class="mt-3 inline-flex items-center justify-center gap-2 py-2 text-sm text-slate-600"><span class="material-symbols-outlined text-lg" aria-hidden="true">mail</span>{EMAIL}</a>
    </nav>
  </div>
</header>
<main id="main">
"""

def footer(root):
    lw, lh = dims("logo-white.png")
    svc = "\n".join(f'<li><a class="text-sm text-slate-300 transition-colors hover:text-accent" href="{root}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f"""
</main>
<footer class="bg-primary-dark text-white">
  <div class="mx-auto max-w-7xl px-5 py-16 md:px-10 lg:px-12">
    <div class="grid grid-cols-1 gap-12 md:grid-cols-2 lg:grid-cols-12">
      <div class="lg:col-span-5">
        <a href="{root}" class="inline-block" aria-label="{BRAND} home"><img src="{root}images/logo-white.png" alt="{BRAND}" width="{lw}" height="{lh}" class="h-12 w-auto" loading="lazy" decoding="async"></a>
        <p class="mt-6 max-w-sm text-sm font-light leading-relaxed text-slate-300">A higher standard of clean for homes and businesses in Las Vegas and the surrounding valley. Locally owned, background-checked and five-star rated.</p>
        <ul class="mt-6 space-y-2 text-sm text-slate-300">
          <li class="flex items-center gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">mail</span><a class="hover:text-accent" href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li class="flex items-center gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">location_on</span>Las Vegas, Nevada &amp; surrounding areas</li>
          <li class="flex items-center gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">schedule</span>Book online 24/7</li>
        </ul>
      </div>
      <div class="lg:col-span-3">
        <h2 class="mb-5 text-[11px] font-bold uppercase tracking-[0.2em] text-accent">Services</h2>
        <ul class="space-y-2.5">{svc}</ul>
      </div>
      <div class="lg:col-span-2">
        <h2 class="mb-5 text-[11px] font-bold uppercase tracking-[0.2em] text-accent">Company</h2>
        <ul class="space-y-2.5">
          <li><a class="text-sm text-slate-300 hover:text-accent" href="{root}about/">About Us</a></li>
          <li><a class="text-sm text-slate-300 hover:text-accent" href="{root}services/">All Services</a></li>
          <li><a class="text-sm text-slate-300 hover:text-accent" href="{root}#reviews">Reviews</a></li>
          <li><a class="text-sm text-slate-300 hover:text-accent" href="{root}contact/">Contact</a></li>
          <li><a class="text-sm text-slate-300 hover:text-accent" href="{root}book/">Book Now</a></li>
        </ul>
      </div>
      <div class="lg:col-span-2">
        <h2 class="mb-5 text-[11px] font-bold uppercase tracking-[0.2em] text-accent">Service Area</h2>
        <ul class="space-y-2.5 text-sm text-slate-300">
          {"".join(f"<li>{a}</li>" for a in AREAS[:6])}
          <li><a class="hover:text-accent" href="{root}about/#areas">View all areas</a></li>
        </ul>
      </div>
    </div>
    <div class="mt-14 flex flex-col items-start justify-between gap-4 border-t border-white/10 pt-8 text-xs text-slate-400 md:flex-row md:items-center">
      <p>&copy; {YEAR} {BRAND} All rights reserved.</p>
      <div class="flex flex-wrap gap-x-6 gap-y-2">
        <a class="hover:text-accent" href="{root}privacy-policy/">Privacy Policy</a>
        <a class="hover:text-accent" href="{root}terms/">Terms of Service</a>
        <a class="hover:text-accent" href="{root}sitemap.xml">Sitemap</a>
      </div>
    </div>
  </div>
</footer>
<script>
(function () {{
  var btn = document.getElementById('mobile-menu-btn');
  var menu = document.getElementById('mobile-menu');
  var icon = document.getElementById('mobile-menu-icon');
  function setOpen(open) {{
    menu.classList.toggle('hidden', !open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    icon.textContent = open ? 'close' : 'menu';
  }}
  btn.addEventListener('click', function () {{ setOpen(menu.classList.contains('hidden')); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') setOpen(false); }});
  document.addEventListener('click', function (e) {{
    if (!menu.classList.contains('hidden') && !menu.contains(e.target) && !btn.contains(e.target)) setOpen(false);
  }});
  window.addEventListener('resize', function () {{ if (window.innerWidth >= 1024) setOpen(false); }});
  /* desktop dropdown: click/tap support in addition to hover */
  var trig = document.querySelector('.nav-dropdown-trigger');
  var tbtn = trig && trig.querySelector('.nav-dropdown-btn');
  if (tbtn) {{
    tbtn.addEventListener('click', function (e) {{
      e.preventDefault();
      var open = !trig.classList.contains('open');
      trig.classList.toggle('open', open);
      tbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }});
    document.addEventListener('click', function (e) {{ if (!trig.contains(e.target)) {{ trig.classList.remove('open'); tbtn.setAttribute('aria-expanded', 'false'); }} }});
  }}
}})();
</script>
</body>
</html>
"""

def cta_band(root, title="Ready for a cleaner home?", text="Get instant pricing and pick a time that works for you. Booking takes about 60 seconds.", dark=True):
    return f"""
<section class="bg-primary text-white">
  <div class="mx-auto flex max-w-7xl flex-col items-start justify-between gap-8 px-5 py-16 md:flex-row md:items-center md:px-10 lg:px-12">
    <div>
      <h2 class="font-serif text-3xl italic md:text-4xl">{title}</h2>
      <p class="mt-3 max-w-xl text-slate-200">{text}</p>
    </div>
    <div class="flex flex-col gap-3 sm:flex-row">
      <a href="{root}book/" class="inline-flex h-12 items-center justify-center gap-2 bg-accent px-8 text-[11px] font-bold uppercase tracking-[0.2em] text-primary-dark transition-colors hover:bg-accent-light">Book Online <span class="material-symbols-outlined text-base" aria-hidden="true">arrow_forward</span></a>
      <a href="mailto:{EMAIL}" class="inline-flex h-12 items-center justify-center gap-2 border border-white/40 px-8 text-[11px] font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-white/10">Email Us</a>
    </div>
  </div>
</section>
"""

def service_card(root, s, compact=False):
    return f"""
<a href="{root}services/{s['slug']}/" class="group flex flex-col border border-stone-200 bg-white transition-all hover:-translate-y-1 hover:border-accent/60 hover:shadow-xl">
  <div class="aspect-[4/3] overflow-hidden">
    {img(s['hero'], s['hero_alt'], 'h-full w-full object-cover transition-transform duration-500 group-hover:scale-105').replace('$root$', root)}
  </div>
  <div class="flex flex-1 flex-col p-7">
    <div class="mb-3 flex items-center gap-3">
      <span class="material-symbols-outlined text-accent" aria-hidden="true">{s['icon']}</span>
      <h3 class="font-serif text-xl text-primary transition-colors group-hover:text-accent">{s['name']}</h3>
    </div>
    <p class="flex-1 text-sm font-light leading-relaxed text-slate-600">{s['card']}</p>
    <span class="mt-6 inline-flex items-center gap-2 text-[11px] font-bold uppercase tracking-widest text-primary">Learn more <span class="material-symbols-outlined text-base transition-transform group-hover:translate-x-1" aria-hidden="true">east</span></span>
  </div>
</a>"""

def trust_bar():
    items = [("verified_user", "Background-Checked", "Every cleaner is screened and trained"),
             ("star", "5-Star Rated", "Loved by Las Vegas homeowners"),
             ("home_pin", "Locally Owned", "A Las Vegas business, not a franchise"),
             ("bolt", "Instant Online Booking", "See your price and book in 60 seconds")]
    lis = "".join(f"""
      <li class="flex items-start gap-4">
        <span class="material-symbols-outlined mt-0.5 text-3xl text-accent" aria-hidden="true">{i}</span>
        <div><p class="text-sm font-bold uppercase tracking-wider text-primary">{t}</p><p class="mt-1 text-sm font-light text-slate-500">{d}</p></div>
      </li>""" for i, t, d in items)
    return f"""
<section class="border-y border-stone-200 bg-white" aria-label="Why choose us">
  <div class="mx-auto max-w-7xl px-5 py-10 md:px-10 lg:px-12">
    <ul class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">{lis}</ul>
  </div>
</section>"""

def breadcrumb(root, items):
    # items: list of (label, href or None)
    parts = []
    for i, (label, href) in enumerate(items):
        if href is None:
            parts.append(f'<li aria-current="page" class="text-primary">{label}</li>')
        else:
            parts.append(f'<li><a class="hover:text-primary" href="{href}">{label}</a></li>')
        if i < len(items) - 1:
            parts.append('<li aria-hidden="true" class="text-slate-400">/</li>')
    return f'<nav aria-label="Breadcrumb"><ol class="flex flex-wrap items-center gap-2 text-[11px] uppercase tracking-widest text-slate-500">{"".join(parts)}</ol></nav>'

def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + p} for i, (n, p) in enumerate(items)]}

def jsonld(*objs):
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in objs if o)

LOCAL_BUSINESS = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": SITE_URL + "/#business",
    "name": BRAND,
    "url": SITE_URL + "/",
    "logo": SITE_URL + "/images/logo-stacked.png",
    "image": SITE_URL + "/images/og-image.jpg",
    "email": EMAIL,
    "founder": {"@type": "Person", "name": OWNER},
    "description": "Residential and commercial cleaning services in Las Vegas, Nevada and surrounding areas. Standard, deep, recurring, move-in/move-out, commercial, post-construction and vacation rental cleaning.",
    "address": {"@type": "PostalAddress", "addressLocality": "Las Vegas", "addressRegion": "NV", "addressCountry": "US"},
    "areaServed": [{"@type": "City", "name": a} for a in AREAS],
    "priceRange": "$$",
    "slogan": "A higher standard of clean.",
    "sameAs": [],
    "potentialAction": {"@type": "ReserveAction", "target": SITE_URL + "/book/", "name": "Book a cleaning"},
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Cleaning Services",
                        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"], "url": f"{SITE_URL}/services/{s['slug']}/"}} for s in SERVICES]},
}

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", path)

def page(path, root, title, description, body, active, ld=None, ogtype="website", ogimage=None):
    canonical = SITE_URL + "/" + path.replace("index.html", "")
    head = HEAD.safe_substitute(title=html.escape(title), description=html.escape(description), canonical=canonical,
                                ogtype=ogtype, ogimage=ogimage or f"{SITE_URL}/images/og-image.jpg",
                                root=root, jsonld=jsonld(*(ld or [])))
    body = body.replace("$root$", root)
    write(path, head + header(root, active) + body + footer(root))

# --------------------------------------------------------------------------- home
def build_home():
    root = ""
    hero = f"""
<section class="relative overflow-hidden bg-stone-100">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-16 md:px-10 lg:grid-cols-12 lg:px-12 lg:py-24">
    <div class="lg:col-span-7">
      <span class="mb-5 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Las Vegas &amp; Surrounding Areas</span>
      <h1 class="font-serif text-5xl italic leading-[1.05] text-slate-900 md:text-6xl xl:text-7xl">A Higher Standard of <span class="not-italic font-black text-primary">Clean.</span></h1>
      <p class="mt-8 max-w-xl border-l-2 border-accent pl-6 text-lg font-light leading-relaxed text-slate-600 md:text-xl">Reliable, detail-driven residential and commercial cleaning for busy homeowners, families, hosts and businesses across the Las Vegas valley. Background-checked cleaners, straightforward pricing and booking that takes a minute.</p>
      <div class="mt-10 flex flex-col gap-4 sm:flex-row">
        <a href="#book" class="inline-flex h-14 items-center justify-center gap-2 bg-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-primary-dark">Book Online <span class="material-symbols-outlined text-base" aria-hidden="true">arrow_forward</span></a>
        <a href="{root}services/" class="inline-flex h-14 items-center justify-center gap-2 border border-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-primary transition-colors hover:bg-primary hover:text-white">View Services</a>
      </div>
      <ul class="mt-10 flex flex-wrap gap-x-8 gap-y-3 text-sm text-slate-600">
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">verified_user</span>Background-checked</li>
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">star</span>5-star rated</li>
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">home_pin</span>Locally owned</li>
      </ul>
    </div>
    <div class="relative lg:col-span-5">
      <div class="absolute -right-3 -top-3 h-20 w-20 border-r-2 border-t-2 border-accent" aria-hidden="true"></div>
      <div class="absolute -bottom-3 -left-3 h-20 w-20 border-b-2 border-l-2 border-accent" aria-hidden="true"></div>
      <div class="aspect-[4/5] overflow-hidden border border-stone-200 shadow-2xl">
        {img('hero-living-room.jpg', 'Bright, spotless living room cleaned by Aven Cleaning Co.', 'h-full w-full object-cover', lazy=False)}
      </div>
      <div class="absolute bottom-6 left-6 right-6 flex items-center gap-4 bg-white/95 p-4 shadow-lg backdrop-blur md:left-auto md:right-8 md:w-72">
        <span class="material-symbols-outlined text-3xl text-accent" aria-hidden="true">request_quote</span>
        <div><p class="text-sm font-bold text-primary">Instant online pricing</p><p class="text-xs text-slate-500">Choose your home size and extras. See your price before you book.</p></div>
      </div>
    </div>
  </div>
</section>
"""
    services = f"""
<section class="bg-cream py-20 lg:py-24" id="services">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="mx-auto mb-14 max-w-2xl text-center">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">What We Do</span>
      <h2 class="font-serif text-4xl italic text-primary md:text-5xl">Cleaning services for every space</h2>
      <p class="mt-5 font-light leading-relaxed text-slate-600">From a quick weekly refresh to a top-to-bottom reset, every service is performed by trained, background-checked cleaners using professional products and a detailed checklist.</p>
    </div>
    <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 xl:grid-cols-4">
      {"".join(service_card(root, s) for s in SERVICES)}
    </div>
  </div>
</section>
"""
    about = f"""
<section class="border-y border-stone-200 bg-white py-20 lg:py-24" id="about">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-14 px-5 md:px-10 lg:grid-cols-2 lg:px-12">
    <div class="relative order-2 lg:order-1">
      <div class="grid grid-cols-2 gap-4">
        {img('about-cleaner.jpg', 'Aven Cleaning Co. cleaner wiping window shutters', 'aspect-[3/4] w-full border border-stone-200 object-cover')}
        {img('care-gloves.jpg', 'Cleaner making a heart shape with gloved hands', 'mt-10 aspect-[3/4] w-full border border-stone-200 object-cover')}
      </div>
      <div class="absolute -bottom-6 left-1/2 flex -translate-x-1/2 items-center gap-4 bg-primary px-6 py-4 text-white shadow-xl">
        <span class="material-symbols-outlined text-3xl text-accent" aria-hidden="true">workspace_premium</span>
        <p class="text-sm font-semibold leading-tight">Locally owned<br><span class="font-light text-slate-200">Las Vegas, Nevada</span></p>
      </div>
    </div>
    <div class="order-1 lg:order-2">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">About Aven Cleaning Co.</span>
      <h2 class="font-serif text-4xl italic text-primary md:text-5xl">Cleaning you can count on, from people you can trust</h2>
      <p class="mt-6 font-light leading-relaxed text-slate-600">Aven Cleaning Co. was founded in Las Vegas by {OWNER} with a simple idea: a cleaning company should make life easier, not add to the to-do list. That means showing up on time, doing exactly what we said we would, and leaving your home or workplace noticeably better than we found it.</p>
      <p class="mt-4 font-light leading-relaxed text-slate-600">We serve busy homeowners, families, professionals, short-term rental hosts and local businesses who value convenience and want a dependable team they can use again and again.</p>
      <ul class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2">
        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">check_circle</span><span class="text-sm text-slate-700">Background-checked, trained cleaners</span></li>
        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">check_circle</span><span class="text-sm text-slate-700">Transparent, upfront online pricing</span></li>
        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">check_circle</span><span class="text-sm text-slate-700">Professional supplies and equipment included</span></li>
        <li class="flex items-start gap-3"><span class="material-symbols-outlined text-accent" aria-hidden="true">check_circle</span><span class="text-sm text-slate-700">Easy rescheduling, no contracts</span></li>
      </ul>
      <a href="{root}about/" class="mt-10 inline-flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.2em] text-primary hover:text-accent">Our story <span class="material-symbols-outlined text-base" aria-hidden="true">east</span></a>
    </div>
  </div>
</section>
"""
    steps = [("1", "edit_calendar", "Book in 60 seconds", "Choose your service, home size and extras online. Your price shows instantly and you pick the date and time that works."),
             ("2", "cleaning_services", "We clean", "A background-checked cleaner arrives on time with professional supplies and follows a detailed room-by-room checklist."),
             ("3", "sentiment_very_satisfied", "Enjoy your space", "Come home to a spotless house. Rate your clean, leave notes for next time and set up a recurring plan if you love it.")]
    how = f"""
<section class="bg-cream py-20 lg:py-24">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="mx-auto mb-14 max-w-2xl text-center">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">How It Works</span>
      <h2 class="font-serif text-4xl italic text-primary md:text-5xl">Three simple steps to a cleaner home</h2>
    </div>
    <ol class="grid grid-cols-1 gap-8 md:grid-cols-3">
      {"".join(f'''
      <li class="relative border border-stone-200 bg-white p-8">
        <span class="absolute right-6 top-5 font-serif text-5xl italic text-stone-200" aria-hidden="true">{n}</span>
        <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">{i}</span>
        <h3 class="mt-5 font-serif text-2xl text-primary">{t}</h3>
        <p class="mt-3 text-sm font-light leading-relaxed text-slate-600">{d}</p>
      </li>''' for n, i, t, d in steps)}
    </ol>
    <div class="mt-12 text-center">
      <a href="#book" class="inline-flex h-14 items-center justify-center gap-2 bg-primary px-10 text-xs font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-primary-dark">Get Your Instant Price <span class="material-symbols-outlined text-base" aria-hidden="true">arrow_forward</span></a>
    </div>
  </div>
</section>
"""
    booking = f"""
<section class="bg-stone-50 border-y border-stone-200" id="book">
  <div class="mx-auto max-w-7xl px-5 py-16 md:px-10 lg:px-12 lg:py-20">
    <div class="mx-auto mb-10 max-w-2xl text-center">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Online Booking</span>
      <h2 class="font-serif text-4xl italic text-primary md:text-5xl">Book your <span class="not-italic font-black">cleaning</span></h2>
      <p class="mt-5 font-light leading-relaxed text-slate-600">Choose your service, home size and any extras — see your price instantly, then pick the date and time that works for you.</p>
    </div>
    <div class="mx-auto max-w-5xl border-y border-stone-200 bg-white sm:border sm:shadow-xl">
      <iframe
        id="home-booking-frame"
        src="{BOOK_EMBED}"
        title="Aven Cleaning Co. online booking form"
        class="home-booking-frame block w-full"
        scrolling="yes"
        allow="payment"
        referrerpolicy="strict-origin-when-cross-origin"
        loading="lazy"></iframe>
    </div>
    <p class="mt-5 text-center text-xs text-slate-500">Trouble loading? <a class="underline hover:text-primary" href="{BOOK_URL}" target="_blank" rel="noopener">Open the booking form in a new tab</a> or email <a class="underline hover:text-primary" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>
<style>
  /* Home page booking iframe — viewport-based height, internal scrolling, no embed.js */
  .home-booking-frame {{ height: calc(100vh - 120px); height: calc(100svh - 120px); min-height: 620px; border: 0; }}
  @media (min-width: 768px) {{ .home-booking-frame {{ height: calc(100vh - 160px); height: calc(100svh - 160px); min-height: 720px; }} }}
</style>
"""
    areas = f"""
<section class="relative overflow-hidden bg-primary-dark text-white" id="areas">
  <div class="absolute inset-0">
    {img('las-vegas-strip.jpg', '', 'h-full w-full object-cover opacity-30')}
    <div class="absolute inset-0 bg-gradient-to-r from-primary-dark via-primary-dark/90 to-primary-dark/60" aria-hidden="true"></div>
  </div>
  <div class="relative mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-20 md:px-10 lg:grid-cols-2 lg:px-12 lg:py-28">
    <div>
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Service Area</span>
      <h2 class="font-serif text-4xl italic md:text-5xl">Proudly serving Las Vegas and the surrounding valley</h2>
      <p class="mt-6 max-w-lg font-light leading-relaxed text-slate-200">From Summerlin to Henderson and everywhere in between, our team travels across the valley. If you do not see your neighborhood listed, reach out and we will let you know if we can help.</p>
      <a href="{root}contact/" class="mt-8 inline-flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.2em] text-accent hover:text-accent-light">Check your area <span class="material-symbols-outlined text-base" aria-hidden="true">east</span></a>
    </div>
    <ul class="grid grid-cols-2 gap-x-6 gap-y-3 sm:grid-cols-3">
      {"".join(f'<li class="flex items-center gap-2 text-sm text-slate-100"><span class="material-symbols-outlined text-base text-accent" aria-hidden="true">location_on</span>{a}</li>' for a in AREAS)}
      <li class="flex items-center gap-2 text-sm text-slate-100"><span class="material-symbols-outlined text-base text-accent" aria-hidden="true">location_on</span>And more</li>
    </ul>
  </div>
</section>
"""
    stars = '<span class="flex text-accent" aria-label="5 out of 5 stars">' + ''.join('<span class="material-symbols-outlined text-lg" style="font-variation-settings:\'FILL\' 1" aria-hidden="true">star</span>' for _ in range(5)) + '</span>'
    reviews = f"""
<section class="bg-cream py-20 lg:py-24" id="reviews">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="mx-auto mb-14 max-w-2xl text-center">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Reviews</span>
      <h2 class="font-serif text-4xl italic text-primary md:text-5xl">What our clients say</h2>
      <p class="mt-5 font-light text-slate-600">Five-star rated by homeowners across Las Vegas.</p>
    </div>
    <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
      {"".join(f'''
      <figure class="flex flex-col border border-stone-200 bg-white p-8 {"lg:col-span-1" if i < 3 else ""}">
        {stars}
        <blockquote class="mt-5 flex-1 font-light leading-relaxed text-slate-700">&ldquo;{html.escape(q)}&rdquo;</blockquote>
        <figcaption class="mt-6 flex items-center gap-3">
          <span class="flex h-10 w-10 items-center justify-center rounded-full bg-primary font-serif text-lg text-white" aria-hidden="true">{n[0]}</span>
          <div><p class="text-sm font-bold text-primary">{n}</p><p class="text-xs text-slate-500">Verified client</p></div>
        </figcaption>
      </figure>''' for i, (n, q) in enumerate(REVIEWS))}
      <div class="flex flex-col items-start justify-center border border-dashed border-accent/60 bg-accent/5 p-8">
        <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">rate_review</span>
        <h3 class="mt-4 font-serif text-2xl text-primary">Join our happy clients</h3>
        <p class="mt-2 text-sm font-light text-slate-600">Book your first cleaning and see why Las Vegas homeowners keep coming back.</p>
        <a href="#book" class="mt-6 inline-flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.2em] text-primary hover:text-accent">Book now <span class="material-symbols-outlined text-base" aria-hidden="true">east</span></a>
      </div>
    </div>
  </div>
</section>
"""
    body = hero + trust_bar() + services + about + how + booking + areas + reviews + cta_band(root)
    ld = [LOCAL_BUSINESS,
          {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": SITE_URL + "/"}]
    page("index.html", root, f"{BRAND} | House & Commercial Cleaning in Las Vegas, NV",
         "Aven Cleaning Co. provides residential and commercial cleaning in Las Vegas, Henderson and surrounding areas. Standard, deep, recurring, move-in/out, Airbnb and post-construction cleaning. Book online in 60 seconds.",
         body, "home", ld)

# --------------------------------------------------------------------------- services index
def build_services_index():
    root = "../"
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto max-w-7xl px-5 py-14 md:px-10 lg:px-12 lg:py-20">
    {breadcrumb(root, [("Home", root), ("Services", None)])}
    <div class="mt-6 max-w-3xl">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Our Services</span>
      <h1 class="font-serif text-5xl italic text-slate-900 md:text-6xl">Cleaning services in <span class="not-italic font-black text-primary">Las Vegas</span></h1>
      <p class="mt-6 text-lg font-light leading-relaxed text-slate-600">Residential and commercial cleaning tailored to the way you live and work. Every service is performed by background-checked cleaners with professional supplies and a detailed checklist. Pricing is instant when you book online.</p>
    </div>
  </div>
</section>
<section class="bg-cream py-16 lg:py-20">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {"".join(service_card(root, s) for s in SERVICES)}
    </div>
  </div>
</section>
<section class="border-t border-stone-200 bg-white py-16">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-10 px-5 md:grid-cols-2 md:px-10 lg:px-12">
    <div>
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Not sure which to choose?</span>
      <h2 class="font-serif text-3xl italic text-primary md:text-4xl">A quick guide</h2>
      <ul class="mt-6 space-y-4 text-sm font-light leading-relaxed text-slate-600">
        <li><strong class="font-semibold text-primary">First time with us?</strong> Start with a <a class="underline hover:text-accent" href="{root}services/deep-cleaning/">Deep Cleaning</a>, then maintain with <a class="underline hover:text-accent" href="{root}services/recurring-cleaning/">Recurring</a> visits.</li>
        <li><strong class="font-semibold text-primary">Home already in good shape?</strong> A <a class="underline hover:text-accent" href="{root}services/standard-cleaning/">Standard Cleaning</a> is all you need.</li>
        <li><strong class="font-semibold text-primary">Moving?</strong> Our <a class="underline hover:text-accent" href="{root}services/move-in-move-out-cleaning/">Move-In / Move-Out</a> service is built for inspections and fresh starts.</li>
        <li><strong class="font-semibold text-primary">Host or business owner?</strong> See <a class="underline hover:text-accent" href="{root}services/vacation-rental-cleaning/">Vacation Rental</a> and <a class="underline hover:text-accent" href="{root}services/commercial-cleaning/">Commercial</a> cleaning.</li>
      </ul>
    </div>
    <div class="border border-stone-200 bg-stone-50 p-8">
      <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">support_agent</span>
      <h3 class="mt-4 font-serif text-2xl text-primary">Still have questions?</h3>
      <p class="mt-2 text-sm font-light text-slate-600">Email us with a few details about your space and we will recommend the right service and send a clear quote.</p>
      <a href="mailto:{EMAIL}" class="mt-6 inline-flex h-12 items-center justify-center gap-2 bg-primary px-6 text-[11px] font-bold uppercase tracking-[0.2em] text-white hover:bg-primary-dark">{EMAIL}</a>
    </div>
  </div>
</section>
{cta_band(root)}
"""
    ld = [breadcrumb_ld([("Home", "/"), ("Services", "/services/")]),
          {"@context": "https://schema.org", "@type": "ItemList", "name": "Cleaning Services",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f"{SITE_URL}/services/{s['slug']}/"} for i, s in enumerate(SERVICES)]}]
    page("services/index.html", root, f"Cleaning Services in Las Vegas | {BRAND}",
         "Explore Aven Cleaning Co. services in Las Vegas and surrounding areas: standard, deep, recurring, move-in/out, commercial, post-construction and Airbnb cleaning. Instant online pricing.",
         body, "services", ld)

# --------------------------------------------------------------------------- service pages
def build_service(s):
    root = "../../"
    incl = "".join(f'<li class="flex items-start gap-3 text-sm text-slate-700"><span class="material-symbols-outlined mt-px text-xl text-accent" aria-hidden="true">check_circle</span>{i}</li>' for i in s["includes"])
    bens = "".join(f'''
      <div class="border border-stone-200 bg-white p-7">
        <span class="material-symbols-outlined text-3xl text-accent" aria-hidden="true">{i}</span>
        <h3 class="mt-4 font-serif text-xl text-primary">{t}</h3>
        <p class="mt-2 text-sm font-light leading-relaxed text-slate-600">{d}</p>
      </div>''' for i, t, d in s["benefits"])
    faqs = "".join(f'''
      <details class="group border-b border-stone-200 py-5">
        <summary class="flex items-start justify-between gap-6 font-semibold text-primary">
          <span>{q}</span>
          <span class="material-symbols-outlined faq-icon shrink-0 text-accent" aria-hidden="true">add</span>
        </summary>
        <p class="mt-3 pr-10 text-sm font-light leading-relaxed text-slate-600">{a}</p>
      </details>''' for q, a in s["faqs"])
    g = s["gallery"]
    related = "".join(service_card(root, BY_SLUG[r]) for r in s["related"])
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-12 px-5 py-14 md:px-10 lg:grid-cols-2 lg:px-12 lg:py-20">
    <div>
      {breadcrumb(root, [("Home", root), ("Services", root + "services/"), (s["name"], None)])}
      <span class="mb-4 mt-6 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Las Vegas &amp; Surrounding Areas</span>
      <h1 class="font-serif text-4xl italic text-slate-900 md:text-5xl xl:text-6xl">{s['name']}</h1>
      <p class="mt-6 text-lg font-light leading-relaxed text-slate-600">{s['lead']}</p>
      <div class="mt-8 flex flex-col gap-4 sm:flex-row">
        <a href="{root}book/" class="inline-flex h-14 items-center justify-center gap-2 bg-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-primary-dark">Book Online <span class="material-symbols-outlined text-base" aria-hidden="true">arrow_forward</span></a>
        <a href="{root}contact/" class="inline-flex h-14 items-center justify-center border border-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-primary transition-colors hover:bg-primary hover:text-white">Ask a Question</a>
      </div>
    </div>
    <div class="relative">
      <div class="absolute -right-3 -top-3 h-16 w-16 border-r-2 border-t-2 border-accent" aria-hidden="true"></div>
      <div class="aspect-[4/3] overflow-hidden border border-stone-200 shadow-xl">
        {img(s['hero'], s['hero_alt'], 'h-full w-full object-cover', lazy=False)}
      </div>
    </div>
  </div>
</section>

<section class="bg-white py-16 lg:py-20">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-14 px-5 md:px-10 lg:grid-cols-12 lg:px-12">
    <div class="lg:col-span-7">
      <h2 class="font-serif text-3xl italic text-primary">Overview</h2>
      {"".join(f'<p class="mt-5 font-light leading-relaxed text-slate-600">{p}</p>' for p in s["overview"])}
      <h2 class="mt-12 font-serif text-3xl italic text-primary">What&rsquo;s included</h2>
      <ul class="mt-6 grid grid-cols-1 gap-x-8 gap-y-3 sm:grid-cols-2">{incl}</ul>
    </div>
    <aside class="lg:col-span-5">
      <div class="sticky top-28 space-y-6">
        <div class="border border-stone-200 bg-stone-50 p-8">
          <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">request_quote</span>
          <h3 class="mt-4 font-serif text-2xl text-primary">Instant pricing online</h3>
          <p class="mt-2 text-sm font-light leading-relaxed text-slate-600">Select your home size, frequency and any add-ons and your price appears before you confirm. No phone calls, no waiting for a callback.</p>
          <a href="{root}book/" class="mt-6 inline-flex h-12 w-full items-center justify-center gap-2 bg-primary text-[11px] font-bold uppercase tracking-[0.2em] text-white hover:bg-primary-dark">Get My Price</a>
          <p class="mt-4 text-center text-xs text-slate-500">Prefer email? <a class="underline hover:text-primary" href="mailto:{EMAIL}">{EMAIL}</a></p>
        </div>
        <ul class="divide-y divide-stone-200 border border-stone-200 bg-white text-sm">
          <li class="flex items-center gap-3 p-4"><span class="material-symbols-outlined text-accent" aria-hidden="true">verified_user</span>Background-checked cleaners</li>
          <li class="flex items-center gap-3 p-4"><span class="material-symbols-outlined text-accent" aria-hidden="true">inventory</span>Supplies &amp; equipment included</li>
          <li class="flex items-center gap-3 p-4"><span class="material-symbols-outlined text-accent" aria-hidden="true">event_available</span>Free rescheduling with 24h notice</li>
          <li class="flex items-center gap-3 p-4"><span class="material-symbols-outlined text-accent" aria-hidden="true">home_pin</span>Locally owned in Las Vegas</li>
        </ul>
      </div>
    </aside>
  </div>
</section>

<section class="bg-cream py-16 lg:py-20">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="grid grid-cols-1 gap-8 md:grid-cols-3">{bens}</div>
    <div class="mt-8 grid grid-cols-2 gap-4">
      {img(g[0][0], g[0][1], 'aspect-[4/3] w-full border border-stone-200 object-cover')}
      {img(g[1][0], g[1][1], 'aspect-[4/3] w-full border border-stone-200 object-cover')}
      {img(g[2][0], g[2][1], 'col-span-2 aspect-[21/9] w-full border border-stone-200 object-cover')}
    </div>
  </div>
</section>

<section class="border-y border-stone-200 bg-white py-16 lg:py-20">
  <div class="mx-auto max-w-3xl px-5 md:px-10">
    <span class="mb-4 block text-center text-xs font-bold uppercase tracking-[0.3em] text-accent">FAQ</span>
    <h2 class="text-center font-serif text-3xl italic text-primary md:text-4xl">{s['name']} questions</h2>
    <div class="mt-8 border-t border-stone-200">{faqs}</div>
  </div>
</section>

<section class="bg-cream py-16 lg:py-20">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <h2 class="mb-10 text-center font-serif text-3xl italic text-primary md:text-4xl">Related services</h2>
    <div class="grid grid-cols-1 gap-8 md:grid-cols-3">{related}</div>
  </div>
</section>
{cta_band(root, f"Book your {s['name'].lower()} today")}
"""
    ld = [breadcrumb_ld([("Home", "/"), ("Services", "/services/"), (s["name"], f"/services/{s['slug']}/")]),
          {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
           "description": s["card"], "url": f"{SITE_URL}/services/{s['slug']}/",
           "image": f"{SITE_URL}/images/{s['hero']}",
           "provider": {"@id": SITE_URL + "/#business"},
           "areaServed": [{"@type": "City", "name": a} for a in AREAS]},
          {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]}]
    page(f"services/{s['slug']}/index.html", root, f"{s['name']} in Las Vegas, NV | {BRAND}", s["meta"], body, s["slug"], ld,
         ogimage=f"{SITE_URL}/images/{s['hero']}")

# --------------------------------------------------------------------------- about
def build_about():
    root = "../"
    values = [("handshake", "Reliability", "We show up when we say we will and do exactly what we promised. Every time."),
              ("search", "Attention to detail", "Baseboards, fixtures, corners. The small things are what make a clean feel complete."),
              ("lock", "Trust", "Every cleaner is background-checked and trained before they ever step into a client's home."),
              ("chat", "Clear communication", "Upfront pricing, reminders before every visit and quick answers when you need them.")]
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto max-w-7xl px-5 py-14 md:px-10 lg:px-12 lg:py-20">
    {breadcrumb(root, [("Home", root), ("About", None)])}
    <div class="mt-6 max-w-3xl">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">About Us</span>
      <h1 class="font-serif text-5xl italic text-slate-900 md:text-6xl">Locally owned. <span class="not-italic font-black text-primary">Detail obsessed.</span></h1>
      <p class="mt-6 text-lg font-light leading-relaxed text-slate-600">Aven Cleaning Co. is a Las Vegas cleaning company built around one goal: making life easier for the people and businesses we serve.</p>
    </div>
  </div>
</section>

<section class="bg-white py-16 lg:py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-14 px-5 md:px-10 lg:grid-cols-2 lg:px-12">
    <div>
      <h2 class="font-serif text-3xl italic text-primary md:text-4xl">Our story</h2>
      <p class="mt-6 font-light leading-relaxed text-slate-600">Aven Cleaning Co. was founded by {OWNER} right here in Las Vegas. After seeing how many cleaning services over-promised and under-delivered, {OWNER.split()[0]} set out to build a company that busy homeowners, families, professionals and business owners could rely on without a second thought.</p>
      <p class="mt-4 font-light leading-relaxed text-slate-600">Our approach is simple. Hire great people and background-check every one of them. Use professional products and a detailed checklist on every visit. Price everything upfront so there are no surprises. And make booking as easy as ordering dinner.</p>
      <p class="mt-4 font-light leading-relaxed text-slate-600">Today we serve homes, short-term rentals and commercial spaces across the Las Vegas valley, and most of our clients come to us through referrals from neighbors and friends. We think that is the best review we could ask for.</p>
      <div class="mt-8 flex items-center gap-4 border-l-2 border-accent pl-6">
        <div><p class="font-serif text-xl text-primary">{OWNER}</p><p class="text-sm text-slate-500">Owner, Aven Cleaning Co.</p></div>
      </div>
    </div>
    <div class="relative">
      <div class="absolute -right-3 -top-3 h-20 w-20 border-r-2 border-t-2 border-accent" aria-hidden="true"></div>
      <div class="absolute -bottom-3 -left-3 h-20 w-20 border-b-2 border-l-2 border-accent" aria-hidden="true"></div>
      {img('about-cleaner.jpg', 'Aven Cleaning Co. team member carefully cleaning window shutters', 'aspect-[4/3] w-full border border-stone-200 object-cover shadow-xl', lazy=False)}
    </div>
  </div>
</section>

<section class="border-y border-stone-200 bg-cream py-16 lg:py-24">
  <div class="mx-auto max-w-7xl px-5 md:px-10 lg:px-12">
    <div class="mx-auto mb-12 max-w-2xl text-center">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">What We Stand For</span>
      <h2 class="font-serif text-4xl italic text-primary">Our values</h2>
    </div>
    <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
      {"".join(f'''
      <div class="border border-stone-200 bg-white p-8">
        <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">{i}</span>
        <h3 class="mt-5 font-serif text-2xl text-primary">{t}</h3>
        <p class="mt-3 text-sm font-light leading-relaxed text-slate-600">{d}</p>
      </div>''' for i, t, d in values)}
    </div>
  </div>
</section>

<section class="bg-white py-16 lg:py-24">
  <div class="mx-auto grid max-w-7xl grid-cols-1 items-center gap-14 px-5 md:px-10 lg:grid-cols-2 lg:px-12">
    <div class="order-2 lg:order-1 grid grid-cols-2 gap-4">
      {img('family-living-room.jpg', 'Clean family living room with a dog relaxing', 'aspect-[4/3] w-full border border-stone-200 object-cover')}
      {img('bathroom-2.jpg', 'Sparkling clean bathroom', 'aspect-[4/3] w-full border border-stone-200 object-cover')}
      {img('commercial-cleaning-3.jpg', 'Clean, modern office lounge', 'col-span-2 aspect-[21/9] w-full border border-stone-200 object-cover')}
    </div>
    <div class="order-1 lg:order-2">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Who We Serve</span>
      <h2 class="font-serif text-3xl italic text-primary md:text-4xl">Homes, rentals and businesses across the valley</h2>
      <p class="mt-6 font-light leading-relaxed text-slate-600">Our ideal clients are busy people who value their time. Families who would rather spend Saturday together than scrubbing bathrooms. Professionals who want to come home to a reset house. Hosts who need flawless turnovers. Business owners who want their space to reflect their standards.</p>
      <ul class="mt-8 space-y-3">
        {"".join(f'<li class="flex items-center gap-3 text-sm text-slate-700"><span class="material-symbols-outlined text-accent" aria-hidden="true">check_circle</span><a class="hover:text-primary hover:underline" href="{root}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)}
      </ul>
    </div>
  </div>
</section>

<section class="relative overflow-hidden bg-primary-dark text-white" id="areas">
  <div class="absolute inset-0">
    {img('las-vegas-sign.jpg', '', 'h-full w-full object-cover opacity-25')}
    <div class="absolute inset-0 bg-gradient-to-b from-primary-dark via-primary-dark/85 to-primary-dark/70" aria-hidden="true"></div>
  </div>
  <div class="relative mx-auto max-w-7xl px-5 py-20 md:px-10 lg:px-12 lg:py-24">
    <div class="max-w-2xl">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Service Area</span>
      <h2 class="font-serif text-4xl italic md:text-5xl">Where we clean</h2>
      <p class="mt-6 font-light leading-relaxed text-slate-200">We serve Las Vegas and the surrounding communities below. Not sure if you are in range? <a class="underline hover:text-accent" href="mailto:{EMAIL}">Email us</a> your zip code and we will confirm.</p>
    </div>
    <ul class="mt-10 grid grid-cols-2 gap-x-6 gap-y-3 sm:grid-cols-3 lg:grid-cols-4">
      {"".join(f'<li class="flex items-center gap-2 text-sm text-slate-100"><span class="material-symbols-outlined text-base text-accent" aria-hidden="true">location_on</span>{a}</li>' for a in AREAS)}
      <li class="flex items-center gap-2 text-sm text-slate-100"><span class="material-symbols-outlined text-base text-accent" aria-hidden="true">location_on</span>Surrounding areas</li>
    </ul>
  </div>
</section>
{cta_band(root, "Let's get your space sparkling", "Book online in about a minute, or email us with any questions. We would love to earn your trust.")}
"""
    ld = [breadcrumb_ld([("Home", "/"), ("About", "/about/")]),
          {"@context": "https://schema.org", "@type": "AboutPage", "name": f"About {BRAND}", "url": SITE_URL + "/about/", "about": {"@id": SITE_URL + "/#business"}}]
    page("about/index.html", root, f"About Us | {BRAND} | Locally Owned Las Vegas Cleaners",
         "Meet Aven Cleaning Co., a locally owned Las Vegas cleaning company founded by Kasey Rivera. Background-checked cleaners, upfront pricing and a detail-obsessed approach to every home and business.",
         body, "about", ld)

# --------------------------------------------------------------------------- contact
def build_contact():
    root = "../"
    quick = [("How do I get a price?", f'Book online and your price appears instantly as you choose your home size and extras. For commercial or post-construction work, <a class="underline hover:text-primary" href="mailto:{EMAIL}">email us</a> a few details for a quote.'),
             ("How soon can you come?", "We often have availability within the week. Check the live calendar on the booking page for the soonest openings."),
             ("Do I need to be home?", "No. Many clients leave a lockbox code or garage code. We confirm access details before your visit."),
             ("What is your cancellation policy?", "Reschedule or cancel free of charge with at least 24 hours notice from your online account or by email.")]
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto max-w-7xl px-5 py-14 md:px-10 lg:px-12 lg:py-20">
    {breadcrumb(root, [("Home", root), ("Contact", None)])}
    <div class="mt-6 max-w-3xl">
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Contact</span>
      <h1 class="font-serif text-5xl italic text-slate-900 md:text-6xl">Let&rsquo;s <span class="not-italic font-black text-primary">talk clean.</span></h1>
      <p class="mt-6 text-lg font-light leading-relaxed text-slate-600">Questions about a service, a custom quote for your business, or help with a booking? We are happy to help.</p>
    </div>
  </div>
</section>

<section class="bg-white py-16 lg:py-20">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-8 px-5 md:px-10 lg:grid-cols-3 lg:px-12">
    <a href="mailto:{EMAIL}?subject=Cleaning%20inquiry" class="group border border-stone-200 bg-cream p-8 transition-all hover:-translate-y-1 hover:border-accent/60 hover:shadow-xl">
      <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">mail</span>
      <h2 class="mt-4 font-serif text-2xl text-primary">Email us</h2>
      <p class="mt-2 text-sm font-light text-slate-600">For quotes, questions and anything else. We reply quickly during business hours.</p>
      <p class="mt-5 break-all text-sm font-semibold text-primary group-hover:text-accent">{EMAIL}</p>
    </a>
    <a href="{root}book/" class="group border border-stone-200 bg-cream p-8 transition-all hover:-translate-y-1 hover:border-accent/60 hover:shadow-xl">
      <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">event_available</span>
      <h2 class="mt-4 font-serif text-2xl text-primary">Book online</h2>
      <p class="mt-2 text-sm font-light text-slate-600">Instant pricing and live availability. Pick your service, date and time in about a minute.</p>
      <p class="mt-5 text-[11px] font-bold uppercase tracking-[0.2em] text-primary group-hover:text-accent">Go to booking &rarr;</p>
    </a>
    <div class="border border-stone-200 bg-cream p-8">
      <span class="material-symbols-outlined text-4xl text-accent" aria-hidden="true">location_on</span>
      <h2 class="mt-4 font-serif text-2xl text-primary">Service area</h2>
      <p class="mt-2 text-sm font-light text-slate-600">Las Vegas, Henderson, North Las Vegas, Summerlin, Spring Valley, Enterprise, Paradise and surrounding communities.</p>
      <a href="{root}about/#areas" class="mt-5 inline-block text-[11px] font-bold uppercase tracking-[0.2em] text-primary hover:text-accent">All areas &rarr;</a>
    </div>
  </div>
</section>

<section class="border-y border-stone-200 bg-cream py-16 lg:py-20">
  <div class="mx-auto grid max-w-7xl grid-cols-1 gap-14 px-5 md:px-10 lg:grid-cols-2 lg:px-12">
    <div>
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Send a Message</span>
      <h2 class="font-serif text-3xl italic text-primary md:text-4xl">Tell us about your space</h2>
      <p class="mt-4 text-sm font-light leading-relaxed text-slate-600">Fill in the details below and your email app will open with everything ready to send to {EMAIL}.</p>
      <form id="contact-form" class="mt-8 space-y-4" novalidate>
        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <label class="block"><span class="sr-only">Your name</span><input name="name" required autocomplete="name" class="w-full border-stone-300 bg-white p-4 text-sm focus:border-accent focus:ring-accent" placeholder="Your name" type="text"></label>
          <label class="block"><span class="sr-only">Phone</span><input name="phone" autocomplete="tel" class="w-full border-stone-300 bg-white p-4 text-sm focus:border-accent focus:ring-accent" placeholder="Phone (optional)" type="tel"></label>
        </div>
        <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <label class="block"><span class="sr-only">Service</span>
            <select name="service" class="w-full border-stone-300 bg-white p-4 text-sm focus:border-accent focus:ring-accent">
              <option value="">Service you're interested in</option>
              {"".join(f'<option>{s["name"]}</option>' for s in SERVICES)}
              <option>Something else</option>
            </select></label>
          <label class="block"><span class="sr-only">Zip code</span><input name="zip" inputmode="numeric" autocomplete="postal-code" class="w-full border-stone-300 bg-white p-4 text-sm focus:border-accent focus:ring-accent" placeholder="Zip code" type="text"></label>
        </div>
        <label class="block"><span class="sr-only">Message</span><textarea name="message" rows="5" class="w-full border-stone-300 bg-white p-4 text-sm focus:border-accent focus:ring-accent" placeholder="Tell us about your home or business, and anything specific you need."></textarea></label>
        <button type="submit" class="inline-flex h-14 w-full items-center justify-center gap-2 bg-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-white transition-colors hover:bg-primary-dark sm:w-auto">Send Message <span class="material-symbols-outlined text-base" aria-hidden="true">send</span></button>
      </form>
    </div>
    <div>
      <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Quick Answers</span>
      <h2 class="font-serif text-3xl italic text-primary md:text-4xl">Before you reach out</h2>
      <div class="mt-6 border-t border-stone-200">
        {"".join(f'''
        <details class="group border-b border-stone-200 py-5">
          <summary class="flex items-start justify-between gap-6 font-semibold text-primary"><span>{q}</span><span class="material-symbols-outlined faq-icon shrink-0 text-accent" aria-hidden="true">add</span></summary>
          <p class="mt-3 pr-10 text-sm font-light leading-relaxed text-slate-600">{a}</p>
        </details>''' for q, a in quick)}
      </div>
      <div class="mt-8 overflow-hidden border border-stone-200">
        {img('las-vegas-sign.jpg', 'Welcome to Fabulous Las Vegas sign', 'aspect-[16/9] w-full object-cover')}
      </div>
    </div>
  </div>
</section>
<script>
document.getElementById('contact-form').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target; var v = function (n) {{ return (f.elements[n].value || '').trim(); }};
  if (!v('name')) {{ f.elements['name'].focus(); f.elements['name'].reportValidity(); return; }}
  var subject = 'Cleaning inquiry' + (v('service') ? ': ' + v('service') : '') + ' - ' + v('name');
  var body = 'Name: ' + v('name') + '\\nPhone: ' + (v('phone') || '-') + '\\nService: ' + (v('service') || '-') + '\\nZip code: ' + (v('zip') || '-') + '\\n\\n' + v('message');
  window.location.href = 'mailto:{EMAIL}?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
}});
</script>
{cta_band(root, "Prefer to skip the email?", "Get instant pricing and live availability on our booking page.")}
"""
    ld = [breadcrumb_ld([("Home", "/"), ("Contact", "/contact/")]),
          {"@context": "https://schema.org", "@type": "ContactPage", "name": f"Contact {BRAND}", "url": SITE_URL + "/contact/", "about": {"@id": SITE_URL + "/#business"}}]
    page("contact/index.html", root, f"Contact Us | {BRAND} | Las Vegas Cleaning Services",
         f"Contact Aven Cleaning Co. in Las Vegas. Email {EMAIL} for quotes and questions, or book your cleaning online with instant pricing and live availability.",
         body, "contact", ld)

# --------------------------------------------------------------------------- book
def build_book():
    root = "../"
    body = f"""
<section class="border-b border-stone-200 bg-stone-100">
  <div class="mx-auto max-w-7xl px-5 py-10 md:px-10 lg:px-12 lg:py-14">
    {breadcrumb(root, [("Home", root), ("Book Now", None)])}
    <div class="mt-5 flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
      <div class="max-w-2xl">
        <span class="mb-3 block text-xs font-bold uppercase tracking-[0.3em] text-accent">Online Booking</span>
        <h1 class="font-serif text-4xl italic text-slate-900 md:text-5xl">Book your <span class="not-italic font-black text-primary">cleaning</span></h1>
        <p class="mt-4 font-light leading-relaxed text-slate-600">Choose your service, home size and extras to see your price instantly, then pick a date and time. Booking takes about a minute.</p>
      </div>
      <ul class="flex flex-wrap gap-x-6 gap-y-2 text-sm text-slate-600">
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">lock</span>Secure checkout</li>
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">event_available</span>Live availability</li>
        <li class="flex items-center gap-2"><span class="material-symbols-outlined text-accent" aria-hidden="true">verified_user</span>Background-checked</li>
      </ul>
    </div>
  </div>
</section>

<section class="bg-cream">
  <div class="mx-auto max-w-5xl px-0 py-6 sm:px-5 md:px-10 md:py-10">
    <div class="booking-frame-wrap border-y border-stone-200 bg-white sm:border sm:shadow-xl">
      <iframe
        id="booking-frame"
        src="{BOOK_EMBED}"
        title="Aven Cleaning Co. online booking form"
        class="booking-frame block w-full"
        scrolling="yes"
        allow="payment"
        referrerpolicy="strict-origin-when-cross-origin"
        loading="eager"></iframe>
    </div>
    <p class="mt-5 px-5 text-center text-xs text-slate-500 sm:px-0">Scroll inside the form to complete each step. Trouble loading? <a class="underline hover:text-primary" href="{BOOK_URL}" target="_blank" rel="noopener">Open the booking form in a new tab</a> or email <a class="underline hover:text-primary" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  </div>
</section>
<style>
  /* The booking iframe uses a fixed viewport-based height with its own internal scrolling.
     No embed.js / iframe-resizer is loaded, so the frame behaves like a normal browser viewport
     and BookingKoala's modals appear inside the frame where the user is looking. */
  .booking-frame {{ height: calc(100vh - 120px); height: calc(100svh - 120px); min-height: 620px; border: 0; }}
  @media (min-width: 768px) {{ .booking-frame {{ height: calc(100vh - 160px); height: calc(100svh - 160px); min-height: 720px; }} }}
</style>
"""
    ld = [breadcrumb_ld([("Home", "/"), ("Book Now", "/book/")])]
    page("book/index.html", root, f"Book Online | {BRAND} | Instant Cleaning Quotes in Las Vegas",
         "Book your Las Vegas house cleaning online with Aven Cleaning Co. Instant pricing, live availability and secure checkout. Standard, deep, recurring, move-in/out and more.",
         body, "book", ld)

# --------------------------------------------------------------------------- legal
def legal_page(path, title, h1, sections, desc):
    root = "../"
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto max-w-7xl px-5 py-14 md:px-10 lg:px-12">
    {breadcrumb(root, [("Home", root), (h1, None)])}
    <h1 class="mt-6 font-serif text-4xl italic text-slate-900 md:text-5xl">{h1}</h1>
    <p class="mt-3 text-sm text-slate-500">Last updated: October 7, 2026</p>
  </div>
</section>
<section class="bg-white py-14">
  <div class="mx-auto max-w-3xl px-5 md:px-10">
    {"".join(f'<h2 class="mt-10 font-serif text-2xl text-primary first:mt-0">{h}</h2>' + "".join(f'<p class="mt-4 font-light leading-relaxed text-slate-600">{p}</p>' for p in ps) for h, ps in sections)}
  </div>
</section>
"""
    page(path, root, f"{title} | {BRAND}", desc, body, "legal", [])

def build_legal():
    legal_page("privacy-policy/index.html", "Privacy Policy", "Privacy Policy", [
        ("Overview", [f"{BRAND} (\"we\", \"us\") respects your privacy. This policy explains what information we collect when you visit our website or book a service, how we use it and the choices you have."]),
        ("Information we collect", ["When you book a cleaning or contact us, we collect the information you provide, such as your name, email address, phone number, service address, access instructions and payment details. Payment information is processed securely by our booking and payment providers and is not stored on our website.",
                                    "Our website may also collect standard technical information such as your browser type, device, pages visited and approximate location through cookies or similar technologies, including third-party fonts and scripts used to display the site."]),
        ("How we use your information", ["We use your information to schedule and perform cleaning services, communicate about appointments, process payments, respond to inquiries, improve our services and send service-related reminders. With your consent we may send occasional promotions; you can opt out at any time."]),
        ("Sharing", ["We do not sell your personal information. We share it only with service providers who help us operate, such as our online booking platform, payment processors and email tools, and only as needed to deliver our services or as required by law."]),
        ("Your choices", [f"You may request access to, correction of or deletion of your personal information by emailing <a class=\"underline hover:text-primary\" href=\"mailto:{EMAIL}\">{EMAIL}</a>. You can disable cookies in your browser settings, although some features of the site may not function properly."]),
        ("Contact", [f"Questions about this policy can be sent to <a class=\"underline hover:text-primary\" href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
    ], f"Privacy policy for {BRAND}, a Las Vegas cleaning company. Learn what information we collect, how we use it and your choices.")
    legal_page("terms/index.html", "Terms of Service", "Terms of Service", [
        ("Agreement", [f"By booking a service with {BRAND} or using this website you agree to these terms. Please read them carefully."]),
        ("Services and pricing", ["Prices shown during online booking are based on the information you provide, including home size, condition and selected extras. If the condition or size of the property differs significantly from what was booked, we may adjust the price or scope and will communicate with you before proceeding."]),
        ("Scheduling, rescheduling and cancellation", ["Appointments may be rescheduled or cancelled free of charge with at least 24 hours notice. Cancellations with less notice, or inability to access the property at the scheduled time, may incur a fee. Arrival windows may vary due to traffic and prior appointments."]),
        ("Access and safety", ["You are responsible for providing safe access to the property and for securing pets, valuables and fragile items. For safety reasons our team does not move heavy furniture or appliances, climb higher than a two-step ladder, or handle biohazards."]),
        ("Satisfaction", ["If you are not satisfied with any part of your cleaning, let us know within 24 hours and we will return to address the area at no additional charge."]),
        ("Liability", ["We take great care in your home. In the unlikely event of damage caused by our team, notify us within 48 hours so we can review and resolve the issue promptly. Our liability is limited to the cost of the service performed except where prohibited by law."]),
        ("Changes", ["We may update these terms from time to time. Continued use of our services after changes are posted constitutes acceptance of the updated terms."]),
        ("Contact", [f"Questions about these terms can be sent to <a class=\"underline hover:text-primary\" href=\"mailto:{EMAIL}\">{EMAIL}</a>."]),
    ], f"Terms of service for {BRAND} cleaning services in Las Vegas, including scheduling, cancellation and satisfaction policies.")

# --------------------------------------------------------------------------- 404
def build_404():
    root = "/"
    body = f"""
<section class="bg-stone-100">
  <div class="mx-auto max-w-3xl px-5 py-24 text-center md:px-10 lg:py-32">
    <span class="mb-4 block text-xs font-bold uppercase tracking-[0.3em] text-accent">404</span>
    <h1 class="font-serif text-5xl italic text-slate-900 md:text-6xl">This page got <span class="not-italic font-black text-primary">swept away.</span></h1>
    <p class="mt-6 font-light leading-relaxed text-slate-600">The page you are looking for does not exist or has moved. Let us get you back on track.</p>
    <div class="mt-10 flex flex-col justify-center gap-4 sm:flex-row">
      <a href="{root}" class="inline-flex h-14 items-center justify-center gap-2 bg-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-white hover:bg-primary-dark">Back to Home</a>
      <a href="{root}services/" class="inline-flex h-14 items-center justify-center border border-primary px-8 text-xs font-bold uppercase tracking-[0.2em] text-primary hover:bg-primary hover:text-white">View Services</a>
    </div>
  </div>
</section>
"""
    head = HEAD.safe_substitute(title=f"Page Not Found | {BRAND}", description="The page you requested could not be found.", canonical=SITE_URL + "/404.html",
                                ogtype="website", ogimage=f"{SITE_URL}/images/og-image.jpg", root=root, jsonld="")
    head = head.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    write("404.html", head + header(root, "none") + body.replace("$root$", root) + footer(root))

# --------------------------------------------------------------------------- misc files
def build_misc():
    pages = ["/", "/services/"] + [f"/services/{s['slug']}/" for s in SERVICES] + ["/about/", "/contact/", "/book/", "/privacy-policy/", "/terms/"]
    prio = lambda p: "1.0" if p == "/" else ("0.9" if p in ("/book/", "/services/") else ("0.8" if p.startswith("/services/") else ("0.3" if p in ("/privacy-policy/", "/terms/") else "0.7")))
    urls = "\n".join(f"  <url><loc>{SITE_URL}{p}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>{prio(p)}</priority></url>" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({
        "name": BRAND, "short_name": "Aven Cleaning", "description": "Residential and commercial cleaning in Las Vegas and surrounding areas.",
        "icons": [{"src": "/android-chrome-192x192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/android-chrome-512x512.png", "sizes": "512x512", "type": "image/png"}],
        "theme_color": "#2f3b69", "background_color": "#fafaff", "display": "browser", "start_url": "/"}, indent=2) + "\n")
    write(".nojekyll", "")
    write(".gitignore", "# Source material (not part of the deployed site)\nStock images/\nstyle 3/\n*.csv\nACC_logo.png\n\n# OS / editor\n.DS_Store\nThumbs.db\ndesktop.ini\n")

if __name__ == "__main__":
    build_home()
    build_services_index()
    for s in SERVICES:
        build_service(s)
    build_about()
    build_contact()
    build_book()
    build_legal()
    build_404()
    build_misc()
