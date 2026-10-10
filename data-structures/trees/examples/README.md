# Tree Examples

Use the sample BST in [the implementation](../implementation/tree_traversals.py) to manually trace each traversal.

- **Inorder:** visits left subtree, node, right subtree; a BST yields sorted values.
- **Preorder:** visits node before descendants; useful when serializing with null markers.
- **Postorder:** visits descendants before the node; useful for bottom-up calculations.
- **Level order:** uses a queue and visits nodes breadth-first.

Test empty trees, a single node, a fully skewed tree, repeated values according to your policy, and a balanced tree. A recursive solution may overflow the call stack on a very deep skewed tree; consider iterative traversal when input size requires it.
