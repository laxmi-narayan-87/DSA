# SALESEASON - Rating 541

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sale Season

It's the sale season again and Chef bought items worth a total of $X$ rupees. The sale season offer is as follows:

- if $X \le 100$, no discount.
- if $100 \lt X \le 1000$, discount is $25$ rupees.
- if $1000 \lt X \le 5000$, discount is $100$ rupees.
- if $X \gt 5000$, discount is $500$ rupees.

Find the final amount Chef needs to pay for his shopping.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line of input containing an integer $X$.
### Output Format

For each test case, output on a new line the final amount Chef needs to pay for his shopping.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 10000$
### Sample 1:
Input
Output

```
4
15
70
250
1000

```

```
15
70
225
975

```

### Explanation:

 **Test case $1$:**  Since $X \le 100$, there is no discount.

 **Test case $3$:**  Here, $X = 250$. Since $100 \lt 250 \le 1000$, discount is of $25$ rupees. Therefore, Chef needs to pay $250-25 = 225$ rupees.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:42:23.677Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x=int(input())
        if x>5000:
            print(x-500)
        elif  5000>=x>1000:
            print(x-100)
        elif 1000>=x>100:
            print(x-25)
        else:
            print(x)
```

---

[View on CodeChef](https://www.codechef.com/problems/SALESEASON)