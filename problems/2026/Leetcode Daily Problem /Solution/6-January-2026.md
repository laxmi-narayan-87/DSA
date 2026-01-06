# 1161. Maximum Level Sum of a Binary Tree

## Problem Statement

Given the `root` of a binary tree, return the **smallest level `x`** such that the **sum of all node values at level `x` is maximum**. The root is at level 1, its children are at level 2, and so on.

**Problem Link:** [LeetCode 1161 - Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/6-January-2026.md)

---

## Solution

```python
from collections import deque

# Definition for a binary tree node. 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        max_sum = float('-inf')
        result_level = 1
        
        while queue: 
            level_sum = 0
            for _ in range(len(queue)):
                node = queue. popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                result_level = level
            level += 1
        
        return result_level
```

### Idea

* Use **BFS (Breadth-First Search)** with a queue to traverse the tree level by level
* For each level: 
  - Calculate the sum of all node values at that level
  - Compare with the current maximum sum
  - If current level sum is greater, update the result level
* Track the level number (starting from 1) and return the level with maximum sum
* Since we process levels from top to bottom, we automatically get the smallest level in case of ties

### Complexity

* **Time:** `O(n)` - visit each node exactly once
* **Space:** `O(w)` - where w is the maximum width of the tree (queue size)
