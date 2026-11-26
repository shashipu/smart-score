# Smart Score: Ranking of Outpatient Clinics

Dataset and analysis code for the paper **"Smart Score"** (manuscript PAPER023267).

## Contents

| File | Description |
|---|---|
| `data/clinics.csv` | Raw dataset of the 70 surveyed clinics (Table 3 of the paper) |
| `smart_score.py` | Computes the Smart Score and ranks the clinics |
| `outputs/smart_score_ranking.csv` | Smart Score and rank of all 70 clinics (Table 8 of the paper) |

## Dataset columns

| Column | Description | Unit / scale | Criterion type | Weight |
|---|---|---|---|---|
| `clinic_id` | Anonymised clinic ID (C001–C070) | – | – | – |
| `rating` | Average online patient rating | 1–5 | Benefit | 0.25 |
| `distance_km` | Walking distance from the user reference point | km | Cost | 0.20 |
| `fee_inr` | Fee for one outpatient consultation | ₹ | Cost | 0.15 |
| `affordability` | Overall affordability of the clinic | 1–10 | Benefit | 0.20 |
| `walkability` | Ease of reaching the clinic on foot | 1–10 | Benefit | 0.20 |

## Method

Each criterion is min-max normalized; for cost criteria (distance, fee) the value is inverted (1 − x′).
The Smart Score is the weighted sum of the normalized values. Equal scores share the same rank.

## How to run

Requires Python 3 (no extra packages).

```bash
python smart_score.py
```

## Data collection and ethics

Clinic data were taken from publicly available listings and on-site observation of publicly
accessible information. No personal or health data of patients were collected.

## Citation

If you use this dataset, please cite the paper (citation details will be added after publication).
