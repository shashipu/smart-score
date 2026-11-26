"""
Smart Score: ranking of outpatient clinics.

Reads data/clinics.csv (70 clinics surveyed in the field study), applies
min-max normalization (cost criteria inverted), computes the weighted
Smart Score and writes the ranking to outputs/smart_score_ranking.csv.

Usage:  python smart_score.py
"""
import csv
import os

# Criterion: (column name, weight, type)
CRITERIA = [
    ("rating",        0.25, "benefit"),
    ("distance_km",   0.20, "cost"),
    ("fee_inr",       0.15, "cost"),
    ("affordability", 0.20, "benefit"),
    ("walkability",   0.20, "benefit"),
]

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "clinics.csv")
OUT = os.path.join(HERE, "outputs", "smart_score_ranking.csv")


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def smart_score(rows):
    mins, maxs = {}, {}
    for col, _, _ in CRITERIA:
        vals = [float(r[col]) for r in rows]
        mins[col], maxs[col] = min(vals), max(vals)

    results = []
    for r in rows:
        score = 0.0
        for col, w, kind in CRITERIA:
            x = (float(r[col]) - mins[col]) / (maxs[col] - mins[col])
            if kind == "cost":
                x = 1 - x
            score += w * x
        results.append((r["clinic_id"], round(score, 4)))

    # Sort descending; equal scores share the same rank
    results.sort(key=lambda t: (-t[1], t[0]))
    ranked, prev, rank = [], None, 0
    for i, (cid, s) in enumerate(results, start=1):
        if s != prev:
            rank, prev = i, s
        ranked.append((rank, cid, s))
    return ranked


def main():
    ranked = smart_score(load(DATA))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "clinic_id", "smart_score"])
        w.writerows(ranked)
    print(f"Ranked {len(ranked)} clinics -> {OUT}")
    for rank, cid, s in ranked[:10]:
        print(f"{rank:>3}  {cid}  {s:.4f}")


if __name__ == "__main__":
    main()
