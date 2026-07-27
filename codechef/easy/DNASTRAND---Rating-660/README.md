# DNASTRAND - Rating 660

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Complementary Strand in a DNA

You are given the sequence of Nucleotides of one strand of DNA through a string $S$ of length $N$. $S$ contains the character $A, T, C,$ and $G$ only.

Chef knows that:

- $A$ is complementary to $T$.
- $T$ is complementary to $A$.
- $C$ is complementary to $G$.
- $G$ is complementary to $C$.

Using the string $S$, determine the sequence of the complementary strand of the DNA.

### Input Format
- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ - denoting the length of string $S$.
- Second line contains $N$ characters denoting the string $S$.
### Output Format

For each test case, output the string containing $N$ characters - sequence of nucleotides of the complementary strand.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $S$ contains A, T, C, and G only
### Sample 1:
Input
Output

```
4
4
ATCG
4
GTCC
5
AAAAA
3
TAC

```

```
TAGC
CAGG
TTTTT
ATG

```

### Explanation:

 **Test case $1$:**  Based on the rules, the complements of `A`, `T`, `C`, and `G` are `T`, `A`, `G`, and `C` respectively. Thus, the complementary string of the given string `ATCG` is `TAGC`.

 **Test case $2$:**  Based on the rules, the complements of `G`, `T`, and `C` are `C`, `A`, and `G` respectively. Thus, the complementary string of the given string `GTCC` is `CAGG`.

 **Test case $3$:**  Based on the rules, the complement of `A` is `T`. Thus, the complementary string of the given string `AAAAA` is `TTTTT`.

 **Test case $4$:**  Based on the rules, the complements of `T`, `A`, and `C` are `A`, `T`, and `G` respectively. Thus, the complementary string of the given string `TAC` is `ATG`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T00:06:57.259Z  

```py
# cook your dish here
table=str.maketrans({"A":"T","T":"A","C":"G","G":"C"})
if __name__=="__main__":
    t=int(input())
    # for _ in range(t):
    #     n=int(input())
    #     s=list(input())
    #     for i in range(n):
    #         ch=s[i]
    #         match ch:
    #             case "A":
    #                 s[i]="T"
    #             case "T":
    #                 s[i]="A"
    #             case "C":
    #                 s[i]="G"
    #             case "G":
    #                 s[i]="C"
    #     print("".join(s))
    
    for _ in range(t):
        n=int(input())
        s=str(input())
        print(s.translate(table))
```

---

[View on CodeChef](https://www.codechef.com/problems/DNASTRAND)