from faker import Faker
import pandas as pd
import random
from datetime import datetime

fake = Faker("en_IN")
random.seed(42)

NUM_CUSTOMERS = 10000

occupations = {
    "Student": (100000, 500000),
    "Teacher": (400000, 900000),
    "Software Engineer": (800000, 2000000),
    "Doctor": (1200000, 3000000),
    "Business": (1000000, 3500000),
    "Manager": (900000, 2500000),
    "Professor": (700000, 1800000),
    "Lawyer": (800000, 2500000),
    "Consultant": (900000, 3000000),
    "Government Employee": (500000, 1500000)
}

segments = ["Standard", "Silver", "Gold", "Platinum"]
segment_weights = [0.55, 0.25, 0.15, 0.05]

cities = [
    "Delhi","Mumbai","Bengaluru","Hyderabad","Chennai",
    "Pune","Kolkata","Ahmedabad","Chandigarh","Jaipur",
    "Lucknow","Indore","Surat","Nagpur","Noida"
]

states = {
    "Delhi":"Delhi",
    "Mumbai":"Maharashtra",
    "Bengaluru":"Karnataka",
    "Hyderabad":"Telangana",
    "Chennai":"Tamil Nadu",
    "Pune":"Maharashtra",
    "Kolkata":"West Bengal",
    "Ahmedabad":"Gujarat",
    "Chandigarh":"Chandigarh",
    "Jaipur":"Rajasthan",
    "Lucknow":"Uttar Pradesh",
    "Indore":"Madhya Pradesh",
    "Surat":"Gujarat",
    "Nagpur":"Maharashtra",
    "Noida":"Uttar Pradesh"
}

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    gender = random.choice(["Male", "Female"])

    if gender == "Male":
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()

    last_name = fake.last_name()

    occupation = random.choice(list(occupations.keys()))

    income = random.randint(
        occupations[occupation][0],
        occupations[occupation][1]
    )

    city = random.choice(cities)

    state = states[city]

    age = random.randint(18, 70)

    segment = random.choices(
        segments,
        weights=segment_weights,
        k=1
    )[0]

    join_date = fake.date_between(
        start_date="-8y",
        end_date="today"
    )

    customers.append({
        "customer_id": customer_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "city": city,
        "state": state,
        "occupation": occupation,
        "annual_income": income,
        "customer_segment": segment,
        "join_date": join_date
    })

df = pd.DataFrame(customers)

df.to_csv("customers.csv", index=False)

print(df.head())

print(f"\nGenerated {len(df)} customers.")