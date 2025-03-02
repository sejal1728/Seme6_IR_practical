import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges (this defines the web graph structure)
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Calculate PageRank
pagerank_scores = nx.pagerank(G)

# Calculate HITS (Hub and Authority) scores
hits_scores = nx.hits(G)

# Print the results
print("PageRank Scores:", pagerank_scores)
print("Hub Scores:", hits_scores[0])  # Hub scores
print("Authority Scores:", hits_scores[1])  # Authority scores

# Visualize the graph
pos = nx.spring_layout(G)  # Positions for all nodes

nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color="gray",
        node_size=2000, font_size=15, font_weight="bold")

plt.title("Directed Graph Visualization")
plt.show()
