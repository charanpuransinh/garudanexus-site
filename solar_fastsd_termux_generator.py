#!/usr/bin/env python3
"""
Solar Product Catalog Generator for FastSD CPU (Android + Termux / Ubuntu PRoot)

This script does NOT use OpenAI API or any paid image API.
It sends prompts to a locally running FastSD CPU server at http://127.0.0.1:8000.
The FastSD model must be installed separately and running before this script starts.
"""

import base64
import csv
import html
import json
import re
import time
from pathlib import Path

try:
    import requests
except ImportError:
    raise SystemExit("Missing requests. Install it with: python -m pip install requests")

API_URL = "http://127.0.0.1:8000"
OUTPUT = Path.home() / "solar_product_catalog"
IMAGES = OUTPUT / "images"
IMAGE_SIZE_NOTE = "Use FastSD's configured model resolution (start with 512x512)."
RETRIES = 2
PAUSE_SECONDS = 2

PRODUCTS = [
(9,"Rooftop Structure","Mounting Structures","A rooftop mounting framework that supports and secures solar PV modules on a building roof. Design depends on roof type, wind load, module layout and structural assessment.","Metal rails, brackets and support members; corrosion-resistant finish; roof-specific mounting arrangement."),
(10,"Ground Structure","Mounting Structures","A ground-mounted support framework that holds solar PV modules at a planned tilt and orientation. Foundation design depends on soil conditions, wind load and engineering calculations.","Metal posts, beams and module rails; fixed-tilt arrangement; site-specific foundation interface."),
(11,"Carport Structure","Mounting Structures","A canopy-style solar mounting structure installed above a parking area, supporting PV modules while providing sheltered parking below.","Canopy frame, columns and module supports; parking clearance; engineered drainage and foundations."),
(12,"Rail","Mounting Structures","A mounting rail that forms the support interface between solar modules and the underlying mounting structure.","Extruded metal rail profile; module mounting channel; compatible with specified clamps and brackets."),
(13,"Purlin","Mounting Structures","A structural cross-member used to support rails or solar mounting components and transfer loads to the primary structure.","Metal structural section; load-transfer member; profile and thickness selected by engineering design."),
(14,"Mid Clamp","Mounting Structures","A solar module mid clamp fitted between two adjacent panels to secure their frame edges to a mounting rail.","Compact metal clamp with bolt; matched to module-frame thickness and rail system."),
(15,"End Clamp","Mounting Structures","A solar module end clamp fitted at the outer edge of a module row to secure the panel frame to a mounting rail.","Metal end-grip clamp with fastener; matched to module frame height and mounting rail."),
(16,"Bolt Nut Kit","Mounting Structures","A hardware kit containing compatible bolts, nuts and washers for assembling solar mounting components.","Corrosion-resistant fasteners; assorted hardware according to the mounting-system bill of materials."),
(17,"Foundation Bolt","Mounting Structures","An anchor bolt embedded or fixed into a concrete foundation to connect a solar support structure to its base.","Threaded anchor bolt with nut and washer; dimensions and embedment selected by structural design."),
(18,"DC Cable Red","Cables and Connectors","A red insulated solar DC cable commonly used to identify the positive conductor in a photovoltaic string circuit.","PV-rated cable; sunlight and weather resistant; conductor size and voltage rating depend on system design."),
(19,"DC Cable Black","Cables and Connectors","A black insulated solar DC cable commonly used to identify the negative conductor in a photovoltaic string circuit.","PV-rated cable; sunlight and weather resistant; conductor size and voltage rating depend on system design."),
(20,"AC Cable","Cables and Connectors","An alternating-current power cable used to connect an inverter output to the AC distribution system or grid interface.","Insulated power conductors with protective outer sheath; rating selected for current, voltage and installation method."),
(21,"Earthing Cable","Cables and Connectors","A protective earthing conductor that bonds designated solar-system equipment to the earthing network.","Protective conductor; insulation and cross-section selected according to electrical design and applicable standards."),
(22,"MC4 Male","Cables and Connectors","A male-type photovoltaic connector used to make a weather-resistant DC connection in compatible solar cable assemblies.","PV connector body with metal contact; must be paired with a manufacturer-compatible connector."),
(23,"MC4 Female","Cables and Connectors","A female-type photovoltaic connector used to mate with a compatible male PV connector in a solar DC circuit.","PV connector body with metal contact; must be paired with a manufacturer-compatible connector."),
(24,"Cable Tie","Cables and Connectors","A fastening tie used to bundle and secure solar cables neatly along approved cable routes and support points.","Locking strap; UV-resistant material recommended for outdoor use; size matched to cable bundle."),
(25,"Cable Tray","Cables and Connectors","A tray system used to route, support and organize electrical cables in a solar installation.","Metal or polymer tray sections with fittings; tray type and loading selected for the site."),
(26,"Combiner Box","Boxes and Protection","An enclosure that combines multiple PV string outputs into a common DC output and may contain string-level protection and monitoring components.","Weather-rated enclosure; internal busbars and string protection as configured; cable-entry and labeling provisions."),
(27,"DCDB Box","Boxes and Protection","A DC distribution box used to isolate, protect and distribute DC power between the PV array and inverter, according to system architecture.","Enclosure with specified DC switching and protection devices; voltage and current ratings must match the installation."),
(28,"ACDB Box","Boxes and Protection","An AC distribution box installed on the inverter AC side to provide switching, isolation and protective-device housing.","Enclosure with AC-rated protective and switching components; configuration depends on inverter and grid connection."),
(29,"SPD","Boxes and Protection","A surge protective device designed to limit transient overvoltage and divert surge current in a compatible solar electrical circuit.","DIN-rail protective module; DC or AC type selected for system voltage and installation location."),
(30,"DC MCB","Boxes and Protection","A DC miniature circuit breaker used for switching and overcurrent protection in appropriately designed direct-current circuits.","DC-rated breaker; pole count, voltage and current ratings selected for the circuit."),
(31,"DC Fuse","Boxes and Protection","A photovoltaic DC fuse designed to interrupt excessive current in a PV string or DC circuit when correctly selected.","PV fuse element and compatible holder; fuse class and rating selected from the system protection study."),
(32,"Isolator Switch","Boxes and Protection","A manually operated isolating switch used to disconnect a designated DC or AC section for maintenance when correctly rated.","Enclosed rotary or switch mechanism; pole count and voltage/current rating matched to the circuit."),
(33,"Earthing Rod","Earthing and Safety","A conductive earth electrode installed in the ground as part of an electrical earthing system.","Copper-bonded, galvanized or other specified electrode; type and length selected from soil and earthing design."),
(34,"Lightning Arrester","Earthing and Safety","An air-terminal component used as part of a designed lightning protection system to provide a preferred strike attachment point.","Metal air terminal with mounting hardware; integrated with designed down conductors and earth termination."),
(35,"Earthing Strip","Earthing and Safety","A flat conductive metal strip used to bond equipment and connect components within an earthing network.","Copper or galvanized steel strip; width and thickness selected according to approved earthing design."),
(36,"Earth Pit Cover","Earthing and Safety","A protective cover fitted over an earth inspection pit to provide access for inspection while protecting the pit opening.","Durable inspection cover; dimensions and load rating suitable for the earth pit and installation location."),
(37,"Data Logger","Monitoring and Metering","A monitoring gateway that collects operating data from compatible inverters, meters and sensors and forwards it to a monitoring platform.","Communication interfaces depend on model; data collection and remote monitoring when compatible."),
(38,"WiFi Dongle","Monitoring and Metering","A wireless communication accessory that enables supported solar inverters or monitoring devices to connect to a Wi-Fi network.","Compact plug-in communication adapter; compatibility and network requirements are model-specific."),
(39,"Energy Meter","Monitoring and Metering","An electrical meter used to measure energy consumption or generation at a defined point in a solar installation.","Digital display and electrical measurement terminals; phase type, accuracy class and current range are model-specific."),
(40,"Net Meter","Monitoring and Metering","A bidirectional electricity meter used in approved grid-connected installations to record energy imported from and exported to the utility grid.","Import/export energy measurement; utility approval, meter specification and installation rules apply."),
(41,"CT Coil","Monitoring and Metering","A current transformer used to sense AC current for compatible energy meters, monitoring devices or protection systems.","Current-sensing transformer; ratio, accuracy and physical size must match connected equipment."),
(42,"Cleaning Brush","Maintenance","A soft cleaning brush designed to remove loose dust and light debris from solar module surfaces without abrasive scrubbing.","Non-abrasive bristles and suitable handle; cleaning method follows module manufacturer guidance."),
(43,"Cleaning Sprinkler","Maintenance","A water-sprinkling accessory used in a solar-panel cleaning arrangement to distribute water across module surfaces.","Spray nozzle or sprinkler assembly; water quality and pressure suitable for PV module cleaning."),
(44,"Spare MC4 Kit","Maintenance","A spare photovoltaic connector kit for replacement or field maintenance of compatible solar DC cable connections.","Compatible connector pairs and accessories; connector brand and model must match the existing cable system."),
(45,"Tool Kit","Maintenance","A maintenance tool set containing suitable hand tools for routine solar installation inspection and service tasks.","Selected insulated and general-purpose tools; use tools with appropriate ratings for each task."),
]

