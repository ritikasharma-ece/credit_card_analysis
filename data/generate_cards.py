import pandas as pd
import random
from faker import Faker
from datetime import timedelta

fake = Faker("en_IN")
random.seed(42)

customers = pd.read_csv("customers.csv")

cards = []

card_id = 1

# Credit limits based on customer segment
credit_limits = {
    "Standard": (50000, 150000),
    "Silver": (100000, 300000),
    "Gold": (300000, 800000),
    "Platinum": (800000, 2000000)
}

# Card types allowed for each segment
card_options = {
    "Standard": ["Classic"],
    "Silver": ["Classic", "Gold"],
    "Gold": ["Gold", "Platinum"],
    "Platinum": ["Platinum", "Business"]
}

for _, customer in customers.iterrows():

    # Each customer gets 1-3 cards
    num_cards = random.randint(1, 3)

    for _ in range(num_cards):

        segment = customer["customer_segment"]

        card_type = random.choice(card_options[segment])

        low, high = credit_limits[segment]

        credit_limit = random.randint(low, high)

        # Available limit is between 30% and 100% of credit limit
        available_limit = random.randint(
            int(credit_limit * 0.30),
            credit_limit
        )

        import pandas as pd

        join_date = pd.to_datetime(customer["join_date"]).date()

        issue_date = fake.date_between(
            start_date=join_date,
            end_date="today"
)
        

        expiry_date = issue_date + timedelta(days=365 * 5)

        cards.append({
            "card_id": card_id,
            "customer_id": customer["customer_id"],
            "card_type": card_type,
            "credit_limit": credit_limit,
            "available_limit": available_limit,
            "issue_date": issue_date,
            "expiry_date": expiry_date
        })

        card_id += 1

cards_df = pd.DataFrame(cards)

cards_df.to_csv("cards.csv", index=False)

print(cards_df.head())

print(f"\nGenerated {len(cards_df)} cards.")