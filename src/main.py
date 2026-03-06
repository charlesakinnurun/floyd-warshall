import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class FloydWarshallVisualizer:
    """
    A class to implement the Floyd-Warshall algorithm and visualize
    the process and results for All-Pairs Shortest Paths.
    """
    
    def __init__(self, num_nodes):
        # Initialize the number of nodes in the graph
        self.num_nodes = num_nodes
        
        # Initialize the distance matrix with infinity
        # np.inf represents that there is no direct edge between nodes initially
        self.dist_matrix = np.full((num_nodes, num_nodes), np.inf)
        
        # The distance from a node to itself is always 0
        np.fill_diagonal(self.dist_matrix, 0)
        
        # Predecessor matrix to reconstruct the actual paths
        # None indicates no intermediate step exists yet
        self.next_node = [[None for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, u, v, weight):
        """Adds a directed edge from u to v with a specific weight."""
        self.dist_matrix[u][v] = weight
        # For path reconstruction: to get from u to v, the next step is v
        self.next_node[u][v] = v

    def run_algorithm(self):
        """
        The core Floyd-Warshall logic:
        For every pair of vertices (i, j), check if a path through 
        an intermediate vertex 'k' is shorter than the current path.
        """
        # k is the 'intermediate' node we are considering
        for k in range(self.num_nodes):
            # i is the source node
            for i in range(self.num_nodes):
                # j is the destination node
                for j in range(self.num_nodes):
                    # Check if the path through k (i -> k -> j) is shorter
                    if self.dist_matrix[i][k] + self.dist_matrix[k][j] < self.dist_matrix[i][j]:
                        # Update the shortest distance
                        self.dist_matrix[i][j] = self.dist_matrix[i][k] + self.dist_matrix[k][j]
                        # Update the path tracking
                        self.next_node[i][j] = self.next_node[i][k]

    def get_path(self, start, end):
        """Reconstructs the shortest path from start to end."""
        if self.next_node[start][end] is None:
            return []
        path = [start]
        while start != end:
            start = self.next_node[start][end]
            path.append(start)
        return path

    def visualize_graph(self, title="Graph Visualization"):
        """Uses NetworkX and Matplotlib to draw the graph and the distance matrix."""
        G = nx.DiGraph()
        
        # Add edges to the NetworkX graph for visualization
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                if i != j and self.dist_matrix[i][j] != np.inf:
                    G.add_edge(i, j, weight=self.dist_matrix[i][j])

        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 5))

        # Subplot 1: The Graph Structure
        plt.subplot(1, 2, 1)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold', arrows=True)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title(f"{title}\n(Shortest Path Distances)")

        # Subplot 2: The Distance Matrix Heatmap
        plt.subplot(1, 2, 2)
        # Replace inf with a high value just for the heatmap color scaling
        display_matrix = np.where(self.dist_matrix == np.inf, -1, self.dist_matrix)
        plt.imshow(display_matrix, cmap='YlGnBu')
        plt.colorbar(label='Shortest Distance (-1 = No Path)')
        plt.title("Distance Matrix Heatmap")
        
        # Add text labels to the heatmap cells
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                val = self.dist_matrix[i][j]
                label = '∞' if val == np.inf else str(int(val))
                plt.text(j, i, label, ha='center', va='center', color='black')

        plt.tight_layout()
        plt.show()

def main():
    # --- EXAMPLE 1: Standard Graph ---
    print("Example 1: Running Floyd-Warshall on a 4-node graph...")
    # Node mapping: 0:A, 1:B, 2:C, 3:D
    fw = FloydWarshallVisualizer(4)
    fw.add_edge(0, 1, 3)   # A -> B (3)
    fw.add_edge(1, 0, 2)   # B -> A (2)
    fw.add_edge(0, 3, 5)   # A -> D (5)
    fw.add_edge(1, 2, 1)   # B -> C (1)
    fw.add_edge(2, 3, 8)   # C -> D (8)
    fw.add_edge(3, 2, 2)   # D -> C (2)

    print("Initial state created. Processing...")
    fw.run_algorithm()
    
    print("\nShortest Distance Matrix:")
    print(fw.dist_matrix)
    
    # Path reconstruction example
    start_node, end_node = 0, 2
    path = fw.get_path(start_node, end_node)
    print(f"\nShortest Path from {start_node} to {end_node}: {path}")
    
    # Visualization
    fw.visualize_graph("Floyd-Warshall Result (Example 1)")

    # --- ILLUSTRATION OF THE CONCEPT ---
    # The Floyd-Warshall Algorithm works on the Dynamic Programming principle.
    # Time Complexity: O(V^3) where V is the number of vertices.
    # Space Complexity: O(V^2) for the distance matrix.
    # It handles negative weights but NOT negative cycles.

if __name__ == "__main__":
    main()