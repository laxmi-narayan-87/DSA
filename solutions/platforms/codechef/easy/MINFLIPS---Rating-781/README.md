# MINFLIPS - Rating 781

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Minimum number of Flips

Chef has an array $A$ of length $N$ consisting of $1$ and $-1$ only.

In one operation, Chef can choose any index $i$ $(1\le i \le N)$ and multiply the element $A_i$ by $-1$.

Find the  **minimum**  number of operations required to make the sum of the array equal to $0$. Output `-1` if the sum of the array cannot be made $0$.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case consists of a single integer $N$ denoting the length of the array.
- Second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.
### Output Format

For each test case, output the minimum number of operations to make the sum of the array equal to $0$. Output `-1` if it is not possible to make the sum equal to $0$.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $A_i = 1$ or $A_i = -1$
### Sample 1:
Input
Output

```
4
4
1 1 1 1
5
1 -1 1 -1 1
6
1 -1 -1 1 1 1
2
1 -1

```

```
2
-1
1
0

```

### Explanation:

 **Test case $1$:**  The minimum number of operations required is $2$. In the first operation, change $A_3$ from $1$ to $-1$. Similarly, in the second operation, change $A_4$ from $1$ to $-1$. Thus, the sum of the final array is $1+1-1-1=0$.

 **Test case $2$:**  It can be proven that the sum of the array cannot be made equal to zero by making any number of operations.

 **Test case $3$:**  We can change $A_1$ from $1$ to $-1$ in one operation. Thus, the sum of the array becomes $-1-1-1+1+1+1=0$.

 **Test case $4$:**  The sum of the array is already zero. Thus we do not need to make any operations.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T13:29:35.746Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if n % 2:
            print(-1)
            continue

        ones = sum(x == 1 for x in a)

        print(abs(ones - (n - ones)) // 2)
```

---

[View on CodeChef](https://www.codechef.com/problems/MINFLIPS)