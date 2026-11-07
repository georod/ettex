#!/usr/bin/env python3
"""Rewrite the image_url column of the POI CSV so it points to Cloudinary.

Usage:
    python3 update_image_urls.py data/pois.csv data/pois_cloudinary.csv
    python3 update_image_urls.py data/pois.csv data/pois_cloudinary.csv --check   # also test 5 links

Requires: pandas (pip install pandas)
"""
import sys
import urllib.request
from os.path import basename, splitext
from urllib.parse import urlparse, quote

import pandas as pd

CLOUD_NAME = "zgpzyatq"
FOLDER = ""                 # public ID prefix; set to "" if your public IDs have no folder; "etvx/pois" 
TRANSFORM = "w_600,f_auto,q_auto"    # 600 px wide, best format (WebP/AVIF), auto quality


def cloudinary_url(old_url: str) -> str:
    """http://old-site/.../004.jpg -> https://res.cloudinary.com/<cloud>/image/upload/<transform>/<folder>/004"""
    if not old_url.strip():
        return ""
    stem = splitext(basename(urlparse(old_url.strip()).path))[0]   # '004'
    public_id = f"{FOLDER}/{stem}" if FOLDER else stem
    return f"https://res.cloudinary.com/{CLOUD_NAME}/image/upload/{TRANSFORM}/{quote(public_id)}"


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    src, dst = sys.argv[1], sys.argv[2]

    # dtype=str keeps values such as '004' intact; keep_default_na avoids turning text into NaN
    df = pd.read_csv(src, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    if "image_url" not in df.columns:
        sys.exit("No 'image_url' column found. Columns: " + ", ".join(df.columns))

    df["image_url"] = df["image_url"].map(cloudinary_url)
    df.to_csv(dst, index=False, encoding="utf-8")
    n = (df["image_url"] != "").sum()
    print(f"Rewrote {n} of {len(df)} rows -> {dst}")
    print("Example:", next((u for u in df["image_url"] if u), "(none)"))

    if "--check" in sys.argv:
        print("\nChecking the first 5 links...")
        for u in [u for u in df["image_url"] if u][:5]:
            try:
                req = urllib.request.Request(u, method="HEAD")
                with urllib.request.urlopen(req, timeout=15) as r:
                    print(r.status, u)
            except Exception as e:
                print("FAILED", u, "->", e)


if __name__ == "__main__":
    main()
