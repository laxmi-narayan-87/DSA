# Bigger is Greater

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<!-- 
**Please note that this is a team event, and your submission will be accepted only as a part of a team, even single member teams are allowed. Please click [here](https://www.hackerrank.com/auth/create_team/csindia) to register as a team, if you have NOT already registered.**
-->

_[Lexicographical order](https://en.wikipedia.org/wiki/Lexicographical_order)_ is often known as alphabetical order when dealing with strings.  A string is _greater_ than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters.  This new word must meet two criteria:

- It must be greater than the original word
- It must be the smallest word that meets the first condition

**Example**   
$w = \texttt{abcd}$

The next largest word is $\texttt{abdc}$.  

Complete the function *biggerIsGreater* below to create and return the new string meeting the criteria.  If it is not possible, return `no answer`.

**Function Description**  

Complete the *biggerIsGreater* function in the editor below.  

biggerIsGreater has the following parameter(s):  

- *string w*: a word

**Returns**   
- *string:* the smallest lexicographically higher string possible or `no answer`  

**Input Format**

The first line of input contains $T$, the number of test cases.   
Each of the next $T$ lines contains $w$.





**Constraints**

* $1 \le T \le 10^5$  
* $1 \le length of w \le 100$  
* $w$ will contain only letters in the range ascii[a..z].

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-23T04:24:20.198Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = list(w)
    n = len(w)
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = n - 1
    while w[j] <= w[i]:
        j -= 1
    w[i], w[j] = w[j], w[i]
    w[i + 1:] = reversed(w[i + 1:])
    return "".join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/bigger-is-greater/problem)