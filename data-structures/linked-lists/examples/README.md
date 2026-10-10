# Linked List Examples

Small traces and edge cases to work through before coding.

## Reversal trace

For `A → B → C → None`, repeatedly save the next node, point the current node backward, then advance both pointers. The final head is `C`; no nodes should be lost.

## Essential edge cases

- Empty list
- One node
- Two nodes
- Target is at the head, middle, tail, or absent
- Duplicate values
- Delete the only node, then append again
- Reverse twice and confirm the original order is restored

The runnable implementation is in [implementation/](../implementation/).
