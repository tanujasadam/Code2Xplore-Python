import random
import pandas as pd
import numpy as np
import math


def generate_city_data(n=18):
    data = []
    for i in range(1, n+1):
        zone = {
            "zone": i,
            "traffic": random.randint(0,100),
            "air_quality": random.randint(0,300),
            "energy": random.randint(0,500)
        }
        data.append(zone)
    return data


def classify_zones(data):
    categories = {}
    for d in data:
        if d["air_quality"] > 200 or d["traffic"] > 80:
            categories[d["zone"]] = "High Risk"
        elif d["energy"] > 400:
            categories[d["zone"]] = "Energy Critical"
        elif d["traffic"] < 30 and d["air_quality"] < 100:
            categories[d["zone"]] = "Safe Zone"
        else:
            categories[d["zone"]] = "Moderate"
    return categories


def sort_by_traffic(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["traffic"] < data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]
    return data


def analyze_data(df):
    df["risk_score"] = (
        df["traffic"]*0.4 +
        df["air_quality"]*0.4 +
        df["energy"]*0.2
    )

    df["sqrt_risk"] = df["risk_score"].apply(math.sqrt)

    mean_values = np.mean(df[["traffic","air_quality","energy"]])

    top3 = df.nlargest(3, "risk_score")

    return df, mean_values, top3


def system_decision(df):

    max_risk = df["risk_score"].max()
    avg_risk = df["risk_score"].mean()
    min_risk = df["risk_score"].min()

    if max_risk > 250:
        decision = "Critical Emergency"
    elif avg_risk > 180:
        decision = "High Alert"
    elif avg_risk > 120:
        decision = "Moderate Risk"
    else:
        decision = "City Stable"

    return (max_risk, avg_risk, min_risk), decision


roll = int(input("Enter Roll Number: "))

city_data = generate_city_data()

if roll % 3 == 0:
    random.shuffle(city_data)
else:
    city_data = sort_by_traffic(city_data)

categories = classify_zones(city_data)

df = pd.DataFrame(city_data)

df, means, top3 = analyze_data(df)

risk_tuple, decision = system_decision(df)

print("\nCity DataFrame")
print(df)

print("\nCategorized Zones")
print(categories)

print("\nTop 3 Risk Zones")
print(top3)

print("\nRisk Tuple")
print(risk_tuple)

print("\nFinal System Decision")
print(decision)