# LeetCode 976: Largest Perimeter Triangle 

[![LeetCode](https://img.shields.io/badge/LeetCode-976-orange)](https://leetcode.com/problems/largest-perimeter-triangle/)

---

## Problem

Given an array of positive integers `nums` representing side lengths, find the **largest perimeter** of a triangle that can be formed with any three of these lengths.  
Return `0` if no triangle can be formed.

**Triangle Condition:** For sides `a ≤ b ≤ c`, a triangle exists if `a + b > c`.

---

## Examples

**Input:** `nums = [2,1,2]`  
**Output:** `5`

**Input:** `nums = [1,2,1]`  
**Output:** `0`

**Input:** `nums = [3,2,3,4]`  
**Output:** `10`

---

## First Principles Breakdown

**Goal:** Maximize perimeter while satisfying triangle inequality.

### Step 1: Understand the Triangle Rule
- For three sides `a, b, c`, a triangle exists if sum of any two sides > third.
- To maximize perimeter, we want the largest sides possible that satisfy the condition.

### Step 2: Generate All Possibilities (Brute Force)
- Check all triplets `(i, j, k)` to see if they form a triangle.
- Keep track of the maximum perimeter.

### Step 3: Optimize Using Sorting
- **Observation:** Largest sides will produce largest perimeter.
- Sort sides in descending order.
- Check consecutive triplets. The first valid triangle is guaranteed to be the largest.

### Step 4: Apply Greedy / Two Pointers
- Start from the largest side, use either:
  - Two pointers approach on sorted array
  - Consecutive check after sorting descendingly

**Principle:** Break problem into atomic operations—check, compare, update maximum.

---

## Approaches & Limitations

### Approach 1: Brute Force (3 Loops)

```python
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        n = len(nums)
        max_perimeter = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b > c and a + c > b and b + c > a:
                        max_perimeter = max(max_perimeter, a + b + c)
        return max_perimeter
```
**Time Complexity:** O(n³)  
**Space Complexity:** O(1)

**Limitations:**  
- **Slow for large arrays:** Impractical for large `n` due to O(n³) time.  
- **Redundant checks:** Checks many invalid or duplicate triplets.  
- **Solves:**  
    - **Handles all triplets:** This approach finds the largest perimeter even for unsorted or edge-case inputs.  
    - **Handles any range of integers:** Will find correct answer even with zeros or negatives (though not required by problem).

---

### Approach 2: Sort + Two Pointers

```python
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i-1] + nums[i-2] > nums[i]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0
```
**Time Complexity:** O(n log n) (sorting)  
**Space Complexity:** O(1)

**Limitations:**  
- **Fails for negative/zero values:** Only works correctly for positive integers, as per problem constraints.
- **Only finds one triangle:** Does not enumerate all possible triangles.
- **May not always handle all duplicate max perimeters:** If multiple triplets have the same max perimeter, returns only one.
- **Solves:**  
    - **Solves inefficiency of brute force:** Much faster for large arrays.
    - **Avoids redundant checks:** By sorting, only relevant triplets are checked.


---

### Approach 3: Sort + Greedy (Optimal)

```python
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
```
**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

---

## Key Insights

- **Decompose:** Check individual triplets for triangle inequality.
- **Normalize / Sort:** Sorting simplifies comparisons.
- **Compare numerically:** Sum of two sides must exceed the third.
- **Greedy maximization:** Largest sides first → largest perimeter.
- **Early exit:** Once valid triplet found, no need to check smaller sides.

---

## Tags

#array #greedy #sorting #math #first-principle

---
