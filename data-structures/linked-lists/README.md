# Linked Lists

A linked list stores values in nodes connected by references. Unlike arrays, nodes do not need contiguous memory. This makes local insertion and deletion convenient when the relevant node is already known, but indexed access requires traversal.

## Node model

A singly linked node contains a value and a reference to the next node. A doubly linked node also points to the previous node. The list maintains a head reference and may optionally maintain a tail and length.

## Variants

- **Singly linked list** — each node points forward; simple and memory-efficient.
- **Doubly linked list** — supports traversal in both directions at the cost of an extra reference per node.
- **Circular linked list** — the final node links back to the first node; traversal must use a stopping condition other than reaching `None`.

## Operation complexity

| Operation | Singly linked list | Notes |
|---|---:|---|
| Access by index | O(n) | Traverse from the head |
| Search by value | O(n) | Worst case visits every node |
| Insert at head | O(1) | Update the head reference |
| Insert after a known node | O(1) | Does not include finding the node |
| Delete head | O(1) | Advance the head |
| Delete by value | O(n) | Usually find the predecessor first |
| Append | O(n), or O(1) with tail | Depends on whether a tail is maintained |

## Core patterns

1. **Two pointers** — slow/fast pointers find a midpoint or detect a cycle.
2. **Dummy/sentinel node** — simplifies edge cases around head insertion and deletion.
3. **In-place reversal** — maintain previous, current, and next references.
4. **Merge sorted lists** — advance the pointer with the smaller value.
5. **Cycle detection** — Floyd's tortoise-and-hare algorithm uses O(1) extra space.
6. **Intersection** — align lengths or switch traversal heads.

## Implementation

- [Singly linked list implementation](implementation/singly_linked_list.py)

## Practice topics

See [problems/README.md](problems/README.md) for a progression of common interview patterns. Problem-specific submissions remain in `solutions/platforms/` and `solutions/languages/`; this folder is for reusable learning notes and examples.

## Common pitfalls

- Losing the remainder of a list by overwriting a reference too early.
- Forgetting empty-list and single-node cases.
- Creating accidental cycles during reversal or insertion.
- Assuming deletion is O(1) when the node must first be located.
- Failing to update both head and tail for an empty or one-element list.

## Further reading

- [GeeksforGeeks: Linked List Data Structure](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [LeetCode: Linked List](https://leetcode.com/tag/linked-list/)
