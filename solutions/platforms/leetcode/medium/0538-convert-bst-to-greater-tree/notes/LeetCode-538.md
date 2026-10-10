# LeetCode 538: Convert BST to Greater Tree

[![LeetCode](https://img.shields.io/badge/LeetCode-538-blue)](https://leetcode.com/problems/convert-bst-to-greater-tree/)

---

## Problem

Given the root of a Binary Search Tree (BST), convert it to a **Greater Tree** such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

---

## Examples

### Example 1

**Input Tree:**
```
    4
   / \
  1   6
 / \ / \
0  2 5  7
    \     \
     3     8
```

**Output Tree:**
```
    30
   /  \
 36    21
/ \   / \
36 35 26 15
   \      \
   33      8
```

---

### Example 2

**Input:** `root = [0, null, 1]`  
**Output:** `[1, null, 1]`

---

## Approach 1: Reverse Inorder Traversal (Optimal ⭐)

We leverage the **BST property** (inorder traversal gives sorted ascending order).  
If we traverse **right → root → left**, we get values in descending order.  
While traversing, keep a running sum and update each node.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        # Traverse right subtree first
        self.convertBST(root.right)
        
        # Update running sum and modify node
        self.sum += root.val
        root.val = self.sum
        
        # Then traverse left subtree
        self.convertBST(root.left)
        
        return root
```

---

## Approach 2: Iterative Reverse Inorder with Stack

Instead of recursion, simulate with a stack.

```python
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left

        return root
```

---

## Complexity Analysis

- **Time Complexity:** O(n) (visit each node once)
- **Space Complexity:**
  - Recursion: O(h) where h = tree height (worst case O(n))
  - Iterative stack: O(h)

---

## Walkthrough Example

**Input:** `[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`

**Steps:**
1. Traverse to rightmost → start with 8, sum = 8
2. Node 7 → sum = 15 → update node = 15
3. Node 6 → sum = 21 → update node = 21
4. Node 5 → sum = 26 → update node = 26
5. Node 4 → sum = 30 → update node = 30
6. Continue left subtree → update values accordingly

---

## Edge Cases

- Empty tree (`[]`) → return `[]`
- Single node tree → node value stays the same
- Skewed tree (all right or all left) → still works with recursion/stack

---

## Related Topics

- Binary Search Trees
- Tree Traversals
- Inorder / Reverse Inorder
- Recursion / Iterative DFS

---

## Tags

#bst #binary-tree #dfs #inorder #recursion #medium
