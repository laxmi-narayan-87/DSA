# 865. Smallest Subtree with all the Deepest Nodes

## Problem Statement

Given the `root` of a binary tree, return the **smallest subtree** such that it contains **all the deepest nodes** in the original tree.  A node is called the deepest if it has the largest depth possible among any node in the entire tree. 

**Problem Link:** [LeetCode 865 - Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/09-January-2026.md)

> **Note:** This question is the same as [1123: Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

---

## Solution

```python
from typing import Optional

# Definition for a binary tree node. 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (None, 0)
            
            left, left_depth = dfs(node.left)
            right, right_depth = dfs(node.right)
            
            if left_depth > right_depth: 
                return (left, left_depth + 1)
            elif left_depth < right_depth: 
                return (right, right_depth + 1)
            else:
                return (node, left_depth + 1)
        
        return dfs(root)[0]
```

### Idea

* Use **DFS (Depth-First Search)** to traverse the tree and return both: 
  - The subtree root containing all deepest nodes
  - The depth of that subtree
* For each node, compare the depths of left and right subtrees: 
  - If **left is deeper:** All deepest nodes are in the left subtree
  - If **right is deeper:** All deepest nodes are in the right subtree
  - If **both are equal:** Current node is the LCA (Lowest Common Ancestor) of all deepest nodes
* Return the node and its depth + 1 (accounting for current level)
* The final answer is the node returned from the root

### Complexity

* **Time:** `O(n)` - visit each node exactly once
* **Space:** `O(h)` - recursion stack where h is the height of the tree
