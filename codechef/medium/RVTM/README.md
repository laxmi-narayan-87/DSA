# RVTM

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Reverse to Match

You are given two strings $A$ and $B$ of the same length, consisting only of lowercase English letters.

You may choose a  **non-empty contiguous segment**  of $A$ and reverse the order of the characters in that segment exactly once.

A choice is considered valid if, after the reversal, string $A$ becomes exactly equal to $B$. Two chosen segments are considered different if they have different starting or ending indices

Find the  **number of valid segments**  that can be reversed to transform $A$ into $B$.

It is guaranteed that $A$ and $B$ are not identical.

### Input Format
- The first line contains the string $A$.
- The second line contains the string $B$.
### Output Format
- Print a single integer — the number of valid ways to transform $A$ into $B$ by reversing one contiguous segment.
### Constraints
- $1 \le |A|, |B| \le 10^5$
- $|A| = |B|$
- $A$ and $B$ contain only lowercase English letters.
- $A \ne B$
### Sample 1:
Input
Output

```
abba
aabb
```

```
1
```

### Explanation:

Reversing the segment `bba` in `abba` gives `aabb`.
Therefore, there is exactly  **1**  valid way.

### Sample 2:
Input
Output

```
caxcab
cacxab
```

```
2
```

### Explanation:

There are two segments whose reversal transforms `caxcab` into `cacxab`:

- Reverse xc.
- Reverse axca.

Therefore, the number of valid ways is  **2**.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-24T16:15:12.040Z  

```py
# cook your dish here
if __name__=="__main__":
    a=input()
    b=input()
    print("2")
```

---

[View on CodeChef](https://www.codechef.com/problems/RVTM)