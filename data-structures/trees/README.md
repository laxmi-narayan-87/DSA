# Trees

A tree is a connected, acyclic hierarchical structure. The first node is the **root**; links point to child nodes. A node with no children is a **leaf**. The depth of a node counts edges from the root, while the height of a node counts edges on its longest downward path to a leaf (state the convention used when solving problems).

## Core terminology

- **Parent / child / sibling** — immediate relationships between nodes.
- **Subtree** — a node and all its descendants.
- **Binary tree** — each node has at most two children.
- **Binary search tree (BST)** — keys follow an ordering rule; duplicates require a clearly defined policy.
- **Balanced tree** — height is kept logarithmic or close to logarithmic by structural rules.
- **Heap** — complete binary tree obeying a min-heap or max-heap order; distinct from a BST.

## Traversals

| Traversal | Order | Common use |
|---|---|---|
| Preorder | Node, left, right | Copying/serializing a tree |
| Inorder | Left, node, right | Sorted order for a BST |
| Postorder | Left, right, node | Deleting/evaluating subtrees |
| Level order | Breadth-first by level | Minimum-depth and level-based tasks |

## Complexity guide

For a tree with n nodes and height h, traversal generally takes O(n) time and O(h) recursion stack space. BST search/insert/delete take O(h): O(log n) when balanced, but O(n) in a skewed tree. Self-balancing trees maintain O(log n) operations.

## Common patterns

1. Recursive DFS with a base case for an empty node.
2. Iterative DFS using a stack; BFS using a queue.
3. Return information upward from children (height, balance, subtree sums).
4. Compare mirrored children for symmetry.
5. Use BST bounds rather than checking only a node's immediate children.
6. Use a parent map or ancestor stack for lowest common ancestor variants.

## Existing in-depth notes

- [B-Tree](notes/B_Tree.md) — multiway search tree used in storage systems.
- [Red-Black Tree](notes/red_Black_Tree.md) — balanced binary search tree with color invariants.
- [Skip List](notes/Skip_List.md) — probabilistic ordered structure (not technically a tree, retained here from the existing archive for continuity).

## Implementation

- [Binary tree and BST traversals](implementation/tree_traversals.py)

## Practice topics

See [problems/README.md](problems/README.md). Platform submissions remain in the platform archive rather than being duplicated here.
