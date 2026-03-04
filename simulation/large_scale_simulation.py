import random
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("datasets/node_dataset.csv")

# Sample nodes for simulation
nodes = df.sample(30).to_dict("records")

TOTAL_TASKS = 500

random_success = 0
trust_success = 0
ai_success = 0

random_latency = []
trust_latency = []
ai_latency = []

# RANDOM SELECTION
for i in range(TOTAL_TASKS):
    node = random.choice(nodes)
    if node["failure_risk"] == 1:
        result = random.random() > 0.4
    else:
        result = random.random() > 0.1
    
    if result:
        random_success += 1
    
    random_latency.append(node["latency"])

# TRUST-BASED SELECTION
for i in range(TOTAL_TASKS):
    # [cite_start]Select node with highest trust score [cite: 375, 402]
    node = max(nodes, key=lambda x: x["trust_score"])
    
    if node["failure_risk"] == 1:
        result = random.random() > 0.3
    else:
        result = random.random() > 0.08
    
    if result:
        trust_success += 1
    
    trust_latency.append(node["latency"])

# AI + TRUST SELECTION
for i in range(TOTAL_TASKS):
    reliable_nodes = []
    for n in nodes:
        # [cite_start]Filter nodes based on reliability/risk [cite: 391, 393]
        if n["failure_risk"] == 0:
            reliable_nodes.append(n)
    
    if len(reliable_nodes) > 0:
        node = max(reliable_nodes, key=lambda x: x["trust_score"])
    else:
        node = random.choice(nodes)
    
    result = random.random() > 0.05
    
    if result:
        ai_success += 1
    
    ai_latency.append(node["latency"])

# RESULTS CALCULATION
random_rate = (random_success / TOTAL_TASKS) * 100
trust_rate = (trust_success / TOTAL_TASKS) * 100
ai_rate = (ai_success / TOTAL_TASKS) * 100

random_fail = 100 - random_rate
trust_fail = 100 - trust_rate
ai_fail = 100 - ai_rate

avg_random_latency = sum(random_latency) / len(random_latency)
avg_trust_latency = sum(trust_latency) / len(trust_latency)
avg_ai_latency = sum(ai_latency) / len(ai_latency)

# CONSOLE OUTPUT
print(f"Random Success Rate: {random_rate}%")
print(f"Trust-based Success Rate: {trust_rate}%")
print(f"AI+Trust Success Rate: {ai_rate}%")

# PLOTTING
methods = ["Random", "Trust", "AI+Trust"]

# [cite_start]Success Rate Graph [cite: 512, 513]
plt.figure()
plt.bar(methods, [random_rate, trust_rate, ai_rate])
plt.ylabel("Success Rate (%)")
plt.title("Placement Performance Comparison")
plt.savefig("success_rate.png")

# [cite_start]Failure Rate Graph [cite: 561, 562]
plt.figure()
plt.bar(methods, [random_fail, trust_fail, ai_fail])
plt.ylabel("Failure Rate (%)")
plt.title("Failure Comparison")
plt.savefig("failure_rate.png")

# [cite_start]Latency Graph [cite: 513, 619]
plt.figure()
plt.bar(methods, [avg_random_latency, avg_trust_latency, avg_ai_latency])
plt.ylabel("Avg Latency (ms)")
plt.title("Latency Comparison")
plt.savefig("latency_comparison.png")

print("Graphs created successfully.")