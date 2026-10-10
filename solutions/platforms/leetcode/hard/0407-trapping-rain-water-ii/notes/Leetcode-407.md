# LeetCode 407: Trapping Rain Water II

[![LeetCode](https://img.shields.io/badge/LeetCode-407-blue)](https://leetcode.com/problems/trapping-rain-water-ii/)

---

## Problem

Given an `m x n` integer matrix `heightMap` representing the height of each cell, compute **how much water it can trap after raining**.

- Water can only be trapped if surrounded by higher walls.
- Cells on the border cannot trap water.

---

## Solution: Min-Heap + BFS Traversal

**Idea:**  

- Start from the boundary cells (cannot trap water).  
- Use a min-heap (priority queue) to always process the lowest boundary cell first.  
- Perform BFS from each popped cell, expanding to neighbors:  
  - If a neighbor is lower than the current max boundary height, it can trap water.  
  - Push neighbor into the heap with updated height (`max(current, neighbor)`) and mark as visited.

```python
from heapq import heappush, heappop
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        ROWS, COLS = len(heightMap), len(heightMap[0])
        min_heap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS-1] or c in [0, COLS-1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        water = 0
        max_h = -1
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            water += max_h - h
            neighbors = [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]
            for nr, nc in neighbors:
                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or heightMap[nr][nc] == -1):
                    continue
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return water
```

---

### Complexity Analysis

- **Time Complexity:** O(m * n * log(m * n))  
  Each cell is pushed and popped from the heap once.
- **Space Complexity:** O(m * n)  
  Min-heap storage and visited marking.

---

## Key Insights

- **BFS** ensures all neighbors are explored in increasing boundary height order.
- **Min-Heap** guarantees we always process the lowest height, which is critical for correct water trapping calculation.
- **Visited marking** prevents revisiting cells, maintaining correctness and efficiency.

---

## Tags

#matrix #heap #bfs #priority-queue #simulation #hard
