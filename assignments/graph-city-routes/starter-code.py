"""Starter code for Graph Algorithms - City Routes assignment.

Complete the TODOs in each section.
"""

from collections import deque
import heapq
import random
import time


# Sample road map: (from_node, to_node, travel_time)
ROADS = [
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


def build_graph(roads):
    """Build an undirected weighted adjacency list.

    Returns:
        dict[str, list[tuple[str, int]]]
    """
    graph = {}

    # TODO: Build adjacency list for both directions.
    # Example: graph["A"] = [("B", 4), ("C", 2)]

    return graph


def bfs_min_hops(graph, start, goal, blocked_roads=None):
    """Return a path with minimum number of hops using BFS.

    Args:
        graph: adjacency list
        start: start node
        goal: target node
        blocked_roads: optional set of blocked undirected edges
            like {frozenset({"A", "B"})}

    Returns:
        list[str] | None
    """
    if blocked_roads is None:
        blocked_roads = set()

    # TODO:
    # 1) Use a queue for BFS
    # 2) Track visited nodes
    # 3) Track parent pointers to reconstruct the path
    # 4) Return None if no route exists

    return None


def dijkstra_shortest_time(graph, start, goal, blocked_roads=None):
    """Return the minimum-cost path and total travel time.

    Returns:
        tuple[list[str], int] | None
    """
    if blocked_roads is None:
        blocked_roads = set()

    # TODO:
    # 1) Use a priority queue (min-heap)
    # 2) Track best known distance to each node
    # 3) Track parent pointers for path reconstruction
    # 4) Return None if no route exists

    return None


def reconstruct_path(parent, start, goal):
    """Reconstruct a path from parent pointers."""
    path = []
    current = goal

    # TODO: Build path by walking from goal -> start using parent

    # Reverse and validate path before returning
    return None


def make_blocked_edge(a, b):
    """Create a normalized undirected edge key."""
    return frozenset({a, b})


def generate_random_graph(num_nodes, edge_probability=0.08, max_weight=20):
    """Generate a random undirected weighted graph."""
    nodes = [f"N{i}" for i in range(num_nodes)]
    graph = {node: [] for node in nodes}

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                w = random.randint(1, max_weight)
                a, b = nodes[i], nodes[j]
                graph[a].append((b, w))
                graph[b].append((a, w))

    return graph, nodes


def benchmark_algorithms():
    """Run basic timing comparisons for BFS and Dijkstra."""
    for size in [50, 200, 1000]:
        graph, nodes = generate_random_graph(size)
        start, goal = nodes[0], nodes[-1]

        t0 = time.perf_counter()
        _ = bfs_min_hops(graph, start, goal)
        bfs_ms = (time.perf_counter() - t0) * 1000

        t0 = time.perf_counter()
        _ = dijkstra_shortest_time(graph, start, goal)
        dij_ms = (time.perf_counter() - t0) * 1000

        print(f"size={size:4d} | BFS={bfs_ms:8.3f} ms | Dijkstra={dij_ms:8.3f} ms")


def demo():
    graph = build_graph(ROADS)

    print("Graph:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")

    tests = [("A", "E"), ("A", "F"), ("B", "E")]

    print("\n--- Without blocked roads ---")
    for start, goal in tests:
        bfs_path = bfs_min_hops(graph, start, goal)
        dij_result = dijkstra_shortest_time(graph, start, goal)

        print(f"\n{start} -> {goal}")
        print("BFS:", bfs_path)
        print("Dijkstra:", dij_result)

    blocked = {
        make_blocked_edge("B", "D"),
        make_blocked_edge("D", "E"),
    }

    print("\n--- With blocked roads ---")
    for start, goal in tests:
        bfs_path = bfs_min_hops(graph, start, goal, blocked_roads=blocked)
        dij_result = dijkstra_shortest_time(graph, start, goal, blocked_roads=blocked)

        print(f"\n{start} -> {goal}")
        print("BFS:", bfs_path)
        print("Dijkstra:", dij_result)

    print("\n--- Benchmark ---")
    benchmark_algorithms()


if __name__ == "__main__":
    demo()
