# Sherlock and the Valid String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Sherlock considers a string to be *valid* if all characters of the string appear the same number of times.  It is also *valid* if he can remove just $1$ character at $1$ index in the string, and the remaining characters will occur the same number of times.  Given a string $s$, determine if it is *valid*.  If so, return `YES`, otherwise return `NO`.

**Example**  
$s=abc$

This is a valid string because frequencies are $\{a: 1, b: 1, c: 1\}$.  

$s=abcc$  

This is a valid string because we can remove one $c$ and have $1$ of each character in the remaining string.  

$s=abccc$  

This string is not *valid* as we can only remove $1$ occurrence of $c$.  That leaves character frequencies of $\{a: 1, b: 1, c: 2\}$.  

**Function Description**  

Complete the *isValid* function in the editor below.  

isValid has the following parameter(s):  

- *string s*: a string  

**Returns**  

- *string:* either `YES` or `NO`


**Input Format**

A single string $s$.

**Constraints**

- $1 \le |s| \le 10^5$   
- Each character $s[i] \in ascii[a-z]$

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T10:14:18.133Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freqmap = {}
    for x in s:
        freqmap[x] = freqmap.get(x, 0) + 1
    freq_count = {}
    for freq in freqmap.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1
    if len(freq_count) == 1:
        return "YES"
    if len(freq_count) > 2:
        return "NO"
    f1, f2 = sorted(freq_count.keys())
    if f2 == f1 + 1 and freq_count[f2] == 1:
        return "YES"
    if f1 == 1 and freq_count[f1] == 1:
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem)