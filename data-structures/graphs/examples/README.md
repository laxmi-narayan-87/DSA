# Graph Examples

For the graph in [implementation/graph_traversal.py](../implementation/graph_traversal.py), sketch the adjacency list and predict BFS/DFS order before running it.

## Edge cases to test

- Empty graph and missing start vertex
- Isolated vertex
- Disconnected components
- Self-loop and duplicate edge
- Directed edge that cannot be traversed backward
- Cycles (ensure traversal terminates)

## Algorithm selection

- Reachability or unweighted shortest path: BFS/DFS
- Dependency ordering: topological sort on a DAG
- Non-negative weighted shortest path: Dijkstra
- Negative edges: Bellman-Ford
- Minimum spanning tree: Kruskal or Prim
