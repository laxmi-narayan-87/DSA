# Partition Labels

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return  *a list of integers representing the size of these parts*.

 

Original
Python3
 **Example 1:** 

```
Input:s = "ababcbacadefegdehijhklij"Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

```

 **Example 2:** 

```
Input:s = "eccbbbbdec"Output: [10]

```

 

 **Constraints:** 

- 1 <= s.length <= 500
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 91.02%)  
**Memory:** 18.9 MB (beats 99.45%)  
**Submitted:** 2026-11-14T09:12:57.398Z  

```py
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={ch:i for i,ch in enumerate(s)}
        result=[]
        start=end=0
        for i,ch in enumerate(s):
            end=max(end,last[ch])

            if i==end:
                result.append(end-start+1)
                start=i+1
        return result
```

---

[View on LeetCode](https://leetcode.com/problems/partition-labels/)