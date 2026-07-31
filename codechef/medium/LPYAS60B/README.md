# LPYAS60B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Average Score

Write a program to print the average score of a student who appeared in three subject's exams and got score  **X**,  **Y**  and  **Z**  respectively in those subjects.

 **Note:**  Formula to calculate the average of  **N**  numbers:

Average = (sum of all numbers) /  **N** 

### Input Format

Input contains three space separated numbers on the same line,  **X**,  **Y**  and  **Z**  - the scores of students in three subjects.

### Output Format

Output on a single line the average score of students in these three subjects.

### Sample 1:
Input
Output

```
95 80.5 58.5
```

```
78.0

```

### Explanation:

Average score = (95 + 80.5 + 58.5) / 3 = 78.0

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T04:13:09.985Z  

```py
# cook your dish here
x,y,z=map(float,input().split())
print((x+y+z)/3)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS60B)