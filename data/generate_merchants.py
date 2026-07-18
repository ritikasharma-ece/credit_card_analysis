import pandas as pd
import random

random.seed(42)

NUM_MERCHANTS = 500

merchant_categories = {
    "Grocery": [
        "DMart", "Reliance Fresh", "Big Bazaar", "More", "Spencer's"
    ],
    "Electronics": [
        "Amazon", "Flipkart", "Croma", "Reliance Digital", "Vijay Sales"
    ],
    "Restaurant": [
        "Domino's", "Pizza Hut", "McDonald's", "Burger King", "KFC"
    ],
    "Food Delivery": [
        "Swiggy", "Zomato"
    ],
    "Fuel": [
        "Indian Oil", "HP", "BPCL", "Shell"
    ],
    "Travel": [
        "IRCTC", "MakeMyTrip", "Goibibo", "Yatra"
    ],
    "Transport": [
        "Uber", "Ola"
    ],
    "Hotel": [
        "Taj Hotels", "OYO", "Marriott", "Radisson"
    ],
    "Pharmacy": [
        "Apollo Pharmacy", "MedPlus", "1mg"
    ],
    "Fashion": [
        "Myntra", "Ajio", "Lifestyle", "Pantaloons"
    ],
    "Entertainment": [
        "PVR", "INOX", "BookMyShow"
    ],
    "Utilities": [
        "Electricity Board", "Water Board", "Gas Agency"
    ]
}

cities = [
    "Delhi",
    "Mumbai",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Ahmedabad",
    "Jaipur",
    "Kolkata",
    "Chandigarh",
    "Lucknow",
    "Noida",
    "Indore",
    "Surat",
    "Nagpur"
]

merchants = []

merchant_id = 1

while merchant_id <= NUM_MERCHANTS:

    category = random.choice(list(merchant_categories.keys()))

    base_name = random.choice(merchant_categories[category])

    merchant_name = f"{base_name} #{merchant_id}"

    city = random.choice(cities)

    merchants.append({
        "merchant_id": merchant_id,
        "merchant_name": merchant_name,
        "category": category,
        "city": city,
        "country": "India"
    })

    merchant_id += 1

df = pd.DataFrame(merchants)

df.to_csv("merchants.csv", index=False)

print(df.head())
print(f"\nGenerated {len(df)} merchants.")