import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# Load Data
# -----------------------------
cards = pd.read_csv("cards.csv")
merchants = pd.read_csv("merchants.csv")

NUM_TRANSACTIONS = 500000

# -----------------------------
# Amount ranges by merchant category
# -----------------------------
amount_ranges = {
    "Grocery": (100, 5000),
    "Electronics": (5000, 150000),
    "Restaurant": (200, 6000),
    "Food Delivery": (150, 2500),
    "Fuel": (500, 4000),
    "Travel": (3000, 50000),
    "Transport": (100, 3000),
    "Hotel": (3000, 50000),
    "Pharmacy": (100, 5000),
    "Fashion": (500, 25000),
    "Entertainment": (200, 6000),
    "Utilities": (300, 12000)
}

status_choices = [
    "Success",
    "Failed",
    "Declined",
    "Refund"
]

status_weights = [
    0.94,
    0.02,
    0.03,
    0.01
]

payment_methods = [
    "Chip",
    "Tap",
    "Swipe",
    "Online"
]

transactions = []

# -----------------------------
# Transaction Generation
# -----------------------------
for transaction_id in range(1, NUM_TRANSACTIONS + 1):

    card = cards.sample(1).iloc[0]

    merchant = merchants.sample(1).iloc[0]

    category = merchant["category"]

    low, high = amount_ranges[category]

    amount = round(random.uniform(low, high), 2)

    status = random.choices(
        status_choices,
        weights=status_weights,
        k=1
    )[0]

    payment_method = random.choice(payment_methods)

    transaction_time = fake.date_time_between(
        start_date="-3y",
        end_date="now"
    )

    transactions.append({
        "transaction_id": transaction_id,
        "card_id": int(card["card_id"]),
        "merchant_id": int(merchant["merchant_id"]),
        "transaction_time": transaction_time,
        "amount": amount,
        "status": status,
        "payment_method": payment_method
    })

    if transaction_id % 10000 == 0:
        print(f"{transaction_id} transactions generated...")

transactions_df = pd.DataFrame(transactions)

transactions_df.to_csv(
    "transactions.csv",
    index=False
)

print(transactions_df.head())

print(f"\nGenerated {len(transactions_df)} transactions.")