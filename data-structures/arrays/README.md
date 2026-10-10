# Arrays

Arrays store elements in an indexed sequence. In lower-level languages, a conventional array generally occupies contiguous memory and often has a fixed length. Python lists, Java `ArrayList`, and C++ `std::vector` are dynamic-array abstractions that manage capacity and may allocate new storage as they grow.

## Key characteristics

- **Indexed access:** O(1) for a valid index.
- **Sequential storage:** contiguous element slots in conventional arrays and dynamic-array buffers.
- **Dynamic capacity:** dynamic arrays may reallocate when capacity is exhausted.
- **Shifting:** inserting or deleting near the beginning or middle usually shifts elements.
- **Cache locality:** sequential traversal is often efficient due to locality.

## Operation complexity

| Operation | Typical dynamic-array complexity | Notes |
|---|---:|---|
| Access/update by index | O(1) | Assumes valid index |
| Linear search | O(n) | Unsorted data |
| Binary search | O(log n) | Input must be sorted |
| Append | Amortized O(1) | Occasional resize costs O(n) |
| Insert/delete at an arbitrary position | O(n) | Elements may need shifting |
| Traverse | O(n) | Visits each element |
| Reverse in place | O(n) time, O(1) extra space | Two pointers |
| Rotate in place | O(n) time, O(1) extra space | Three-reversal method |

## Common patterns

1. **Two pointers** — pair ends, reverse, partition, or compare sequences.
2. **Sliding window** — maintain a moving contiguous range.
3. **Prefix sums** — answer range-sum queries or track cumulative totals.
4. **Hash-based lookup** — complement lookup, frequency counting, and deduplication.
5. **Binary search** — exploit sorted order or a monotonic predicate.
6. **In-place transformations** — reduce auxiliary memory by overwriting safely.

## Implementation

The [implementation](implementation/array_operations.py) demonstrates linear search, binary search, maximum lookup, in-place reversal, and right rotation. Run it with Python 3:

```bash
python data-structures/arrays/implementation/array_operations.py
```

Run the regression tests from the repository root:

```bash
python -m unittest discover -s data-structures/arrays/tests -v
```

## Examples and practice

- [Examples and edge-case walkthroughs](examples/README.md)
- [Practice roadmap](problems/README.md) grouped by technique. Keep platform submissions in `solutions/platforms/` and language-focused archives in `solutions/languages/`; this folder contains reusable knowledge rather than copied submissions.

## Edge cases to check

- Empty input and a one-element list
- Duplicate values and missing search targets
- Binary search on sorted input only
- Rotation by zero, by the list length, by more than the length, and by a negative amount
- In-place mutation versus returning a new list
- Already sorted, reverse-sorted, and all-equal values

## Further reading

- [GeeksforGeeks: Array Data Structure](https://www.geeksforgeeks.org/array-data-structure/)
- [LeetCode: Array](https://leetcode.com/tag/array/)
- [HackerRank: Arrays](https://www.hackerrank.com/domains/data-structures/arrays)
