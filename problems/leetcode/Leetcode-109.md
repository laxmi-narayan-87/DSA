# LeetCode 109 - Convert Sorted List to Binary Search Tree

## Problem Statement

Given the `head` of a singly linked list where elements are sorted in **ascending order**, convert it to a height-balanced **Binary Search Tree (BST)**.

- A height-balanced BST is a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

**Link:** [LeetCode 109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

---

## Examples

### Example 1

**Input:**
```
head = [-10,-3,0,5,9]
```

**Output (One possible BST):**
```
     0
    / \
  -3   9
  /   /
-10  5
```

### Example 2

**Input:**
```
head = []
```

**Output:**
```
[]
```

---

## Approach 1: Fast & Slow Pointer (In-place)

We use the **fast & slow pointer technique** to find the middle element of the linked list, which becomes the root of the BST.

- The left half forms the left subtree.
- The right half forms the right subtree.
- Recursively repeat until the list is exhausted.

**Time Complexity:** `O(n log n)`  
**Space Complexity:** `O(log n)` (recursion stack)

### Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next

        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if head != slow else None)
        root.right = self.sortedListToBST(slow.next)

        return root
```

---

## Approach 2: Array Conversion

We first convert the linked list into an **array** and then use the standard **sorted array to BST** construction.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(n)`

### Code

```python
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        val = []
        node = head
        while node:
            val.append(node.val)
            node = node.next

        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            root = TreeNode(val[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(val) - 1)
```

---

## Visual Explanation

### Example Walkthrough (`head = [-10,-3,0,5,9]`)

1. Convert linked list to BST:
    ```
    Linked List:  -10 -> -3 -> 0 -> 5 -> 9
    Mid = 0 → Root = 0
    ```

2. Left side: `[-10, -3]`
    ```
    Mid = -3 → Left child = -3
    Left of -3 = -10
    ```

3. Right side: `[5, 9]`
    ```
    Mid = 9 → Right child = 9
    Left of 9 = 5
    ```

### Final BST

```
       0
      / \
    -3   9
    /   /
 -10   5
```

---

## Key Takeaways

- **Fast & Slow pointer** avoids extra space, directly splits the list.
- **Array conversion** is simpler but uses extra memory.
- Both ensure a **balanced BST**.

---
