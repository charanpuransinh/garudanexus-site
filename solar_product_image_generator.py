#!/usr/bin/env python3
# Solar Product Image Generator
# Creates one separate product image for every item (9-45), plus JSON, CSV and HTML catalog.

import os
import re
import csv
import json
import base64
import time
import html
from pathlib import Path
from openai import OpenAI

# ---------- SETTINGS ----------
MODEL = os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-2.5-flare")
QUALITY = os.getenv("IMAGE_QUALITY", "high")  # low / medium / high
IMAGE_SIZE = "1024x1024"
OUTPUT_FORMAT = "jpeg"
OUTPUT_DIR = Path("solar_product_catalog")
IMAGE_DIR = OUTPUT_DIR / "images"
RETRY_COUNT = 3
WAIT_SECONDS = 3

# Product data: descriptions are intentionally general; exact ratings/specifications
# should be added only after confirming the actual supplier's product datasheet.
PRODUCTS = [
    {"id": 9, "name": "Rooftop Structure", "category": "Mounting Structures",
     "description": "A rooftop mounting structure used to support and secure solar PV modules on building roofs. It is typically engineered from corrosion-resistant metal sections and selected according to roof type, wind load and module layout.",
     "features": "Roof-mounted rails, brackets and support members; corrosion-resistant finish; designed for stable module positioning."},
    {"id": 10, "name": "Ground Structure", "category": "Mounting Structures",
     "description": "A ground-mounted support framework that holds solar PV modules above the ground at a planned tilt and orientation. Foundation design and structural sizing depend on site soil, wind loads and project engineering.",
     "features": "Metal support posts, beams and module rails; fixed-tilt arrangement; site-specific foundation interface."},
    {"id": 11, "name": "Carport Structure", "category": "Mounting Structures",
     "description": "A canopy-style solar mounting structure installed above a parking area. It supports PV modules while providing sheltered parking space beneath the structure.",
     "features": "Canopy frame, columns and module supports; open parking clearance; engineered drainage and foundations."},
    {"id": 12, "name": "Rail", "category": "Mounting Structures",
     "description": "An aluminium or steel mounting rail that forms the linear support interface between solar modules and the mounting structure.",
     "features": "Extruded or formed rail profile; module mounting channel; compatible with the specified clamps and brackets."},
    {"id": 13, "name": "Purlin", "category": "Mounting Structures",
     "description": "A structural cross-member used to support rails or solar mounting components and transfer loads to the primary structure.",
     "features": "Metal structural section; load-transfer member; profile and thickness selected by engineering design."},
    {"id": 14, "name": "Mid Clamp", "category": "Mounting Structures",
     "description": "A solar module mid clamp fitted between two adjacent panels to hold their frame edges securely to the mounting rail.",
     "features": "Compact metal clamp with bolt; designed for the specified module-frame thickness and rail system."},
    {"id": 15, "name": "End Clamp", "category": "Mounting Structures",
     "description": "A solar module end clamp used at the outer edge of a module row to secure the panel frame to the mounting rail.",
     "features": "Metal end-grip clamp with fastener; matched to module frame height and mounting rail."},
    {"id": 16, "name": "Bolt Nut Kit", "category": "Mounting Structures",
     "description": "A hardware kit containing compatible bolts, nuts and washers for assembling solar mounting components.",
     "features": "Corrosion-resistant fasteners; assorted hardware as specified by the mounting-system bill of materials."},
    {"id": 17, "name": "Foundation Bolt", "category": "Mounting Structures",
     "description": "An anchor bolt embedded or fixed into a concrete foundation to connect the solar support structure to its base.",
     "features": "Threaded anchor bolt with nut and washer; dimensions and embedment selected by structural design."},

    {"id": 18, "name": "DC Cable Red", "category": "Cables and Connectors",
     "description": "A red insulated solar DC cable commonly used to identify the positive conductor in a photovoltaic string circuit.",
     "features": "PV-rated cable; sunlight and weather resistant; conductor size and voltage rating must match system design."},
    {"id": 19, "name": "DC Cable Black", "category": "Cables and Connectors",
     "description": "A black insulated solar DC cable commonly used to identify the negative conductor in a photovoltaic string circuit.",
     "features": "PV-rated cable; sunlight and weather resistant; conductor size and voltage rating must match system design."},
    {"id": 20, "name": "AC Cable", "category": "Cables and Connectors",
     "description": "An alternating-current power cable used to connect the inverter output to the AC distribution system or grid interface.",
     "features": "Power cable with insulated conductors and protective outer sheath; rating selected for current, voltage and installation method."},
    {"id": 21, "name": "Earthing Cable", "category": "Cables and Connectors",
     "description": "A protective earthing conductor that bonds designated solar-system equipment to the earthing network.",
     "features": "Protective conductor; suitable insulation and cross-section as specified by electrical design and applicable standards."},
    {"id": 22, "name": "MC4 Male", "category": "Cables and Connectors",
     "description": "A male-type photovoltaic connector used to make a weather-resistant DC connection in compatible solar cable assemblies.",
     "features": "PV connector body with metal contact; use only with matching, manufacturer-compatible connector parts."},
    {"id": 23, "name": "MC4 Female", "category": "Cables and Connectors",
     "description": "A female-type photovoltaic connector used to mate with a compatible male PV connector in a solar DC circuit.",
     "features": "PV connector body with metal contact; use only with matching, manufacturer-compatible connector parts."},
    {"id": 24, "name": "Cable Tie", "category": "Cables and Connectors",
     "description": "A fastening tie used to bundle and secure solar cables neatly along approved cable routes and support points.",
     "features": "Locking strap; UV-resistant material recommended for outdoor use; selected to suit cable bundle size."},
    {"id": 25, "name": "Cable Tray", "category": "Cables and Connectors",
     "description": "A tray system used to route, support and organize electrical cables in a solar installation.",
     "features": "Metal or polymer tray sections with fittings; tray type, loading and corrosion protection selected for the site."},

    {"id": 26, "name": "Combiner Box", "category": "Boxes and Protection",
     "description": "An enclosure that combines multiple PV string outputs into a common DC output and may contain string-level protection and monitoring components.",
     "features": "Weather-rated enclosure; internal busbars and string protection as configured; cable entry and labeling provisions."},
    {"id": 27, "name": "DCDB Box", "category": "Boxes and Protection",
     "description": "A DC distribution box used to isolate, protect and distribute DC power between the PV array and inverter, according to system architecture.",
     "features": "Enclosure with specified DC switching and protection devices; voltage and current ratings must match the installation."},
    {"id": 28, "name": "ACDB Box", "category": "Boxes and Protection",
     "description": "An AC distribution box installed on the inverter AC side to provide switching, isolation and protective-device housing.",
     "features": "Enclosure with AC-rated protective and switching components; configuration depends on inverter and grid connection."},
    {"id": 29, "name": "SPD", "category": "Boxes and Protection",
     "description": "A surge protective device designed to limit transient overvoltage and divert surge current in a compatible solar electrical circuit.",
     "features": "DIN-rail protective module; DC or AC type selected for system voltage, protection level and installation location."},
    {"id": 30, "name": "DC MCB", "category": "Boxes and Protection",
     "description": "A DC miniature circuit breaker used for switching and overcurrent protection in appropriately designed direct-current circuits.",
     "features": "DC-rated breaker; pole count, voltage and current ratings must be selected for the circuit."},
    {"id": 31, "name": "DC Fuse", "category": "Boxes and Protection",
     "description": "A photovoltaic DC fuse designed to interrupt excessive current in a PV string or DC circuit when correctly selected.",
     "features": "PV fuse element and compatible holder; fuse class and rating selected from the system protection study."},
    {"id": 32, "name": "Isolator Switch", "category": "Boxes and Protection",
     "description": "A manually operated isolating switch used to disconnect a designated DC or AC section for safe maintenance when correctly rated.",
     "features": "Enclosed rotary or switch mechanism; pole count and voltage/current rating must match the circuit."},

    {"id": 33, "name": "Earthing Rod", "category": "Earthing and Safety",
     "description": "A conductive earth electrode installed in the ground as part of an electrical earthing system.",
     "features": "Copper-bonded, galvanized or other specified electrode; length and type selected from soil and earthing design."},
    {"id": 34, "name": "Lightning Arrester", "category": "Earthing and Safety",
     "description": "An air-terminal component used as part of a designed lightning protection system to provide a preferred strike attachment point.",
     "features": "Metal air terminal with mounting hardware; must be integrated with correctly designed down conductors and earth termination."},
    {"id": 35, "name": "Earthing Strip", "category": "Earthing and Safety",
     "description": "A flat conductive metal strip used to bond equipment and connect components within an earthing network.",
     "features": "Copper or galvanized steel strip; width and thickness selected according to the approved earthing design."},
    {"id": 36, "name": "Earth Pit Cover", "category": "Earthing and Safety",
     "description": "A protective cover fitted over an earth inspection pit to provide access for inspection while protecting the pit opening.",
     "features": "Durable inspection cover; suitable for the pit dimensions and expected outdoor or traffic conditions."},

    {"id": 37, "name": "Data Logger", "category": "Monitoring and Metering",
     "description": "A monitoring gateway that collects operating data from compatible inverters, meters and sensors and forwards it to a monitoring platform.",
     "features": "Communication interfaces depend on model; supports data collection and remote monitoring when compatible."},
    {"id": 38, "name": "WiFi Dongle", "category": "Monitoring and Metering",
     "description": "A wireless communication accessory that enables supported solar inverters or monitoring devices to connect to a Wi-Fi network.",
     "features": "Compact plug-in communication adapter; compatibility and network requirements are model-specific."},
    {"id": 39, "name": "Energy Meter", "category": "Monitoring and Metering",
     "description": "An electrical meter used to measure energy consumption or generation at a defined point in the solar installation.",
     "features": "Digital display and electrical measurement terminals; phase type, accuracy class and current range are model-specific."},
    {"id": 40, "name": "Net Meter", "category": "Monitoring and Metering",
     "description": "A bidirectional electricity meter used in approved grid-connected installations to record energy imported from and exported to the utility grid.",
     "features": "Import/export energy measurement; utility approval, meter specification and installation rules apply."},
    {"id": 41, "name": "CT Coil", "category": "Monitoring and Metering",
     "description": "A current transformer used to sense AC current for compatible energy meters, monitoring devices or protection systems.",
     "features": "Current-sensing transformer; ratio, accuracy and physical size must match the connected equipment."},

    {"id": 42, "name": "Cleaning Brush", "category": "Maintenance",
     "description": "A soft cleaning brush designed to remove loose dust and light debris from solar module surfaces without abrasive scrubbing.",
     "features": "Non-abrasive bristles and suitable handle; cleaning method must follow module manufacturer guidance."},
    {"id": 43, "name": "Cleaning Sprinkler", "category": "Maintenance",
     "description": "A water-sprinkling accessory used in a solar-panel cleaning arrangement to distribute water across module surfaces.",
     "features": "Spray nozzle or sprinkler assembly; water quality, pressure and cleaning method should suit the PV modules."},
    {"id": 44, "name": "Spare MC4 Kit", "category": "Maintenance",
     "description": "A spare photovoltaic connector kit for replacement or field maintenance of compatible solar DC cable connections.",
     "features": "Compatible connector pairs and accessories; connector brand and model must match the existing cable system."},
    {"id": 45, "name": "Tool Kit", "category": "Maintenance",
     "description": "A maintenance tool set containing suitable hand tools for routine solar installation inspection and service tasks.",
     "features": "Selected insulated and general-purpose tools; use tools with appropriate ratings for the specific task."},
]


