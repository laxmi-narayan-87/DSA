# GS11

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Test cases with multiple types of input

Listen

In the previous problem, each testcase had 2 lines of input - each consisting of integers.
Test cases can also contain a combination of integers and strings.

### Task

Lets write a program in the IDE which performs the following

- The 1st line of input contains $t$ - the count of testcases Each testcase consists of the following $2$ lines of input The 1st line of the testcase contains 2 integers - accept them as variables $A$ and $B$ The 2nd line of the testcase contains 1 string - accept it as a variable $C$
- For each test case, output on one line the 2 integers followed by the string
### Sample 1:
Input
Output

```
2
1 2
abcde
34 567
A1B2C3
```

```
1 2 abcde
34 567 A1B2C3
```

### Explanation:

Test case 1:
1 2
abcde

Output for test case 1: 1 2 abcde

Test case 2:
34 567
A1B2C3

Output for test case 2: 34 567 A1B2C3

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:21:08.638Z  

```py
t = int(input())

for i in range(t):
    # accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())
    
    # accept 1 string on the 2nd line of each test case
    C = input()
    
    # output the 2 integers and 1 string on a single line
    print(A,B,C, end=" ")

```

---

[View on CodeChef](https://www.codechef.com/problems/GS11)