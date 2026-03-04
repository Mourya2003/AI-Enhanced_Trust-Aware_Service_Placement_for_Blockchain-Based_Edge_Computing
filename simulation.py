import random
import numpy as np
from components.blockchain import Blockchain
from components.edge_node import EdgeNode
from components.trust_manager import TrustManager
from components.placement_controller import PlacementController

# --------------------------------
# SYSTEM SETUP
# --------------------------------

blockchain = Blockchain()
trust_manager = TrustManager()
placement_controller = PlacementController(blockchain)

validators = ["validator1","validator2","validator3"]
for v in validators:
    blockchain.add_validator(v)

# create nodes
nodes = []

for i in range(6):
    node = EdgeNode(f"node_{i}", initial_trust=random.randint(60,90))
    
    node.total_tasks = random.randint(50,120)
    node.success_count = int(node.total_tasks * random.uniform(0.8,0.95))
    node.failure_count = node.total_tasks - node.success_count
    
    nodes.append(node)

# --------------------------------
# TASK SIMULATION
# --------------------------------

success_count = 0
fail_count = 0

for task in range(50):

    node, msg = placement_controller.request_placement(nodes)

    if node:

        success = random.random() > 0.15

        trust_manager.update_trust(node, success)

        if success:
            success_count += 1
        else:
            fail_count += 1

# --------------------------------
# RESULTS
# --------------------------------

print("\nSimulation Finished\n")
print("Total Tasks:",50)
print("Success:",success_count)
print("Failures:",fail_count)

rate = success_count/50*100
print("Success Rate:",round(rate,2),"%")