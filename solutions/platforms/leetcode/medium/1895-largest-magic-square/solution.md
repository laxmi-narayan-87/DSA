# 1895. Largest Magic Square

## Problem Statement

A `k x k` **magic square** is a `k x k` grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. Given an `m x n` integer grid, return the **size** (i.e., the side length `k`) of the **largest magic square** that can be found within this grid. 

**Problem Link:** [LeetCode 1895 - Largest Magic Square](https://leetcode.com/problems/largest-magic-square/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/18-January-2026.md)

---

## Solution

```python
from typing import List

class Solution: 
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        def is_magic_square(grid:  List[List[int]], row:  int, col: int, k:  int) -> bool:
            # Get the target sum from the first row
            target = sum(grid[row][col:col + k])
            
            # Check all row sums
            for i in range(row, row + k):
                if sum(grid[i][col:col + k]) != target:
                    return False
            
            # Check all column sums
            for j in range(col, col + k):
                if sum(grid[i][j] for i in range(row, row + k)) != target:
                    return False
            
            # Check main diagonal (top-left to bottom-right)
            if sum(grid[row + i][col + i] for i in range(k)) != target:
                return False
            
            # Check anti-diagonal (top-right to bottom-left)
            if sum(grid[row + i][col + k - i - 1] for i in range(k)) != target:
                return False
            
            return True
        
        m, n = len(grid), len(grid[0])
        
        # Try from largest to smallest possible square size
        for k in range(min(m, n), 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic_square(grid, i, j, k):
                        return k
        
        return 1  # At minimum, a 1x1 square is always magic

```

### Idea

* Use **Brute Force with Early Termination** - start from the largest possible size
* **Algorithm:**
  1. Try square sizes from `min(m, n)` down to 1 (largest first)
  2. For each size `k`, check all possible top-left positions `(i, j)`
  3. For each position, verify if it forms a magic square: 
     - Calculate target sum from the first row
     - Check all row sums equal target
     - Check all column sums equal target
     - Check both diagonal sums equal target
  4. Return the first (largest) `k` that forms a magic square
* **Optimization:** Since we search from largest to smallest, return immediately when found

### Example Walkthrough

For `grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]`:
- Try k=4: No 4×4 magic square found
- Try k=3: Check position (1,1):
  - Rows: 5+1+6=12, 5+4+3=12, 2+7+3=12 ✓
  - Cols: 5+5+2=12, 1+4+7=12, 6+3+3=12 ✓
  - Diagonals: 5+4+3=12, 6+4+2=12 ✓
  - Found!  Return 3

### Complexity

* **Time:** `O(m × n × min(m,n)⁴)` - O(mn) positions × O(min(m,n)) sizes × O(min(m,n)³) to check each square
* **Space:** `O(1)` - only using constant extra space

### Optimization Note
This solution can be optimized using **prefix sums** to check row/column sums in O(1) time, reducing overall complexity to `O(m × n × min(m,n)²)`.