def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def make_prompt(item):
    number, name, category, description, features = item
    return (
        f"Photorealistic professional e-commerce studio product photograph of exactly one "
        f"{name}, a solar photovoltaic installation component. {description} "
        f"Visual details: {features} "
        "Show the complete single product, centered, large, isolated on a pure white seamless "
        "background with a soft realistic contact shadow. Front three-quarter product view, "
        "accurate industrial materials, clean neutral studio lighting, sharp focus, realistic "
        "manufacturing detail. No people, no hands, no packaging, no logo, no watermark, "
        "no labels, no writing, no collage, no extra products. Square product image."
    )

def find_image_payload(obj):
    """Handle common FastSD API response shapes without assuming one exact key."""
    if isinstance(obj, dict):
        for key in ("image", "image_base64", "image_data", "result", "output"):
            value = obj.get(key)
            if isinstance(value, str) and len(value) > 500:
                return value
            found = find_image_payload(value)
            if found:
                return found
        for value in obj.values():
            found = find_image_payload(value)
            if found:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = find_image_payload(value)
            if found:
                return found
    elif isinstance(obj, str) and len(obj) > 500:
        if obj.startswith("data:image"):
            return obj.split(",", 1)[1]
        # Accept raw base64-looking strings.
        if re.fullmatch(r"[A-Za-z0-9+/=\s]+", obj):
            return obj
    return None

