# Graphs

A graph is a set of vertices (nodes) connected by edges. Graphs model relationships such as routes, dependencies, networks, and state transitions.

## Graph types

- **Directed / undirected** — edges have a direction or can be traversed both ways.
- **Weighted / unweighted** — edges carry costs or all have equal cost.
- **Cyclic / acyclic** — a path may or may not return to a previously visited vertex.
- **Connected / disconnected** — in an undirected graph, whether every vertex can reach every other vertex.
- **DAG** — directed acyclic graph, useful for prerequisite and dependency ordering.

## Representations

| Representation | Space | Best fit |
|---|---:|---|
| Adjacency list | O(V + E) | Usually preferred for sparse graphs |
| Adjacency matrix | O(V²) | Dense graphs or frequent edge-existence checks |
| Edge list | O(E) | Edge-centric algorithms such as Kruskal's |

For an undirected graph, store each edge in both endpoint adjacency lists. For a directed graph, store only the outgoing edge unless the algorithm explicitly needs reverse edges.

## Essential algorithms

| Algorithm | Purpose | Typical complexity |
|---|---|---|
| BFS | Shortest path in an unweighted graph | O(V + E) |
| DFS | Reachability, components, cycle-related tasks | O(V + E) |
| Topological sort | Order vertices in a DAG | O(V + E) |
| Dijkstra | Single-source shortest paths with non-negative weights | O((V + E) log V) with a heap |
| Bellman-Ford | Shortest paths with negative edges; detect reachable negative cycles | O(VE) |
| Floyd-Warshall | All-pairs shortest paths | O(V³) |
| Kruskal / Prim | Minimum spanning tree | Commonly O(E log E) / heap-dependent |
| Union-Find | Maintain disjoint components | Near O(1) amortized per operation |

## Reliable workflow

1. Identify whether the graph is directed and/or weighted.
2. Decide how isolated vertices and disconnected components are represented.
3. Select a representation based on constraints.
4. Track visited state to avoid revisiting vertices indefinitely.
5. Choose the algorithm that matches the weight constraints: BFS for unweighted shortest paths; Dijkstra only when weights are non-negative.
6. Analyze complexity in terms of V (vertices) and E (edges).

## Implementation

- [Adjacency-list graph with BFS and DFS](implementation/graph_traversal.py)

## Practice topics

See [problems/README.md](problems/README.md). Keep platform submissions in `solutions/platforms/` and language archives in `solutions/languages/`.
