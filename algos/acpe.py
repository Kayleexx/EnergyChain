# ACPE: This involves dynamically adjusting participation requirements based on node energy availability. 
# Define the logic for how nodes decide to participate in the consensus process based on their energy balance.

import random
import matplotlib.pyplot as plt

# Define the Node class
class Node:
    def __init__(self, capacity, energy_consumption):
        self.capacity = capacity
        self.energy_consumption = energy_consumption
        self.energy_balance = random.randint(30, 70)  # Initialize with random energy balance

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

# Implement ACPE Mechanism
def acpe_mechanism(nodes):
    # Logic for ACPE mechanism (adjusting participation requirements based on energy balance)
    for node in nodes:
        # Example: Nodes with energy balance below a threshold may choose not to participate
        if node.energy_balance < 50:
            # Adjust participation requirements
            node.participation_requirement = "Low"
        else:
            node.participation_requirement = "High"

# Main simulation
nodes = [
    Node(capacity=100, energy_consumption=8),
    Node(capacity=120, energy_consumption=10),
    Node(capacity=80, energy_consumption=6)
]

blockchain = Blockchain(nodes)

# Lists to store energy balance data for plotting
energy_balance_data = [[] for _ in range(len(nodes))]

# Simulate blockchain with 10 blocks
for _ in range(10):
    acpe_mechanism(nodes)
    blockchain.add_block()

    # Store energy balance data for each node
    for i, node in enumerate(nodes):
        energy_balance_data[i].append(node.energy_balance)

# Print node statistics
for i, node in enumerate(nodes):
    print(f"Node {i + 1}: Capacity={node.capacity}, Energy Consumption={node.energy_consumption}")

# Generate plots or charts (using Matplotlib) to visualize the results
for i, node_data in enumerate(energy_balance_data):
    plt.plot(range(1, 11), node_data, label=f'Node {i + 1}')

plt.xlabel("Blocks")
plt.ylabel("Energy Balance")
plt.legend()
plt.title("Energy Balance Over Blocks")
plt.show()
