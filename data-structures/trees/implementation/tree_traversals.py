"""Binary-tree traversal and BST examples."""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import Optional, Iterator


@dataclass
class TreeNode:
    value: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def preorder(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def level_order(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result


def bst_insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)
    # This example ignores duplicates; choose a policy for production use.
    return root


if __name__ == "__main__":
    root: Optional[TreeNode] = None
    for value in (8, 3, 10, 1, 6, 14, 4, 7, 13):
        root = bst_insert(root, value)
    print(preorder(root))
    print(inorder(root))       # sorted values for a BST
    print(postorder(root))
    print(level_order(root))
