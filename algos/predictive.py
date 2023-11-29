# Predictive Energy Allocation: Integrate predictive analytics to allocate consensus tasks based on forecasted energy availability. 
# This involves predicting energy surplus for each node and allocating tasks accordingly.

import random
import matplotlib.pyplot as plt

# Define the Node class
class Node:
    def __init__(self, capacity, energy_consumption):
        self.capacity = capacity
        self.energy_consumption = energy_consumption
        self.energy_balance = random.randint(30, 70)  # Initialize with random energy balance
        self.predicted_surplus = 0  # Initialize predicted surplus to 0

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
        self.blocks.append(self.nodes.copy())  # Store the state of nodes after each block

# Implement Predictive Energy Allocation
def predictive_energy_allocation(nodes):
    # Logic for predicting energy surplus and allocating tasks accordingly
    for node in nodes:
        # Example: Predicted surplus is calculated based on energy balance and energy consumption
        node.predicted_surplus = node.energy_balance - node.energy_consumption
        # Allocate tasks based on predicted surplus (higher surplus, more tasks)
        node.task_allocation = min(node.predicted_surplus, 10)  # Assign a maximum of 10 tasks

# Main simulation
nodes = [
    Node(capacity=100, energy_consumption=8),
    Node(capacity=120, energy_consumption=10),
    Node(capacity=80, energy_consumption=6)
]

blockchain = Blockchain(nodes)

# Lists to store energy balance and task allocation data for plotting
energy_balance_data = [[] for _ in range(len(nodes))]
task_allocation_data = [[] for _ in range(len(nodes))]

# Simulate blockchain with 10 blocks
for _ in range(10):
    predictive_energy_allocation(nodes)
    blockchain.add_block()

    # Store energy balance and task allocation data for each node
    for i, node in enumerate(nodes):
        energy_balance_data[i].append(node.energy_balance)
        task_allocation_data[i].append(node.task_allocation)

# Print node statistics
for i, node in enumerate(nodes):
    print(f"Node {i + 1}: Capacity={node.capacity}, Energy Consumption={node.energy_consumption}")

# Generate plots or charts (using Matplotlib) to visualize the results
for i in range(len(nodes)):
    plt.subplot(len(nodes), 1, i + 1)
    plt.plot(range(1, 11), energy_balance_data[i], label=f'Energy Balance')
    plt.plot(range(1, 11), task_allocation_data[i], label=f'Task Allocation')
    plt.xlabel("Blocks")
    plt.ylabel("Value")
    plt.legend()
    plt.title(f"Node {i + 1} Energy Balance and Task Allocation")

plt.tight_layout()
plt.show()
