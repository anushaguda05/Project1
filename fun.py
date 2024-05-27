import networkx as nx
import matplotlib.pyplot as plt
# Create an empty graph
graph = nx.Graph()

# Assuming each line contains data like "person1, person2"
with open('Mytable.sql', 'r') as file:
    for line in file:
        person1 = line.strip().split(', ')  # Adjust the splitting logic based on your data
        graph.add_node(person1)
        
        graph.add_edge(person1)
        
# Draw the graph
pos = nx.spring_layout(graph)  # Position nodes using a spring layout
nx.draw(graph, pos, with_labels=True, node_size=500)
plt.show()


# You can also add more attributes to nodes and edges as needed
