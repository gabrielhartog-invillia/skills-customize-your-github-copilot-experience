# 📘 Assignment: Graph Algorithms - City Routes

## 🎯 Objective

Apply advanced algorithmic thinking by modeling a city as a weighted graph and implementing search algorithms to solve real routing problems efficiently.

## 📝 Tasks

### 🛠️ Model the City as a Weighted Graph

#### Descrição
Create a graph structure where each intersection is a node and each road is an edge with a travel time cost.

#### Requisitos
O programa concluído deve:

- Represent the graph using an adjacency list
- Support both directions for roads (undirected graph)
- Load road data from a list of tuples in the starter code
- Print the resulting graph in a readable format for debugging

**Exemplo de entrada (trecho):**
```python
roads = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "D", 5),
    ("C", "D", 8)
]
```

### 🛠️ Find Routes with BFS and Dijkstra

#### Descrição
Implement two algorithms and compare their behavior:
- BFS for minimum number of intersections (hops)
- Dijkstra for minimum total travel time

#### Requisitos
O programa concluído deve:

- Implement `bfs_min_hops(graph, start, goal)` returning the path with the fewest hops
- Implement `dijkstra_shortest_time(graph, start, goal)` returning `(path, total_cost)`
- Reconstruct and return full paths, not only cost values
- Handle cases where no route exists by returning `None`
- Demonstrate both algorithms using at least 3 start/goal pairs

**Exemplo de saída esperada:**
```text
BFS route A -> E: A -> C -> E (2 hops)
Dijkstra route A -> E: A -> B -> D -> E (total time: 11)
```

### 🛠️ Add Constraints and Analyze Performance

#### Descrição
Extend your solution so that some roads can be temporarily blocked and compare algorithm runtime on larger random graphs.

#### Requisitos
O programa concluído deve:

- Add support for a `blocked_roads` list that excludes edges during path search
- Re-run route queries after blocking roads and explain route changes
- Generate random graphs with increasing size (for example 50, 200, and 1000 nodes)
- Measure runtime of BFS and Dijkstra for each graph size
- Print a short analysis (3-6 lines) explaining when each algorithm is most useful
