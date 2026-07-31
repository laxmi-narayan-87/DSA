# GS10

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### What are test cases

Listen

In the previous problem - we wrote the program to accept 5 inputs on 5 separate lines.

- What will we do if we expect 100 inputs or test cases?
- What about 100,000 inputs or test cases?

For taking a lot of test cases as input, we use loops.
In the last problem, we told you that the number of test cases was 5.
Usually the number of test cases is the first input you take and then take that input for each test case.

Consider this test case

```
2
4
5

```

Here 2 is the number of test cases. 4 and 5 are the the input for 1st and 2nd test case respectively. A code for taking and printing this test cases will be:

```
t = int(input())
for i in range(t):
    n = int(input())
    print(n)

# Output
4
5

```

- We took the input for 't', the number of test cases in the first line.
- Then we ran a loop which will go from 0 to '(t-1)', using the range function.
- For each test case, we input the value in 'n' and printed it.
### Task

Write a program in the IDE which does the following

- Accepts the count of test cases - $t$ - as an integer input given in the 1st line. This is followed by $t$ lines - Each line contains an integer $N$
- For each test cases, prints out the integer $N$ to console on a separate line
### Sample 1:
Input
Output

```
3
1
22
33
```

```
1
22
33
```

### Explanation:

Since the count of test cases is 3 -> we accept 3 inputs and print 3 outputs

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T11:18:09.673Z  

```py
# accept the count of test cases given in the the 1st line
t = int(input())

# run a loop to accept 't' inputs
for i in range(t):     
    N = int(input())      
    print(N)

```

---

[View on CodeChef](https://www.codechef.com/problems/GS10)