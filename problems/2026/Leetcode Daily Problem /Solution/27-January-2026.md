# 3650. Minimum Cost Path with Edge Reversals

## Problem Statement

Find the minimum cost to travel from node `0` to node `n - 1` in a directed weighted graph where you can reverse any incoming edge at double the cost.

**Problem Link:** [LeetCode 3650 - Minimum Cost Path with Edge Reversals](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/27-January-2026.md)

---

## Solution

```python
class Solution:
    def dijkstra(self, n: int) -> int:
        INF  = 10**9
        vis  = [False] * n
        dist = [INF] * n
        pq: List[Tuple[int, int]] = [(0, 0)]
        dist[0] = 0
        while pq:
            du, u = heapq.heappop(pq)
            if vis[u]:
                continue
            vis[u] = True
            for v, w in self.G[u]:
                nd = du + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return -1 if dist[n - 1] == INF else dist[n - 1]

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        self.G = [[] for _ in range(n)]
        for u, v, w in edges:
            self.G[u].append((v, w))
            self.G[v].append((u, 2 * w))
        return self.dijkstra(n)
```

### Idea

* **Key Insight:** Model all possible moves (normal + reversed) as edges in a modified graph.
* For each directed edge `u → v` with cost `w`:
  - Add forward edge `u → v` with cost `w` (using the edge normally)
  - Add reverse edge `v → u` with cost `2 * w` (simulating the switch reversal)
* **Why this works:**
  - Original edge usage: Direct traversal from `u` to `v` costs `w`
  - Reversed edge usage: If at node `v`, we can "reverse" the incoming edge and go back to `u` at cost `2 * w`
  - Dijkstra automatically chooses the cheapest option at each step
  - No need to explicitly track which switches are used—Dijkstra's greedy nature ensures optimal path selection
* Run **Dijkstra's algorithm** to find shortest path from node `0` to node `n - 1`.

### Complexity

* **Time:** `O((V + E) log V)` - Dijkstra with priority queue
* **Space:** `O(V + E)` - Adjacency list and auxiliary structures
