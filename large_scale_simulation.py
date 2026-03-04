import random
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("datasets/node_dataset.csv")

# create nodes from dataset
nodes = df.sample(30).to_dict("records")

TOTAL_TASKS = 500

random_success = 0
trust_success = 0
ai_success = 0

random_latency = []
trust_latency = []
ai_latency = []

# ---------------------------
# RANDOM PLACEMENT
# ---------------------------

for _ in range(TOTAL_TASKS):

    node = random.choice(nodes)

    failure_probability = node["failure_risk"]

    if failure_probability == 1:
        result = random.random() > 0.4
    else:
        result = random.random() > 0.1

    if result:
        random_success += 1

    random_latency.append(node["latency"])


# ---------------------------
# TRUST PLACEMENT
# ---------------------------

for _ in range(TOTAL_TASKS):

    node = max(nodes, key=lambda x: x["trust_score"])

    failure_probability = node["failure_risk"]

    if failure_probability == 1:
        result = random.random() > 0.3
    else:
        result = random.random() > 0.08

    if result:
        trust_success += 1

    trust_latency.append(node["latency"])


# ---------------------------
# AI + TRUST PLACEMENT
# ---------------------------

for _ in range(TOTAL_TASKS):

    # pick nodes predicted reliable
    reliable_nodes = [n for n in nodes if n["failure_risk"] == 0]

    if reliable_nodes:
        node = max(reliable_nodes, key=lambda x: x["trust_score"])
    else:
        node = random.choice(nodes)

    result = random.random() > 0.05

    if result:
        ai_success += 1

    ai_latency.append(node["latency"])


# ---------------------------
# RESULTS
# ---------------------------

random_rate = random_success / TOTAL_TASKS * 100
trust_rate = trust_success / TOTAL_TASKS * 100
ai_rate = ai_success / TOTAL_TASKS * 100

print("\n----- EXPERIMENT RESULTS -----\n")

print("Random Success Rate:", random_rate)
print("Trust Success Rate:", trust_rate)
print("AI + Trust Success Rate:", ai_rate)


# ---------------------------
# GRAPH
# ---------------------------

methods = ["Random", "Trust", "AI+Trust"]
rates = [random_rate, trust_rate, ai_rate]

plt.figure(figsize=(6,4))
plt.bar(methods, rates)
plt.ylabel("Success Rate (%)")
plt.title("Service Placement Performance Comparison")
plt.savefig("placement_comparison.png")

print("\nGraph saved: placement_comparison.png")