# 712. Minimum ASCII Delete Sum for Two Strings

## Problem Statement

Given two strings `s1` and `s2`, return the **lowest ASCII sum of deleted characters** to make two strings equal.

**Problem Link:** [LeetCode 712 - Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/10-January-2026.md)

---

## Solution

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize first column:  delete all characters from s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        
        # Initialize first row:  delete all characters from s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match, no deletion needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose minimum:  delete from s1 or delete from s2
                    dp[i][j] = min(
                        dp[i - 1][j] + ord(s1[i - 1]),  # Delete from s1
                        dp[i][j - 1] + ord(s2[j - 1])   # Delete from s2
                    )
        
        return dp[m][n]
```

### Idea

* Use **Dynamic Programming** with a 2D table: 
  - `dp[i][j]` = minimum ASCII delete sum to make `s1[0:i]` and `s2[0:j]` equal
* **Base cases:**
  - `dp[i][0]` = sum of ASCII values of first `i` characters of `s1` (delete all from s1)
  - `dp[0][j]` = sum of ASCII values of first `j` characters of `s2` (delete all from s2)
* **Recurrence relation:**
  - If `s1[i-1] == s2[j-1]`: characters match, no deletion needed → `dp[i][j] = dp[i-1][j-1]`
  - Otherwise, take minimum of:
    - Delete from `s1`: `dp[i-1][j] + ord(s1[i-1])`
    - Delete from `s2`: `dp[i][j-1] + ord(s2[j-1])`
* The answer is `dp[m][n]`

### Complexity

* **Time:** `O(m × n)` - fill the entire DP table
* **Space:** `O(m × n)` - store the DP table