def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def make_prompt(product):
    return f"""
Create a premium, photorealistic e-commerce product photograph of exactly one item:
{product['name']}.

Product context: {product['description']}
Visual details: {product['features']}

Requirements:
- Show only this specific product, not a collage and not a collection.
- The product must be large, centered, fully visible, and recognizable.
- Accurate industrial/electrical product photography, realistic materials,
  believable dimensions, clean professional studio lighting.
- Plain pure white seamless background, soft natural contact shadow.
- Front three-quarter view, sharp focus, high detail.
- No people, no hands, no packaging, no watermark, no logo, no brand name.
- Do not add labels, captions, diagrams, measurements or any text in the image.
- Square composition suitable for a professional solar equipment website.
""".strip()


def save_image(client, product, force=False):
    filename = f"{product['id']:02d}-{slugify(product['name'])}.jpg"
    path = IMAGE_DIR / filename

    if path.exists() and not force:
        print(f"[SKIP] {filename} already exists")
        return filename

    for attempt in range(1, RETRY_COUNT + 1):
        try:
            print(f"[{product['id']}/45] Generating: {product['name']} (attempt {attempt})")
            result = client.images.generate(
                model=MODEL,
                prompt=make_prompt(product),
                size=IMAGE_SIZE,
                quality=QUALITY,
                output_format=OUTPUT_FORMAT,
                n=1,
            )
            image_bytes = base64.b64decode(result.data[0].b64_json)
            path.write_bytes(image_bytes)
            print(f"[SAVED] {path}")
            return filename
        except Exception as exc:
            print(f"[ERROR] {product['name']}: {exc}")
            if attempt < RETRY_COUNT:
                time.sleep(WAIT_SECONDS * attempt)

    print(f"[FAILED] {product['name']} - will be listed in failed_items.json")
    return None


