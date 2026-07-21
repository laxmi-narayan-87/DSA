# Encryption

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

An English text needs to be encrypted using the following encryption scheme.  
First, the spaces are removed from the text. Let $L$ be the length of this text.  
Then, characters are written into a grid, whose rows and columns have the following constraints:

$$\lfloor\sqrt{L}\rfloor \le row \le column \le \lceil\sqrt{L}\rceil\text{, where }\lfloor x \rfloor \text{ is floor function and }\lceil x \rceil\text{ is ceil function}$$ 
 
**Example**  

$s = \texttt{if man was meant to stay on the ground god would have given us roots}$  

After removing spaces, the string is $54$ characters long.  $\sqrt{54}$ is between $7$ and $8$, so it is written in the form of a grid with 7 rows and 8 columns. 

    ifmanwas  
    meanttos          
    tayonthe  
    groundgo  
    dwouldha  
    vegivenu  
    sroots

+ Ensure that $rows \times columns \ge L$   
+ If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. $rows \times columns$.  

The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded message for the grid above is:  
    
`imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau`  
    
Create a function to encode a message.

**Function Description**  

Complete the *encryption* function in the editor below.  

encryption has the following parameter(s):  

- *string s:* a string to encrypt  

**Returns**  

- *string:* the encrypted string  

**Input Format**

One line of text, the string $s$

**Constraints**

$1 \le \text{ length of }s \le 81$   
$s$ contains characters in the range ascii[a-z] and space, ascii(32).

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T10:55:38.662Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    L = len(s)
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    if rows * cols < L:
        rows += 1
    ans = []
    for c in range(cols):
        word = ""
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                word += s[idx]
        ans.append(word)
    return " ".join(ans)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/encryption/problem)