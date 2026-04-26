import random
import copy
import math
import numpy as np
import pandas as pd


def generate_data(n=15):
    data = []
    for i in range(n):
        zone_data = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(10, 100),
                "pollution": random.randint(20, 120),
                "energy": random.randint(50, 200)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone_data)
    return data


def custom_risk_score(t, p, e):
    return math.log(t + p + e)


def to_dataframe(data):
    rows = []
    for item in data:
        rows.append([
            item["zone"],
            item["metrics"]["traffic"],
            item["metrics"]["pollution"],
            item["metrics"]["energy"]
        ])
    return pd.DataFrame(rows, columns=["zone", "traffic", "pollution", "energy"])


def mutate_data(data):
    for item in data:
        item["metrics"]["traffic"] += random.randint(1, 10)
        item["history"].append(random.randint(10, 100))

        t = item["metrics"]["traffic"]
        p = item["metrics"]["pollution"]
        e = item["metrics"]["energy"]

        item["risk"] = custom_risk_score(t, p, e)


def manual_correlation(x, y):
    x = np.array(x)
    y = np.array(y)

    mx = np.mean(x)
    my = np.mean(y)

    num = np.sum((x - mx) * (y - my))
    den = math.sqrt(np.sum((x - mx) ** 2) * np.sum((y - my) ** 2))

    return num / den


def detect_anomalies(arr):
    mean = np.mean(arr)
    std = np.std(arr)

    res = []
    for i, v in enumerate(arr):
        if v > mean + std:
            res.append(i + 1)
    return res


# MAIN
roll = int(input("Enter Roll Number: "))

original = generate_data()

if roll % 2 == 0:
    original = list(reversed(original))
else:
    original = original[3:] + original[:3]

print("\nORIGINAL DATA (BEFORE)")
print(original)

assignment_copy = original
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

mutate_data(shallow_copy)

print("\nORIGINAL AFTER SHALLOW COPY MUTATION")
print(original)

print("\nSHALLOW COPY")
print(shallow_copy)

print("\nDEEP COPY")
print(deep_copy)

df = to_dataframe(original)

df["risk"] = np.log(df["traffic"] + df["pollution"] + df["energy"])
df["sqrt_risk"] = np.sqrt(df["risk"])

print("\nDATAFRAME")
print(df)

mean_vals = np.mean(df[["traffic", "pollution", "energy"]])
var_vals = np.var(df[["traffic", "pollution", "energy"]])

print("\nMEAN")
print(mean_vals)

print("\nVARIANCE")
print(var_vals)

corr = manual_correlation(df["traffic"], df["pollution"])
print("\nMANUAL CORRELATION:", corr)

anomalies = detect_anomalies(df["risk"])
print("\nANOMALY ZONES:", anomalies)

high_risk = df[df["risk"] > np.mean(df["risk"])]

print("\nHIGH RISK ZONES")
print(high_risk["zone"].tolist())

clusters = []
current = []

for z in high_risk["zone"]:
    if not current:
        current.append(z)
    elif z == current[-1] + 1:
        current.append(z)
    else:
        clusters.append(current)
        current = [z]

if current:
    clusters.append(current)

print("\nRISK CLUSTERS:", clusters)

stability_index = 1 / np.var(df["risk"])

max_risk = np.max(df["risk"])
min_risk = np.min(df["risk"])

result = (max_risk, min_risk, stability_index)

print("\nRESULT TUPLE")
print(result)

if stability_index > 2:
    decision = "System Stable"
elif stability_index > 1:
    decision = "Moderate Risk"
elif stability_index > 0.5:
    decision = "High Corruption Risk"
else:
    decision = "Critical Failure"

print("\nFINAL DECISION:", decision)