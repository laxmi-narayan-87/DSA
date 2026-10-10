# LeetCode 3005: Count Elements With Maximum Frequency

[![LeetCode](https://img.shields.io/badge/LeetCode-3005-purple)](https://leetcode.com/problems/count-elements-with-maximum-frequency/)

---

## Problem

You are given an integer array `nums`.  
The **frequency** of an element is the number of times it appears in the array.  

Return the **total number of elements** that appear with the **highest frequency**.

---

## Examples

### Example 1

**Input:**  
`nums = [1,2,2,3,1,4]`  
**Output:**  
`4`  
**Explanation:** Both 1 and 2 have frequency 2.  
So, total count = 2 + 2 = 4.

---

### Example 2

**Input:**  
`nums = [1,2,3,4,5]`  
**Output:**  
`5`  
**Explanation:** All numbers appear once, so highest frequency = 1.  
Count = 1+1+1+1+1 = 5.

---

## Approach 1: Hash Map Frequency Counting (Optimal ⭐)

- Use a dictionary to count occurrences of each number.  
- Track:
  - `max_freq`: maximum frequency so far.  
  - `result_sum`: total count of elements with `max_freq`.  
- Update while iterating through `nums`.

```python
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq = 0
        result_sum = 0

        for num in nums:
            # Count frequency of each number
            freq[num] = freq.get(num, 0) + 1
            f = freq[num]

            # If new max frequency found → reset sum
            if f > max_freq:
                max_freq = f
                result_sum = f
            # If equal to max frequency → add to sum
            elif f == max_freq:
                result_sum += f

        return result_sum
```

---

## Approach 2: Counter + Math (Concise)

- Use `collections.Counter` to count occurrences.
- Compute `max_freq` as the highest frequency.
- Count how many elements occur with `max_freq`.
- Total elements with max frequency = `max_freq * count`.

```python
from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        count = sum(1 for v in freq.values() if v == max_freq)
        return max_freq * count
```

---

## Complexity Analysis

- **Time Complexity:** O(n) — one pass to count elements.
- **Space Complexity:** O(k) — where k = number of distinct elements.

---

## Walkthrough Example

**Input:** `nums = [1,2,2,3,1,4]`

Steps:

1. Count frequencies → `{1:2, 2:2, 3:1, 4:1}`
2. Max frequency = 2
3. Elements with freq=2: 1 and 2
4. Result = 2+2 = 4

**Output:** `4`

---

## Edge Cases

- Single element array: `[5]` → Output = 1
- All elements unique: `[1,2,3]` → Output = 3
- All same elements: `[7,7,7]` → Output = 3

---

## Related Topics

- Hash Map
- Array Counting
- Frequency Analysis

---

## Tags

#hashmap #array #frequency #easy

---
