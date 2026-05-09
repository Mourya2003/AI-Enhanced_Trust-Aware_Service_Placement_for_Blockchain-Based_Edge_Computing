import pandas as pd
import random
import os


# --------------------------------
# CREATE DATASET DIRECTORY SAFELY
# --------------------------------

os.makedirs("datasets", exist_ok=True)

rows = []

TOTAL_SAMPLES = 2000


# --------------------------------
# GENERATE REALISTIC NODE DATA
# --------------------------------

for i in range(TOTAL_SAMPLES):

    trust = random.randint(40, 100)

    success_rate = random.uniform(0.50, 0.99)

    failures = random.randint(0, 25)

    latency = random.uniform(5, 150)

    cpu_usage = random.uniform(10, 95)

    memory_usage = random.uniform(10, 95)

    # --------------------------------
    # CALCULATE FAILURE RISK SCORE
    # --------------------------------

    risk_score = 0

    # Trust effect
    if trust < 60:
        risk_score += random.uniform(0.20, 0.35)

    # Success rate effect
    if success_rate < 0.75:
        risk_score += random.uniform(0.20, 0.35)

    # Failure history effect
    if failures > 10:
        risk_score += random.uniform(0.10, 0.25)

    # Latency effect
    if latency > 90:
        risk_score += random.uniform(0.10, 0.20)

    # CPU overload effect
    if cpu_usage > 80:
        risk_score += random.uniform(0.10, 0.20)

    # Memory overload effect
    if memory_usage > 80:
        risk_score += random.uniform(0.10, 0.20)

    # --------------------------------
    # PROBABILISTIC LABELING
    # --------------------------------

    failure_probability = min(1.0, risk_score)

    label = 1 if random.random() < failure_probability else 0

    rows.append({
        "trust_score": trust,
        "success_rate": success_rate,
        "failures": failures,
        "latency": latency,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "failure_risk": label
    })


# --------------------------------
# SAVE DATASET
# --------------------------------

df = pd.DataFrame(rows)

dataset_path = "datasets/node_dataset.csv"

df.to_csv(dataset_path, index=False)


# --------------------------------
# OUTPUT
# --------------------------------

print("Dataset generated successfully")

print("Total samples:", len(df))

print("\nDataset saved to:")
print(dataset_path)

print("\nSample Data:")
print(df.head())