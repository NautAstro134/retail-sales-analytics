"""Generate a deterministic demo dataset compatible with the retail dbt project."""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20261028
ORDER_COUNT = 1000
START_DATE = date(2023, 1, 2)
END_DATE = date(2024, 12, 31)

REGIONS = ["North", "South", "East", "West"]
REPS = ["Alice", "Bob", "Carlos", "Diana", "Eve", "Frank"]
PRODUCTS = {
    "Desk": (250.00, 1800.00),
    "Laptop": (500.00, 2200.00),
    "Chair": (80.00, 700.00),
    "Headset": (25.00, 300.00),
    "Mouse": (10.00, 150.00),
    "Webcam": (20.00, 250.00),
    "Keyboard": (20.00, 220.00),
    "Monitor": (100.00, 900.00),
}
DISCOUNTS = [0, 0.05, 0.10, 0.15, 0.20]

rng = random.Random(SEED)
output_path = Path("data/sales_demo.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
date_span = (END_DATE - START_DATE).days

with output_path.open("w", newline="", encoding="utf-8") as output_file:
    writer = csv.writer(output_file)
    writer.writerow([
        "order_id", "order_date", "rep", "region", "product",
        "quantity", "unit_price", "discount"
    ])

    for order_number in range(1, ORDER_COUNT + 1):
        product = rng.choice(list(PRODUCTS))
        low_price, high_price = PRODUCTS[product]
        writer.writerow([
            f"ORD-{order_number:04d}",
            START_DATE + timedelta(days=rng.randint(0, date_span)),
            rng.choice(REPS),
            rng.choice(REGIONS),
            product,
            rng.randint(1, 20),
            f"{rng.uniform(low_price, high_price):.2f}",
            rng.choice(DISCOUNTS),
        ])

print(f"Created {ORDER_COUNT:,} demo orders at {output_path.resolve()}")
