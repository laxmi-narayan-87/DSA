# 1339. Maximum Product of Splitted Binary Tree

## Problem Statement

Given the `root` of a binary tree, split the tree into two subtrees by removing exactly one edge such that the product of the sums of the two resulting subtrees is maximized. Return the maximum product modulo `10^9 + 7`.

**Problem Link:** [LeetCode 1339 - Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/7-January-2026.md)

---

## Solution

```python

# Definition for a binary tree node. 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self. left = left
#         self. right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        subtree = []
        
        def dfs(node):
            if not node: 
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            subtree.append(s)
            return s
        
        total = dfs(root)
        max_prod = max(s * (total - s) for s in subtree)
        return max_prod % MOD
```

### Idea

* Use **two-pass approach**:
  1. **First DFS pass:** Calculate the sum of each subtree and store all subtree sums
  2. **Calculate total sum:** The root's subtree sum equals the entire tree's sum
  3. **Find maximum product:** For each subtree with sum `s`, if we cut its edge, we get two parts: 
     - Subtree with sum `s`
     - Remaining tree with sum `total - s`
     - Product = `s × (total - s)`
* Find the maximum product among all possible cuts
* Return the result modulo `10^9 + 7`

### Complexity

* **Time:** `O(n)` - visit each node twice (once for calculating sums, once for finding max)
* **Space:** `O(n)` - store all subtree sums + recursion stack
