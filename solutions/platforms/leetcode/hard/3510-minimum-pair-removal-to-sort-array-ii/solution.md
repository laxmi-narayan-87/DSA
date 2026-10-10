# 3510. Minimum Pair Removal to Sort Array II

## Problem Statement

Given an array `nums`, you can perform the following operation any number of times:

- Select the adjacent pair with the minimum sum in `nums`. If multiple such pairs exist, choose the leftmost one.
- Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

**Problem Link:** [LeetCode 3510 - Minimum Pair Removal to Sort Array II](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/23-January-2026.md)

---

## Solution

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        arr = [int(x) for x in nums]
        removed = [False] * n
        heap = []
        asc = 0
        for i in range(1, n):
            heapq.heappush(heap, (arr[i - 1] + arr[i], i - 1))
            if arr[i] >= arr[i - 1]:
                asc += 1
        if asc == n - 1:
            return 0

        rem = n
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]

        while rem > 1:
            if not heap:
                break
            sumv, left = heapq.heappop(heap)
            right = nxt[left]
            if right >= n or removed[left] or removed[right] or arr[left] + arr[right] != sumv:
                continue
            pre = prev[left]
            after = nxt[right]

            if arr[left] <= arr[right]:
                asc -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                asc -= 1
            if after != n and arr[right] <= arr[after]:
                asc -= 1

            arr[left] += arr[right]
            removed[right] = True
            rem -= 1

            if pre != -1:
                heapq.heappush(heap, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    asc += 1
            else:
                prev[left] = -1

            if after != n:
                prev[after] = left
                nxt[left] = after
                heapq.heappush(heap, (arr[left] + arr[after], left))
                if arr[left] <= arr[after]:
                    asc += 1
            else:
                nxt[left] = n

            if asc == rem - 1:
                return n - rem

        return n
```

### Idea

* Use a **min-heap** to efficiently find the adjacent pair with the minimum sum.
* Track all adjacent pairs in the heap initially.
* Maintain `prev` and `nxt` arrays to handle the linked list of active elements after merging.
* Keep count of **ascending pairs** (`asc`) to check if array is non-decreasing.
* For each operation:
  * Extract the minimum sum pair from heap.
  * Validate the pair is still valid (not removed, sum matches).
  * Update the ascending count by removing old relationships.
  * Merge the pair by replacing left element with sum and marking right as removed.
  * Add new adjacent pairs to the heap and update ascending count.
  * Early termination: if all remaining pairs are ascending, return operations count.

### Complexity

* **Time:** `O(n² log n)` - Each merge can add pairs to heap, worst case all pairs
* **Space:** `O(n)` - For heap, arrays, and tracking structures
