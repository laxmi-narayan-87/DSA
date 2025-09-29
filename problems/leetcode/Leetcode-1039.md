# LeetCode 1039: Minimum Score Triangulation of Polygon

[![LeetCode](https://img.shields.io/badge/LeetCode-1039-blue)](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/)

---

## Problem

Given an array `values` representing the vertices of a convex polygon in order, find the minimum score to triangulate it.  
- The **score** of a triangle is the product of its three vertex values.  
- Triangulation is dividing the polygon into non-overlapping triangles using its vertices.  
- Return the **minimum total score** of all possible triangulations.

**Triangle Rule:** For any triangle `(i, k, j)`, score = `values[i] * values[k] * values[j]`.

---

## First Principles Breakdown

**Decompose:**  
- Any triangulation of a convex polygon can be built from smaller subpolygons by choosing a vertex `k` between `i` and `j` and forming a triangle `(i, k, j)`.
- The cost to triangulate from `i` to `j` is the cost to triangulate from `i` to `k`, plus from `k` to `j`, plus the triangle `(i, k, j)`.

**Atomic Operation:**  
- Each triangle's score is `values[i] * values[k] * values[j]`.

**Recursive Build:**  
- Try every possible `k` between `i` and `j` for every subpolygon, and take the minimum total score.

**Overlapping Subproblems:**  
- Many subpolygons are solved multiple times, so memoization or tabulation (DP) is essential for efficiency.

**Base Case:**  
- If the polygon has less than 3 vertices (`j - i < 2`), it cannot be triangulated (score 0).

---

## Examples

**Input:** `values = [1,2,3]`  
**Output:** `6`

**Input:** `values = [3,7,4,5]`  
**Output:** `144`

**Input:** `values = [1,3,1,4,1,5]`  
**Output:** `13`

---

## Approaches

### Approach 1: Brute Force (Recursive)

**Idea:**  
Try every possible way to split the polygon into triangles. For each segment `(i, j)`, recursively try all possible vertices `k` between `i` and `j` to make a triangle `(i, k, j)` and sum the minimal cost.

- Check all possible triangles recursively and compute total score.
- Time Complexity: O(3^n)  
- Space Complexity: O(n) (call stack)

```python
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        
        def solve(i, j):
            if j - i < 2:
                return 0
            ans = float('inf')
            for k in range(i + 1, j):
                score = solve(i, k) + solve(k, j) + values[i] * values[j] * values[k]
                ans = min(ans, score)
            return ans
        
        return solve(0, n - 1)
```

---

### Approach 2: Top-Down DP with Memoization

**Idea:**  
Use recursion as in brute force, but cache (`dp[i][j]`) answers for subproblems to avoid redundant computation.

- Same recursion as brute force, but store intermediate results to avoid recomputation.
- Time Complexity: O(n³)
- Space Complexity: O(n²) (DP table) + O(n) (recursion stack)

```python
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]
        
        def solve(i, j):
            if j - i < 2:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            ans = float('inf')
            for k in range(i + 1, j):
                score = solve(i, k) + solve(k, j) + values[i] * values[j] * values[k]
                ans = min(ans, score)
            dp[i][j] = ans
            return ans
        
        return solve(0, n - 1)
```

---

### Approach 3: Bottom-Up DP (Tabulation)

**Idea:**  
Build up the solution for small subpolygons to larger ones using a DP table. For each length, compute the minimum triangulation cost for each interval `(i, j)` by trying all possible middle vertices `k`.

- Fill DP table iteratively from smaller sub-polygons to larger ones.
- Time Complexity: O(n³)
- Space Complexity: O(n²)

```python
class Solution:
    def minScoreTriangulation(self, A: list[int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    score = dp[i][k] + dp[k][j] + A[i] * A[j] * A[k]
                    dp[i][j] = min(dp[i][j], score)
        
        return dp[0][n - 1]
```

---

## Key Insights

- **Decompose problem:** Solve for sub-polygons first.
- **Overlapping subproblems:** Top-down memoization reduces exponential recursion to cubic time.
- **Bottom-up approach:** Iteratively compute for increasing polygon lengths.
- **Triangle choice:** Try all possible middle vertices `k` to minimize score.

---

## Tags

#dynamic-programming #geometry #polygon #medium

---
