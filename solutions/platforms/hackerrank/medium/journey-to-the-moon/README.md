# Journey to the Moon

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

The member states of the UN are planning to send people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.

 **Example** 

There are astronauts numbered through. Astronauts grouped by country are and. There are pairs to choose from: and.

 **Function Description** 

Complete the  *journeyToMoon*  function in the editor below.

journeyToMoon has the following parameter(s):

- int n: the number of astronauts
- int astronaut[p][2]: each element is a element array that represents the ID's of two astronauts from the same country

 **Returns** 
-  *int:*  the number of valid pairs

 **Input Format** 

The first line contains two integers and, the number of astronauts and the number of pairs.
Each of the next lines contains space-separated integers denoting astronaut ID's of two who share the same nationality.

 **Constraints** 

-
-

 **Sample Input 0** 

```
5 3
0 1
2 3
0 4

```

 **Sample Output 0** 

```
6

```

 **Explanation 0** 

Persons numbered belong to one country, and those numbered belong to another. The UN has ways of choosing a pair:

 **Sample Input 1** 

```
4 1
0 2

```

 **Sample Output 1** 

```
5

```

 **Explanation 1** 

Persons numbered belong to the same country, but persons and don't share countries with anyone else. The UN has ways of choosing a pair:

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T10:47:19.428Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    graph = [[] for _ in range(n)]
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    component_sizes = []
    def dfs(node):
        stack = [node]
        visited[node] = True
        size = 0
        while stack:
            curr = stack.pop()
            size += 1
            for nei in graph[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        return size
    for i in range(n):
        if not visited[i]:
            component_sizes.append(dfs(i))
    ans = 0
    remaining = n
    for size in component_sizes:
        remaining -= size
        ans += size * remaining
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/journey-to-the-moon/problem)