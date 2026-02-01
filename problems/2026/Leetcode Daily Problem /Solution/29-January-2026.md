# 2976. Minimum Cost to Convert String I

## Problem Statement

Find the minimum cost to convert string `source` to `target` where you can change characters using given transformations with specified costs, or return `-1` if impossible.

**Problem Link:** [LeetCode 2976 - Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/29-January-2026.md)

---

## Solution

```python
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for o, c, z in zip(original, changed, cost):
            u = ord(o) - 97
            v = ord(c) - 97
            dist[u][v] = min(dist[u][v], z)
        for k in range(26):
            for i in range(26):
                if dist[i][k] == inf:
                    continue
                for j in range(26):
                    if dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        total_cost = 0
        for s_char, t_char in zip(source, target):
            u = ord(s_char) - 97
            v = ord(t_char) - 97
            if u == v:
                continue
            if dist[u][v] == inf:
                return -1
            total_cost += dist[u][v]
        return total_cost
```

### Idea

* Build a graph where nodes are the 26 lowercase letters and edges represent character transformations with costs.
* Use **Floyd-Warshall algorithm** to compute the minimum cost to transform any character to any other character:
  - Initialize `dist[i][i] = 0` (no cost to keep same character)
  - For each transformation, store the minimum cost in `dist[u][v]`
  - For each intermediate character `k`, update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`
* After preprocessing, iterate through `source` and `target`:
  - If characters are the same, no cost needed
  - If `dist[s_char][t_char]` is infinity, transformation is impossible, return `-1`
  - Otherwise, add `dist[s_char][t_char]` to total cost
* **Key insight:** Pre-computing all shortest paths allows O(1) lookup per character conversion

### Complexity

* **Time:** `O(26³ + n)` = `O(n)` - Floyd-Warshall is constant time for 26 letters, plus linear scan of string
* **Space:** `O(26²)` = `O(1)` - Distance matrix is constant size
