# LeetCode 2221: Find Triangular Sum of an Array 

[![LeetCode](https://img.shields.io/badge/LeetCode-2221-blue)](https://leetcode.com/problems/find-triangular-sum-of-an-array/)

---

## Problem

Given an integer array `nums` (digits 0–9), the **triangular sum** is obtained by repeatedly:

- Replacing `nums[i]` with `(nums[i] + nums[i+1]) % 10`.
- Continuing until only one element remains.
- Return the last remaining number.

---

## First Principles Breakdown

At the core, this problem reduces to **aggregating contributions of array elements in a structured, sequential way**.

1. **Atomic Operation:** `(nums[i] + nums[i+1]) % 10`  
   - Each step combines two adjacent numbers, taking only the last digit.

2. **Sequential Reduction:**  
   - The array shrinks by 1 element per iteration until length = 1.  

3. **Observation:**  
   - Each original element contributes to multiple sums along the path to the final number.  
   - Contribution of each element follows **binomial coefficients** (`C(n-1, i)`), as each reduction step mirrors a combination process.

---

## Approaches from First Principles

### Approach 1: Simulation (Extra Array)

**Idea:** Directly implement the process as defined.

- Break the problem into the atomic operation of combining two elements.
- Reduce the array step by step.
- Terminate when array has one element.

```python
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:
            new_nums = [(nums[i] + nums[i+1]) % 10 for i in range(n-1)]
            nums = new_nums
            n -= 1
        return nums[0]
```
*Principle: Decompose complex computation into repeated application of a simple rule.*

---

### Approach 2: In-place Simulation

**Idea:** Apply the same principle, but reduce space usage by modifying the array directly.

```python
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            n -= 1
        return nums[0]
```
*Principle: Reuse existing data structures while performing the same atomic operations.*

---

### Approach 3: Mathematical Formula (Binomial Coefficients)

**Idea:** Recognize that the contribution of each element to the final sum follows combinatorial patterns.

- Element at index `i` contributes `nums[i] * C(n-1, i)` to the final sum modulo 10.

```python
from math import comb
from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i, v in enumerate(nums):
            res += v * comb(n-1, i)
        return res % 10
```
*Principle: Decompose problem into atomic contributions and combine mathematically, avoiding iterative simulation.*

---

## Key Insights from First Principles

- **Atomic Thinking:** Break down into smallest operation `(a+b)%10`.
- **Sequential Composition:** Understand how repeated applications propagate contributions.
- **Pattern Recognition:** Identify combinatorial structure in the process.
- **Optimization:** Replace repeated simulation with direct computation using binomial coefficients.

---

## Tags

#array #math #first-principles #binomial-theorem #simulation #easy
