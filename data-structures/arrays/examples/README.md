# Array Examples and Edge Cases

Run the examples in [implementation/array_operations.py](../implementation/array_operations.py).

## Right rotation

For `[1, 2, 3, 4, 5]` rotated right by 2, the result is `[4, 5, 1, 2, 3]`. The three-reversal method reverses the entire list, then the first k elements, then the remaining elements. The implementation reverses index ranges directly so it mutates the original list without creating slices.

## Expected edge cases

| Input | Operation | Expected result |
|---|---|---|
| `[]` | rotate by 3 | `[]` |
| `[7]` | rotate by 9 | `[7]` |
| `[1, 2, 3]` | rotate by 0 | `[1, 2, 3]` |
| `[1, 2, 3]` | rotate by 3 | `[1, 2, 3]` |
| `[1, 2, 3]` | rotate by -1 | `[2, 3, 1]` |
| `[2, 2, 2]` | binary search for 2 | Any valid matching index |

Binary search requires sorted input. If duplicates exist, the provided implementation returns a matching index, not necessarily the first or last occurrence.
