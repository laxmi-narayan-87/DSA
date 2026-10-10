# 3640. Trionic Array II

**Difficulty:** Hard  
**Topics:** Array, Dynamic Programming  
**Problem:** [LeetCode 3640 - Trionic Array II](https://leetcode.com/problems/trionic-array-ii/)

## Approach: Three-state dynamic programming

A valid trionic subarray has three consecutive phases:

1. Strictly increasing.
2. Strictly decreasing.
3. Strictly increasing.

For each index `i`, track the best sum of a valid partial pattern ending at `i`:

- `inc[i]`: an increasing subarray containing at least one increasing edge.
- `inc_dec[i]`: an increasing-then-decreasing subarray, with both phases non-empty.
- `trionic[i]`: a complete increasing-decreasing-increasing subarray.

Only the adjacent comparison between `nums[i - 1]` and `nums[i]` determines which state can be extended. Initialize unreachable states to negative infinity; this is important because values may be negative and the best valid answer may also be negative.

## Python solution

```python
from typing import List


class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        negative_infinity = -(10**30)
        inc = [negative_infinity] * len(nums)
        inc_dec = [negative_infinity] * len(nums)
        trionic = [negative_infinity] * len(nums)
        answer = negative_infinity

        for i in range(1, len(nums)):
            previous, current = nums[i - 1], nums[i]

            if previous < current:
                # Start or extend the first increasing phase.
                inc[i] = max(previous + current, inc[i - 1] + current)

                # Start or extend the final increasing phase.
                trionic[i] = max(
                    inc_dec[i - 1] + current,
                    trionic[i - 1] + current,
                )

            elif previous > current:
                # Start the decreasing phase or continue it.
                inc_dec[i] = max(
                    inc[i - 1] + current,
                    inc_dec[i - 1] + current,
                )

            answer = max(answer, trionic[i])

        return answer
```

## Examples

```text
Input: nums = [0,-2,-1,-3,0,2,-1]
Output: -4
```

One valid subarray is `[-2, -1, -3, 0, 2]`, whose sum is `-4`.

```text
Input: nums = [1,4,2,7]
Output: 14
```

The entire array is trionic: `1 < 4 > 2 < 7`.

## Complexity

- **Time:** `O(n)` — one pass through the array.
- **Auxiliary space:** `O(n)` — three DP arrays.

## Edge cases to test

- A valid trionic array whose sum is negative.
- Strict comparisons: equal adjacent values must not extend any phase.
- The shortest valid input, such as `[1, 4, 2, 7]`.
- Values near the constraints, where the sum exceeds 32-bit integer range in languages with fixed-width integers.
