import heapq
from collections import deque

from task4 import draw_min_heap_tree


def generate_color_gradient(
    num_colors: int, start_color: str = "#000080", end_color: str = "#ADD8E6"
) -> list[str]:
    """Generates a color gradient from dark to light shade."""
    # Convert hex to RGB
    start_r = int(start_color[1:3], 16)
    start_g = int(start_color[3:5], 16)
    start_b = int(start_color[5:7], 16)

    end_r = int(end_color[1:3], 16)
    end_g = int(end_color[3:5], 16)
    end_b = int(end_color[5:7], 16)

    colors = []
    for i in range(num_colors):
        # Interpolate between the start and end colors
        ratio = i / max(num_colors - 1, 1)
        r = int(start_r + (end_r - start_r) * ratio)
        g = int(start_g + (end_g - start_g) * ratio)
        b = int(start_b + (end_b - start_b) * ratio)

        # Convert back to hex
        color_hex = f"#{r:02X}{g:02X}{b:02X}"
        colors.append(color_hex)

    return colors


def dfs_traversal(heap: list[int]) -> list[int]:
    """Generates a list of indexes of DFS traversal of the binary heap."""
    if not heap:
        return []

    result = []
    # Stack: store node indexes, starting with the root
    stack = [0]

    # Process nodes until the stack is empty
    while stack:
        index = stack.pop()

        # If the index is out of bounds, skip
        if index >= len(heap):
            continue

        # Add the current node to the result
        result.append(heap[index])

        # Add the right child first (because stack is LIFO)
        # so that the left child is processed first
        right_index = 2 * index + 2
        if right_index < len(heap):
            stack.append(right_index)

        # Add the left child
        left_index = 2 * index + 1
        if left_index < len(heap):
            stack.append(left_index)

    return result


def bfs_traversal(heap: list[int]) -> list[int]:
    """Generates a list of indexes of BFS traversal of the binary heap."""
    if not heap:
        return []

    result = []
    # Queue: store node indexes, starting with the root
    queue = deque([0])

    # Process nodes until the queue is empty
    while queue:
        index = queue.popleft()

        # If the index is out of bounds, skip
        if index >= len(heap):
            continue

        # Add the current node to the result
        result.append(heap[index])

        # Add the left child to the queue
        left_index = 2 * index + 1
        if left_index < len(heap):
            queue.append(left_index)

        # Add the right child to the queue
        right_index = 2 * index + 2
        if right_index < len(heap):
            queue.append(right_index)

    return result


def visualize_tree_traversal(heap: list[int], traversal_order: list[int]):
    """Uses task4's draw_min_heap_tree to visualize the heap with colors based on traversal order."""
    # Generate a color gradient
    colors = generate_color_gradient(len(traversal_order))

    # Create a dictionary: node value -> color
    node_colors = {}
    for i, node_val in enumerate(traversal_order):
        if node_val not in node_colors:  # If the node doesn't have a color yet
            node_colors[node_val] = colors[i]

    # Використовуємо draw_min_heap_tree з task4 з кастомними кольорами
    draw_min_heap_tree(heap, node_colors=node_colors)


if __name__ == "__main__":
    user_list = [15, 10, 8, 12, 20, 5, 7, 3, 11, 25, 18]
    heapified_list = user_list.copy()
    heapq.heapify(heapified_list)

    # DFS using stack
    dfs_order = dfs_traversal(heapified_list)
    # Draw the tree with DFS colors
    visualize_tree_traversal(heapified_list, dfs_order)

    # BFS using queue
    bfs_order = bfs_traversal(heapified_list)
    # Draw the tree with BFS colors
    visualize_tree_traversal(heapified_list, bfs_order)
