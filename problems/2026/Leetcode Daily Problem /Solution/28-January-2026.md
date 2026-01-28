# 3651. Minimum Cost Path with Teleportations

## Problem Statement

Find the minimum cost to reach the bottom-right cell from top-left in an `m x n` grid where you can move right/down (costing the destination cell value) or teleport to any cell with smaller or equal value (free, max `k` times).

**Problem Link:** [LeetCode 3651 - Minimum Cost Path with Teleportations](https://leetcode.com/problems/minimum-cost-path-with-teleportations/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/28-January-2026.md)

---

## Solution

```python
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0, 0)]
        allcell = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        values = [val for val, _, _ in allcell]
        ptr = [0] * (k + 1)
        visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]
        while pq:
            c, i, j, t = heapq.heappop(pq)
            if i == m - 1 and j == n - 1:
                return c
            if visited[i][j][t]:
                continue
            visited[i][j][t] = True
            for di, dj in [(1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    heapq.heappush(pq, (c + grid[ni][nj], ni, nj, t))
            if t < k:
                while ptr[t] < len(allcell) and values[ptr[t]] <= grid[i][j]:
                    _, x, y = allcell[ptr[t]]
                    heapq.heappush(pq, (c, x, y, t + 1))
                    ptr[t] += 1
        return -1
```

### Idea

* Use **Dijkstra's algorithm** with state `(cost, i, j, teleports_used)`
* **Pre-process:** Sort all cells by their values in ascending order
* **State space:** Track position `(i, j)` and number of teleportations used `t`
* **Two types of transitions:**
  1. **Normal move:** Move right or down, add destination cell value to cost
  2. **Teleportation:** Jump to any cell with value ≤ current cell value, cost is `0`, increment teleport count
* **Optimization with pointers:** Maintain separate pointers `ptr[t]` for each teleportation level to avoid re-processing cells
  - When at cell with value `v` and `t` teleports used, add all unvisited cells with value ≤ `v` to the priority queue
  - Use pointer to track which cells have already been added at this teleportation level
* **3D visited array:** `visited[i][j][t]` prevents revisiting same state
* **Early termination:** Return cost when reaching `(m-1, n-1)` with any number of teleports

### Complexity

* **Time:** `O(m × n × k × log(m × n × k))` - Priority queue operations
* **Space:** `O(m × n × k)` - Visited array and priority queue
