import heapq

import matplotlib.pyplot as plt
import networkx as nx


def add_edges(
    graph: nx.DiGraph,
    heap: list[int],
    pos: dict,
    index: int = 0,
    x: float = 0,
    y: float = 0,
    layer: int = 1,
    color: str = "skyblue",
) -> nx.DiGraph:
    """Recursively add edges to the existing graph."""
    if index >= len(heap):
        return graph

    # Add the current node
    node_val = heap[index]
    graph.add_node(node_val, color=color, label=node_val)
    pos[node_val] = (x, y)

    # Calculate indices for children
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # Add left child
    if left_index < len(heap):
        left_val = heap[left_index]
        graph.add_edge(node_val, left_val)
        l = x - 1 / 2**layer
        add_edges(
            graph, heap, pos, left_index, x=l, y=y - 1, layer=layer + 1, color=color
        )

    # Add right child
    if right_index < len(heap):
        right_val = heap[right_index]
        graph.add_edge(node_val, right_val)
        r = x + 1 / 2**layer
        add_edges(
            graph, heap, pos, right_index, x=r, y=y - 1, layer=layer + 1, color=color
        )

    return graph


def draw_min_heap_tree(
    user_list: list[int], node_colors: dict[int, str] | None = None
) -> None:
    """Heapify the user list and draw the min-heap as a tree."""
    # Create a min-heap from the copy of the user list (copy to not modify the original)
    heapified_list = user_list.copy()
    heapq.heapify(heapified_list)

    # Draw the min-heap
    tree = nx.DiGraph()
    pos = {}
    tree = add_edges(tree, heapified_list, pos)

    # Update node colors if provided
    if node_colors:
        for node in tree.nodes():
            if node in node_colors:
                tree.nodes[node]["color"] = node_colors[node]

    # Extract colors and labels for drawing
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrowsize=1,
        node_size=2500,
        node_color=colors,
    )

    plt.show()


if __name__ == "__main__":
    # The list is heapified inside the function
    draw_min_heap_tree([6, 4, 5, 10, 1, 3])
