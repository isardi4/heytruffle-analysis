#!/usr/bin/env python3
"""Normaliza un CSV exportado de Apollo (o fuente equivalente) a data/locales.csv."""
import argparse
import csv
import hashlib
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "data/locales.csv"


def norm(value):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def make_id(prefix, *parts):
    raw = "\x1f".join(norm(part) for part in parts)
    return f"{prefix}_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:12]}"


def google_maps_url(name, address, city, state):
    """Build a human-facing Maps search link; does not call or store Maps data."""
    query = ", ".join(part for part in (name, address, city, state) if part)
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(query)


def import_rows(input_path, output_path, name_col, address_col, city_col, state_col, phone_col, source):
    with input_path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or name_col not in reader.fieldnames:
            raise ValueError(f"No existe la columna de nombre {name_col!r} en el CSV")
        source_rows = list(reader)
        columns = list(reader.fieldnames)
    extras = ["company_id", "location_id", "company_name", "location_label", "city", "state", "phone", "origin", "google_maps_url"]
    rows, seen = [], set()
    for row in source_rows:
        name = (row.get(name_col) or "").strip()
        if not name:
            continue
        address, city, state, phone = tuple((row.get(c, "") or "").strip()
                                            for c in (address_col, city_col, state_col, phone_col))
        company_id = make_id("cmp", name)
        source_key = row.get("Apollo Account Id") or row.get("Apollo Record Id") or ""
        location_id = make_id("loc", company_id, source_key or address, city, state)
        if location_id in seen:
            continue
        seen.add(location_id)
        location_label = " · ".join(v for v in (address, city, state) if v)
        rows.append({**row, "company_id": company_id, "location_id": location_id,
                     "company_name": name, "location_label": location_label or name,
                     "city": city, "state": state, "phone": phone, "origin": source,
                     "google_maps_url": google_maps_url(name, address, city, state)})
    if not rows:
        raise ValueError("No se encontraron filas con nombre de empresa")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fields = columns + [name for name in extras if name not in columns]
    with output_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Generado {output_path}: {len(rows)} locales de {len({r['company_id'] for r in rows})} empresas")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Export CSV (Apollo u otra fuente)")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--name-column", default="Company Name")
    parser.add_argument("--address-column", default="Company Street")
    parser.add_argument("--city-column", default="Company City")
    parser.add_argument("--state-column", default="Company State")
    parser.add_argument("--phone-column", default="Company Phone")
    parser.add_argument("--source", default="apollo_export", help="Etiqueta de origen")
    args = parser.parse_args()
    import_rows(args.input, args.output, args.name_column, args.address_column,
                args.city_column, args.state_column, args.phone_column, args.source)


if __name__ == "__main__":
    try:
        main()
    except (OSError, csv.Error, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