def request_image(prompt):
    # FastSD README documents POST /api/generate and use_openvino.
    # Keep OpenVINO disabled on an 8 GB Android phone.
    response = requests.post(
        f"{API_URL}/api/generate",
        json={"prompt": prompt, "use_openvino": False},
        timeout=1800,
    )
    response.raise_for_status()
    payload = find_image_payload(response.json())
    if not payload:
        raise RuntimeError(
            "FastSD response did not contain a recognizable base64 image. "
            "Check the FastSD API response at http://127.0.0.1:8000/api/docs"
        )
    payload = payload.strip()
    if payload.startswith("data:image") and "," in payload:
        payload = payload.split(",", 1)[1]
    return base64.b64decode(payload)

def write_catalog(rows):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "products.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    with (OUTPUT / "products.csv").open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "name", "category", "description", "features", "image"
        ])
        writer.writeheader()
        writer.writerows(rows)

    cards = []
    for p in rows:
        img = f"images/{html.escape(p['image'])}" if p.get("image") else ""
        image_html = (
            f'<img src="{img}" alt="{html.escape(p["name"])}" loading="lazy">'
            if img else '<div class="missing">Image pending</div>'
        )
        cards.append(
            f'<article><div class="photo">{image_html}</div><section>'
            f'<small>{html.escape(p["category"])} · Product {p["id"]}</small>'
            f'<h2>{html.escape(p["name"])}</h2>'
            f'<p>{html.escape(p["description"])}</p>'
            f'<p><b>Key features:</b> {html.escape(p["features"])}</p>'
            f'</section></article>'
        )
    page = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solar Products Catalogue</title><style>
*{box-sizing:border-box}body{margin:0;background:#f3f5f7;color:#172033;font:16px/1.55 Arial}
header{background:#0a1f44;color:#fff;text-align:center;padding:28px 14px;border-bottom:4px solid #c9a24b}
main{max-width:1200px;margin:24px auto;padding:0 14px;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}
article{background:#fff;border:1px solid #e0e4e9;border-radius:12px;overflow:hidden}
.photo img{width:100%;aspect-ratio:1;object-fit:contain;background:#fff}
section{padding:15px}small{color:#947327}h2{font-size:20px;margin:6px 0}p{margin:8px 0}
.missing{height:240px;display:grid;place-items:center;background:#eee;color:#777}
</style></head><body><header><h1>Solar Products Catalogue</h1>
<p>Individual product images and product information</p></header><main>""" + "".join(cards) + "</main></body></html>"
    (OUTPUT / "index.html").write_text(page, encoding="utf-8")

def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("FastSD CPU local image generation — no paid API.")
    print("Checking local FastSD server:", API_URL)
    try:
        info = requests.get(f"{API_URL}/api/info", timeout=10)
        info.raise_for_status()
    except Exception as exc:
        raise SystemExit(
            "\nFastSD server is not reachable.\n"
            "Start it in the FastSD folder with: source env/bin/activate && python src/app.py --api\n"
            f"Details: {exc}"
        )

    rows, failed = [], []
    for number, name, category, description, features in PRODUCTS:
        filename = f"{number:02d}-{slug(name)}.jpg"
        path = IMAGES / filename
        print(f"\n[{number}/45] {name}")
        if path.exists() and path.stat().st_size > 1000:
            print("Already exists — skipping.")
        else:
            success = False
            for attempt in range(1, RETRIES + 1):
                try:
                    print(f"Generating image (attempt {attempt}/{RETRIES})...")
                    path.write_bytes(request_image(make_prompt(
                        (number, name, category, description, features)
                    )))
                    print("Saved:", path)
                    success = True
                    break
                except Exception as exc:
                    print("Generation error:", exc)
                    time.sleep(PAUSE_SECONDS * attempt)
            if not success:
                failed.append({"id": number, "name": name, "error": "See terminal output"})
        rows.append({
            "id": number, "name": name, "category": category,
            "description": description, "features": features,
            "image": filename if path.exists() else ""
        })
        write_catalog(rows)
        (OUTPUT / "failed_items.json").write_text(
            json.dumps(failed, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    print("\nFINISHED")
    print("Images present:", sum(1 for r in rows if r["image"]))
    print("Failed:", len(failed))
    print("Catalog:", OUTPUT / "index.html")
    print("CSV:", OUTPUT / "products.csv")
    print("JSON:", OUTPUT / "products.json")

if __name__ == "__main__":
    main()
