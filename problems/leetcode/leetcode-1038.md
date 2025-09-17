# LeetCode 1038: Binary Search Tree to Greater Sum Tree

[![LeetCode](https://img.shields.io/badge/LeetCode-1038-green)](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

---

## Problem

Given the root of a Binary Search Tree (BST), convert it into a **Greater Sum Tree (GST)** where every node's value is replaced by the sum of all values greater than or equal to the node's original value.

This is similar to **LeetCode 538: Convert BST to Greater Tree**, with the definition of "greater sum" slightly adjusted to include the node itself.

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

- A **BST** in inorder → ascending sorted values.  
- Traversing **right → root → left** visits nodes in descending order.  
- Maintain a running sum and update each node's value.

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

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        # Traverse right subtree
        self.bstToGst(root.right)
        
        # Update running sum and node value
        self.sum += root.val
        root.val = self.sum
        
        # Traverse left subtree
        self.bstToGst(root.left)
        
        return root
```

---

## Approach 2: Iterative Reverse Inorder with Stack

Instead of recursion, simulate reverse inorder traversal using a stack.

```python
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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

- **Time Complexity:** O(n) (every node visited once)
- **Space Complexity:**  
  - Recursion: O(h) where h is tree height (worst O(n))  
  - Iterative stack: O(h)

---

## Walkthrough Example

**Input:** `[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`

**Steps:**
1. Visit 8 → sum = 8 → update 8
2. Visit 7 → sum = 15 → update 15
3. Visit 6 → sum = 21 → update 21
4. Visit 5 → sum = 26 → update 26
5. Visit 4 → sum = 30 → update 30
6. Continue left side → update accordingly

Final tree matches expected output.

---

## Edge Cases

- Empty tree → return None
- Single node → value stays the same
- Skewed tree (all nodes to one side) → still works

---

## Related Topics

- Binary Search Trees
- Tree Traversals
- Reverse Inorder
- Recursion / Iteration

---

## Tags

#bst #binary-tree #dfs #recursion #inorder #medium
