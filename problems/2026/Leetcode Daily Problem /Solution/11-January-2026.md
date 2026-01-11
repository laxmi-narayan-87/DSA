# 85. Maximal Rectangle

## Problem Statement

Given a `rows x cols` binary matrix filled with `0`'s and `1`'s, find the **largest rectangle** containing only `1`'s and return its **area**.

**Problem Link:** [LeetCode 85 - Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/11-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        
        for row in matrix:
            for i in range(n):
                # Update heights:  increment if '1', reset to 0 if '0'
                heights[i] = heights[i] + 1 if row[i] == "1" else 0
            
            # Calculate max rectangle using histogram approach
            stack = [-1]
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]: 
                    h = heights[stack. pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        
        return max_area
```

### Idea

* Treat the problem as **multiple "Largest Rectangle in Histogram" problems**
* For each row, maintain a `heights` array representing histogram heights: 
  - If `matrix[row][col] == '1'`: increment the height
  - If `matrix[row][col] == '0'`: reset height to 0
* For each row, calculate the maximum rectangle area using the histogram approach: 
  - Use a **monotonic stack** to find the largest rectangle
  - When a smaller height is encountered, pop from stack and calculate area
  - Width = current index - previous index in stack - 1
* Track the maximum area across all rows

### Complexity

* **Time:** `O(rows × cols)` - process each cell once and each histogram calculation is O(cols)
* **Space:** `O(cols)` - heights array and stack
