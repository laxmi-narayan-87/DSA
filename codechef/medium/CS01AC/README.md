# CS01AC

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Logical operators & conditional statements

We reviewed basic conditional operators in the previous module.
In this module - we will cover logical operators in conditional statements.

- "and" and "or" statements help check multiple conditions
- Multiple "and" and "or" statements can be clubbed into a single if / else condition
### Task

You are given 3 integers $N$, $A$ and $B$.
You need to compute and output the following for each test case

- If $N$ is divisible by both $A$ and $B$ - then output 'N is divisible by A and B'
- Else if $N$ is divisible by $A$ and not $B$ - then output 'N is divisible by only A'
- Else if $N$ is divisible by $B$ and not $A$ - then output 'N is divisible by only B'
- Else if $N$ is divisible by neither $A$ nor $B$ - then output 'N is divisible by neither A nor B'

Solve this problem in the IDE.

### Sample 1:
Input
Output

```
4
10 5 2
10 3 2
12 3 5
10 4 3
```

```
N is divisible by A and B
N is divisible by only B
N is divisible by only A
N is divisible by neither A nor B
```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-15T18:17:17.113Z  

```cpp
# Update the '_' in the code below to solve the problem

t = int(input())
for i in range(t):
    N, A, B = map(int, input().split())
    if N%A== 0 and N%B == 0:
        print('N is divisible by A and B')
    elif N%A == 0:
        print('N is divisible by only A')
    elif N%B == 0:
        print('N is divisible by only B')
    # The last statement could have been an 'else' statement
    # elif condition used to show usage of 'and' statement
    elif N%A !=0 and N%B != 0:
        print('N is divisible by neither A nor B')
```

---

[View on CodeChef](https://www.codechef.com/problems/CS01AC)