def write_catalog(generated):
    # JSON catalog
    (OUTPUT_DIR / "products.json").write_text(
        json.dumps(generated, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # CSV catalog
    with (OUTPUT_DIR / "products.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "name", "category", "description", "features", "image"]
        )
        writer.writeheader()
        writer.writerows(generated)

    # Responsive HTML preview/catalog
    cards = []
    for p in generated:
        img = f"images/{html.escape(p['image'])}" if p.get("image") else ""
        image_html = (
            f'<img src="{img}" alt="{html.escape(p["name"])}" loading="lazy">'
            if img else '<div class="missing">Image generation pending</div>'
        )
        cards.append(f"""
        <article class="card">
          {image_html}
          <div class="body">
            <small>{html.escape(p['category'])} · Product {p['id']}</small>
            <h2>{html.escape(p['name'])}</h2>
            <p>{html.escape(p['description'])}</p>
            <p class="features"><b>Key features:</b> {html.escape(p['features'])}</p>
          </div>
        </article>""")

    page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Solar Products Catalogue</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f4f6f8;color:#172033;
font:16px/1.55 Arial,sans-serif}.header{background:#0a1f44;color:white;
padding:28px 18px;text-align:center;border-bottom:4px solid #c9a24b}
.header h1{margin:0 0 6px}.wrap{max-width:1200px;margin:24px auto;padding:0 14px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
.card{background:white;border:1px solid #e2e6ec;border-radius:12px;overflow:hidden}
.card img{width:100%;aspect-ratio:1/1;object-fit:contain;background:white}
.body{padding:16px}.body small{color:#8b6b22}.body h2{font-size:20px;margin:7px 0}
.body p{margin:8px 0}.features{color:#4c5668}.missing{height:260px;
display:grid;place-items:center;background:#eee;color:#777}
</style></head><body>
<header class="header"><h1>Solar Products Catalogue</h1>
<p>Product range · Individual product images and descriptions</p></header>
<main class="wrap"><section class="grid">""" + "\n".join(cards) + """
</section></main></body></html>"""
    (OUTPUT_DIR / "index.html").write_text(page, encoding="utf-8")


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY not found.")
        print("Set it first: export OPENAI_API_KEY='your_api_key'")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    client = OpenAI(api_key=api_key)

    generated = []
    failed = []

    print(f"Starting {len(PRODUCTS)} product images using {MODEL} / {QUALITY} quality.")
    print("Existing images are skipped; run again to resume after interruption.\n")

    for product in PRODUCTS:
        image_name = save_image(client, product)
        item = dict(product)
        item["image"] = image_name
        generated.append(item)
        if image_name is None:
            failed.append({"id": product["id"], "name": product["name"]})

        # Save progress after every product so an interruption does not lose the catalog.
        write_catalog(generated)
        (OUTPUT_DIR / "failed_items.json").write_text(
            json.dumps(failed, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    print("\n========== COMPLETE ==========")
    print(f"Products: {len(PRODUCTS)}")
    print(f"Images saved: {len([x for x in generated if x['image']])}")
    print(f"Failed: {len(failed)}")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")
    print(f"Open catalog: {(OUTPUT_DIR / 'index.html').resolve()}")


if __name__ == "__main__":
    main()
