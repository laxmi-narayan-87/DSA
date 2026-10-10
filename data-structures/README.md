# Data Structures

This directory holds reusable data-structure explanations, complexity notes, implementation examples, and practice-topic indexes. Platform-specific submissions remain in `solutions/platforms/`; language archives remain in `solutions/languages/`.

## Categories

### Linear structures

- **[Arrays](arrays/README.md)** — indexed contiguous collections; random access is O(1).
- **[Linked Lists](linked-lists/README.md)** — nodes connected by references; useful for pointer and two-pointer patterns.
- **Stacks** — LIFO collections used in parsing, DFS, and monotonic-stack problems.
- **Queues** — FIFO collections used in BFS and scheduling.

### Non-linear structures

- **[Trees](trees/README.md)** — hierarchical structures, traversals, search trees, and balanced trees.
- **[Graphs](graphs/README.md)** — vertices and edges, traversal, connectivity, shortest paths, and spanning trees.
- **Heaps** — priority-oriented complete trees.
- **Hash Tables** — key-value lookup using hashing.

## Recommended learning order

1. Arrays and basic complexity analysis
2. Linked lists, pointers, and two-pointer techniques
3. Stacks and queues
4. Trees and recursive/iterative traversals
5. Graphs and BFS/DFS
6. Heaps, hash tables, and advanced structures

## Folder conventions

Each topic folder uses the same layout where appropriate:

- `README.md` — theory, operation/algorithm complexity, patterns, and links.
- `implementation/` — small runnable reference implementations.
- `problems/README.md` — curated practice topics, not duplicate submissions.
- `examples/README.md` — walkthroughs and edge cases.
- `notes/` — focused deep dives for specialized variants.

## Complexity reminder

Complexity depends on the exact representation and operation. State assumptions (for example, whether a linked list maintains a tail, whether a tree is balanced, and whether a graph uses an adjacency list) instead of presenting a single complexity as universal.

## Related sections

- [Algorithm guides](../algorithms/README.md)
- [Platform submissions](../solutions/platforms/)
- [Language archives](../solutions/languages/)
- [Repository structure](../docs/REPOSITORY_STRUCTURE.md)
