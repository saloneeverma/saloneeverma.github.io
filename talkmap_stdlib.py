"""Regenerate talkmap/org-locations.js from the .md files in _talks/.

Standalone replacement for talkmap.py: uses only the standard library, so it
needs no frontmatter/getorg/geopy install. Geocodes via the public Nominatim
API and rewrites only org-locations.js; talkmap/map.html and
talkmap/leaflet_dist/ are left alone.
"""

import glob
import json
import os
import sys
import time
import urllib.parse
import urllib.request

REPO = sys.argv[1] if len(sys.argv) > 1 else "."
UA = "saloneeverma.github.io talkmap generator"
NOMINATIM = "https://nominatim.openstreetmap.org/search"


def parse_front_matter(path):
    """Return the YAML front matter of a Markdown file as a flat dict.

    Only handles the `key: "value"` lines this template uses, which is all the
    talkmap needs (title, venue, location).
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.lstrip().startswith("---"):
        return {}
    body = text.lstrip()[3:]
    end = body.find("\n---")
    if end == -1:
        return {}
    data = {}
    for line in body[:end].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key.strip()] = value
    return data


def geocode(location):
    """Look up one location string, returning (lat, lon) or None."""
    url = f"{NOMINATIM}?{urllib.parse.urlencode({'q': location, 'format': 'json', 'limit': 1})}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=15) as resp:
        results = json.load(resp)
    if not results:
        return None
    return float(results[0]["lat"]), float(results[0]["lon"])


points = []
for path in sorted(glob.glob(os.path.join(REPO, "_talks", "*.md"))):
    data = parse_front_matter(path)
    location = data.get("location", "").strip()
    if not location:
        print(f"skip (no location): {os.path.basename(path)}")
        continue

    title = data.get("title", "").strip()
    venue = data.get("venue", "").strip()
    description = f"{title}<br />{venue}; {location}"

    try:
        coords = geocode(location)
    except Exception as ex:
        print(f"ERROR: geocode failed for {location!r}: {ex}")
        continue
    if coords is None:
        print(f"ERROR: no match for {location!r}")
        continue

    points.append([description, coords[0], coords[1]])
    print(f"ok: {location} -> {coords[0]}, {coords[1]}  ({os.path.basename(path)})")
    time.sleep(1.1)  # Nominatim asks for no more than 1 request/second

if not points:
    sys.exit("No talks with a usable location field; refusing to write an empty map.")

out = os.path.join(REPO, "talkmap", "org-locations.js")
with open(out, "w", encoding="utf-8") as fh:
    fh.write("var addressPoints = " + json.dumps(points, indent=2, ensure_ascii=False) + ";")
print(f"\nwrote {len(points)} point(s) to {out}")
