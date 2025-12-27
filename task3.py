import heapq

import matplotlib.pyplot as plt
import networkx as nx


def dijkstra(graph: nx.Graph, start: str) -> dict[str, float]:
    """Dijkstra's algorithm using heapq for optimization."""
    # Initialize distances with infinity
    distances = {node: float("inf") for node in graph.nodes()}
    # and zero for the start node
    distances[start] = 0
    # We start with the first node
    pq = [(0, start)]
    # This is needed to store already visited nodes
    visited = set()

    # While there are nodes to process
    while pq:
        # Extract the node with minimum distance from the heap
        current_dist, current = heapq.heappop(pq)

        # Skip if already processed
        if current in visited:
            continue
        visited.add(current)

        # Check all neighbors of the current node
        for neighbor in graph.neighbors(current):
            # Get the edge weight and calculate a new distance
            weight = graph[current][neighbor].get("weight", 1)
            distance = current_dist + weight

            # If found a shorter path - update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add the neighbor to the heap to process it later
                heapq.heappush(pq, (distance, neighbor))

    return distances


if __name__ == "__main__":
    # Create a sample graph with weighted edges
    graph = nx.Graph()
    graph.add_weighted_edges_from(
        [
            ("A", "B", 4),
            ("A", "C", 2),
            ("B", "C", 1),
            ("B", "D", 5),
            ("C", "D", 8),
            ("C", "E", 10),
            ("D", "E", 2),
            ("D", "F", 6),
            ("E", "F", 3),
        ]
    )

    # Define a starting node and compute shortest paths
    # from the starting node to all other nodes
    start_node = "A"
    distances = dijkstra(graph, start_node)
    print(f"Shortest paths from node '{start_node}': {distances}")

    # Arrange nodes (set a seed to have consistent layout)
    pos = nx.spring_layout(graph, seed=1)

    # Draw colors for each node, except the starting node will be highlighted
    node_colors = [
        "coral" if node == start_node else "skyblue" for node in graph.nodes()
    ]
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=1000)

    # Draw edges with labels
    nx.draw_networkx_edges(graph, pos)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_size=12)

    # Draw node labels with calculated distances (B (10), etc.)
    labels = {node: f"{node}\n({distances[node]:.0f})" for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels)

    plt.title(f"Найкоротші шляхи від вершини '{start_node}' (алгоритм Дейкстри)")
    plt.axis("off")
    plt.show()
