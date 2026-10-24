"""Download the Crypto Fear & Greed Index (alternative.me) and write it as a
Pine Seeds CSV: data/FNG.csv  ->  rows of: YYYYMMDDT,open,high,low,close,volume
Data source: https://alternative.me/crypto/fear-and-greed-index/ (credit them if you share this)
"""
import csv, json, urllib.request
from datetime import datetime, timezone

URL = "https://api.alternative.me/fng/?limit=0&format=json"
with urllib.request.urlopen(URL, timeout=30) as r:
    rows = json.load(r)["data"]

by_day = {}
for row in rows:
    day = datetime.fromtimestamp(int(row["timestamp"]), tz=timezone.utc).strftime("%Y%m%dT")
    by_day[day] = int(row["value"])

with open("data.csv", "w", newline="") as f:
    w = csv.writer(f)
    for day in sorted(by_day):
        v = by_day[day]
        w.writerow([day, v, v, v, v, 0])

print(f"Wrote {len(by_day)} rows, latest {max(by_day)} = {by_day[max(by_day)]}")
