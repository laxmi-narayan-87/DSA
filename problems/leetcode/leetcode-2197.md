# LeetCode 2197: Replace Non-Coprime Numbers in Array

[![LeetCode](https://img.shields.io/badge/LeetCode-2197-orange)](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/)

## Problem

Replace adjacent non-coprime numbers in an array with their LCM until no more merges are possible.

**Definition**: Numbers `a` and `b` are non-coprime if `gcd(a,b) > 1`.

## Examples

```
Input:  [6,4,3,2,1]
Output: [12,1]
Steps:  6,4→12 → 12,3→12 → 12,2→12 → 12,1 (stop)

Input:  [2,6,8,9,7] 
Output: [72,7]
Steps:  2,6→6 → 6,8→24 → 24,9→72 → 72,7 (stop)
```

## Solutions

### Stack + Greedy (Optimal)

```python
import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                num = math.lcm(stack.pop(), num)
            stack.append(num)
        
        return stack
```

**Complexity**: O(n log A) time, O(n) space

### Brute Force

```python
import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        while True:
            merged = False
            for i in range(len(nums) - 1):
                if math.gcd(nums[i], nums[i + 1]) > 1:
                    lcm_val = math.lcm(nums[i], nums[i + 1])
                    nums[i:i + 2] = [lcm_val]
                    merged = True
                    break
            if not merged:
                break
        return nums
```

**Complexity Analysis:**
- Time: O(n² log A) where A is the maximum value
- Space: O(1) extra space

### Approach 2: Stack + Greedy (Optimal) ⭐

```python
import math
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            # Merge with stack elements if possible
            while stack and math.gcd(stack[-1], num) > 1:
                num = math.lcm(stack.pop(), num)
            
            stack.append(num)
        
        return stack
```

**Complexity Analysis:**
- Time: O(n log A) where A is the maximum value
- Space: O(n) for the stack

**Key Insights:**
- Uses stack to handle chain reactions efficiently
- Greedy merging is optimal since merge order doesn't affect final result
- Each element is processed at most once

## Algorithm Walkthrough

**Example:** `nums = [6,4,3,2,1]`

```
Step 1: stack = [6], num = 4
        gcd(6,4) = 2 > 1 → merge
        stack = [12]

Step 2: stack = [12], num = 3  
        gcd(12,3) = 3 > 1 → merge
        stack = [12]

Step 3: stack = [12], num = 2
        gcd(12,2) = 2 > 1 → merge  
        stack = [12]

Step 4: stack = [12], num = 1
        gcd(12,1) = 1 → no merge
        stack = [12,1]
```

## Edge Cases

- **Single element**: `[5]` → `[5]`
- **All coprime**: `[3,5,7]` → `[3,5,7]`  
- **All same**: `[4,4,4]` → `[4]`
- **Empty array**: `[]` → `[]`

## Related Topics

- **Array Manipulation**
- **Number Theory (GCD/LCM)**
- **Stack Data Structure**
- **Greedy Algorithms**

## Tags

`#array` `#math` `#stack` `#greedy` `#hard` `#number-theory`
