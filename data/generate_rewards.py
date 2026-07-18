import pandas as pd
import random

random.seed(42)

transactions = pd.read_csv("transactions.csv")
cards = pd.read_csv("cards.csv")

# Merge to get customer_id
df = transactions.merge(
    cards[["card_id", "customer_id"]],
    on="card_id",
    how="left"
)

# Only successful transactions earn rewards
df = df[df["status"] == "Success"]

reward_types = [
    "Cashback",
    "Travel",
    "Dining",
    "Shopping"
]

rewards = []

reward_id = 1

for _, row in df.iterrows():

    points = int(row["amount"] // 100)

    if points == 0:
        continue

    rewards.append({
        "reward_id": reward_id,
        "customer_id": row["customer_id"],
        "points_earned": points,
        "points_redeemed": random.randint(0, points),
        "reward_type": random.choice(reward_types),
        "reward_date": row["transaction_time"][:10]
    })

    reward_id += 1

rewards_df = pd.DataFrame(rewards)

rewards_df.to_csv("rewards.csv", index=False)

print(rewards_df.head())

print(f"\nGenerated {len(rewards_df)} rewards.")