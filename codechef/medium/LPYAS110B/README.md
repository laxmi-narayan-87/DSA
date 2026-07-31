# LPYAS110B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Count Vowels

Write a program that uses a while loop to find no. of vowels in given input string of lowercase latin letters.

 **Note:**  Vowels in lowercase latin letters are:  **a**,  **e**,  **i**,  **o**  and  **u**.

### Input Format
- The only line of input contains a string.
### Output Format
- The only line of output contains a single integer - The count of vowels in the input string.
### Sample 1:
Input
Output

```
codechef
```

```
3
```

### Explanation:

codechef has 3 vowels:  **o**,  **e**  and another  **e**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T04:58:33.405Z  

```py
# cook your dish here
s=str(input())
nv=0
i=0
while i<len(s):
    if s[i] in "aeiou":
        nv+=1
    i+=1
print(nv)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS110B)