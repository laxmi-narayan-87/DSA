# 3013. Divide an Array Into Subarrays With Minimum Cost II

## Problem Statement

Find the minimum sum of costs when dividing array `nums` into `k` disjoint contiguous subarrays, where the cost is the first element of each subarray, and starting indices i₁ through i_(k-1) must satisfy i_(k-1) - i₁ ≤ dist.

**Problem Link:** [LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/)

**Related:** [February 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/February%20/Leetcode%20Daily%20Problems/Question/02-February-2026.md)

---

## Solution 1: Sliding Window + Sorting

```python
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        ans = float('inf')
        base = nums[0]
        
        for i in range(1, n - k + 2):
            window = nums[i:min(i + dist + 1, n)]
            if len(window) >= k - 1:
                smallest = sorted(window)[:k-1]
                ans = min(ans, base + sum(smallest))
        
        return ans
```

### Idea

* **Base cost:** The first subarray always starts at index 0, so `nums[0]` is always included.
* **Window constraint:** The starting indices of subarrays 2 through k must be within a window of size `dist`.
* **Sliding window:** For each possible starting position `i` of the second subarray (from 1 to n-k+1):
  - Consider elements in the range `[i, i+dist]` as potential starting positions
  - Select the `k-1` smallest values from this window
  - Calculate total cost: `nums[0]` + sum of k-1 smallest values
* Track and return the minimum cost.

### Complexity

* **Time:** `O(n × dist × log(dist))` - For each position, sort a window of size dist
* **Space:** `O(dist)` - For storing the window

---

## Solution 2: Optimized with Two Heaps

```python
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        base = nums[0]
        
        # Use SortedList to maintain smallest k-1 elements efficiently
        small = SortedList()
        large = SortedList()
        current_sum = 0
        
        # Initialize with first dist+1 elements after nums[0]
        for i in range(1, min(dist + 2, len(nums))):
            small.add(nums[i])
            current_sum += nums[i]
            if len(small) > k - 1:
                val = small.pop()
                current_sum -= val
                large.add(val)
        
        ans = base + current_sum
        
        # Slide the window
        for i in range(dist + 2, len(nums)):
            # Add new element
            if nums[i] < small[-1]:
                small.add(nums[i])
                current_sum += nums[i]
                # Move largest from small to large
                val = small.pop()
                current_sum -= val
                large.add(val)
            else:
                large.add(nums[i])
            
            # Remove element going out of window
            out_idx = i - dist - 1
            if nums[out_idx] in small:
                small.remove(nums[out_idx])
                current_sum -= nums[out_idx]
                # Move smallest from large to small
                if large:
                    val = large.pop(0)
                    small.add(val)
                    current_sum += val
            else:
                large.remove(nums[out_idx])
            
            ans = min(ans, base + current_sum)
        
        return ans
```

### Idea

* **Two sorted containers:** Maintain two sorted lists:
  - `small`: Contains the k-1 smallest elements in the current window
  - `large`: Contains the remaining elements in the window
* **Sliding window:** As we slide the window:
  - Add new element to appropriate container
  - Remove element leaving the window
  - Rebalance to ensure `small` has exactly k-1 smallest elements
* **Efficient updates:** SortedList allows O(log n) insertions, deletions, and access.
* Track the sum of elements in `small` to compute cost quickly.

### Complexity

* **Time:** `O(n × log(dist))` - Each insertion/deletion in SortedList is O(log dist)
* **Space:** `O(dist)` - For the two containers

---

## Solution 3: Simple Heap Approach (Corrected)

```python
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        ans = float('inf')
        base = nums[0]
        
        for start in range(1, n - k + 2):
            window = []
            for i in range(start, min(start + dist + 1, n)):
                heapq.heappush(window, nums[i])
            
            if len(window) >= k - 1:
                cost = base
                temp = []
                for _ in range(k - 1):
                    cost += heapq.heappop(window)
                    temp.append(cost - base)
                ans = min(ans, cost)
        
        return ans
```

### Idea

* For each valid starting position of the second subarray, create a min-heap of eligible elements.
* Extract k-1 smallest elements from the heap.
* Calculate and track the minimum total cost.

### Complexity

* **Time:** `O(n × dist × log(dist))` - Building and extracting from heap
* **Space:** `O(dist)` - For the heap

---

## Comparison

| Approach | Time | Space | Best For |
|----------|------|-------|----------|
| Sliding Window + Sorting | O(n × dist × log(dist)) | O(dist) | Simple implementation |
| Two Heaps/SortedList | O(n × log(dist)) | O(dist) | Optimal performance |
| Simple Heap | O(n × dist × log(dist)) | O(dist) | Understanding the problem |
