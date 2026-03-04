import pandas as pd
import random

rows = []

for i in range(1000):

    trust = random.randint(40, 100)
    success_rate = random.uniform(0.6, 0.98)
    failures = random.randint(0, 20)
    latency = random.uniform(5, 120)
    cpu_usage = random.uniform(20, 95)

    # failure label rule
    if trust < 60 or success_rate < 0.75 or latency > 80:
        label = 1
    else:
        label = 0

    rows.append({
        "trust_score": trust,
        "success_rate": success_rate,
        "failures": failures,
        "latency": latency,
        "cpu_usage": cpu_usage,
        "failure_risk": label
    })

df = pd.DataFrame(rows)

df.to_csv("node_dataset.csv", index=False)

print("Dataset generated successfully")
print("Total samples:", len(df))
print(df.head())