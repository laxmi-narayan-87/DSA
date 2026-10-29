# Course Schedule

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you  **must**  take course `bi` first if you want to take course `ai`.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return `true` if you can finish all courses. Otherwise, return `false`.

 

 **Example 1:** 

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

```

 **Example 2:** 

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

```

 

 **Constraints:** 

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 87.08%)  
**Memory:** 21.3 MB (beats 24.70%)  
**Submitted:** 2026-10-29T07:18:19.319Z  

```py

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)

        visited = set()
        path = set()

        def dfs(u):
            if u in path:
                return False

            if u in visited:
                return True

            path.add(u)

            for neigh in graph[u]:
                if not dfs(neigh):
                    return False

            path.remove(u)
            visited.add(u)
            return True

        for u in range(numCourses):
            if not dfs(u):
                return False

        return True

```

---

[View on LeetCode](https://leetcode.com/problems/course-schedule/)