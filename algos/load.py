#  Load Balancing: Develop an algorithm that distributes tasks across nodes considering their energy efficiency.
# Nodes with higher energy efficiency should receive more tasks.

import random
import matplotlib.pyplot as plt

# Define the Node class
class Node:
    def __init__(self, capacity, energy_consumption):
        self.capacity = capacity
        self.energy_consumption = energy_consumption
        self.energy_balance = random.randint(30, 70)  # Initialize with random energy balance
        self.tasks_assigned = 0

# Define a simple blockchain class for simulation
class Blockchain:
    def __init__(self, nodes):
        self.nodes = nodes
        self.blocks = []

    def add_block(self):
        # Simulate a new block being added
        for node in self.nodes:
            if node.energy_balance >= node.energy_consumption:
                node.energy_balance -= node.energy_consumption
                node.tasks_assigned += 1
        self.blocks.append(self.nodes.copy())  # Store the state of nodes after each block

# Implement Load Balancing
def load_balancing(nodes):
    # Logic for load balancing (distributing tasks based on energy efficiency)
    total_capacity = sum(node.capacity for node in nodes)
    for node in nodes:
        node.task_share = (node.capacity / total_capacity) * 100  # Assign task share based on capacity

# Main simulation
nodes = [
    Node(capacity=100, energy_consumption=8),
    Node(capacity=120, energy_consumption=10),
    Node(capacity=80, energy_consumption=6)
]

blockchain = Blockchain(nodes)

# Lists to store task assignment data for plotting
tasks_assigned_data = [[] for _ in range(len(nodes))]

# Simulate blockchain with 10 blocks
for _ in range(10):
    load_balancing(nodes)
    blockchain.add_block()

    # Store task assignment data for each node
    for i, node in enumerate(nodes):
        tasks_assigned_data[i].append(node.tasks_assigned)

# Print node statistics
for i, node in enumerate(nodes):
    print(f"Node {i + 1}: Capacity={node.capacity}, Energy Consumption={node.energy_consumption}")

# Generate plots or charts (using Matplotlib) to visualize the results
for i, node_data in enumerate(tasks_assigned_data):
    plt.plot(range(1, 11), node_data, label=f'Node {i + 1}')

plt.xlabel("Blocks")
plt.ylabel("Tasks Assigned")
plt.legend()
plt.title("Tasks Assigned Over Blocks")
plt.show()
