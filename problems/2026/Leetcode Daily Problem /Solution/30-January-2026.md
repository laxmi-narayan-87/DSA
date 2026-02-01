# 2977. Minimum Cost to Convert String II

## Problem Statement

Find the minimum cost to convert string `source` to `target` where you can change substrings using given transformations with specified costs, ensuring operations use disjoint or identical indices.

**Problem Link:** [LeetCode 2977 - Minimum Cost to Convert String II](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/)

**Related:** [January 2026 Daily Problem](https://github.com/laxmi-narayan-87/DSA/blob/main/problems/2026/Leetcode%20Daily%20Problem%20/Question/30-January-2026.md)

---

## Solution

```python
class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        INF = 10**30
        id = {}
        lens = set()
        sz = 0

        dist = [[INF]*201 for _ in range(201)]

        for s, t, c in zip(original, changed, cost):
            if s not in id:
                id[s] = sz
                lens.add(len(s))
                sz += 1
            if t not in id:
                id[t] = sz
                sz += 1
            dist[id[s]][id[t]] = min(dist[id[s]][id[t]], c)

        for i in range(sz):
            dist[i][i] = 0

        for k in range(sz):
            for i in range(sz):
                if dist[i][k] < INF:
                    for j in range(sz):
                        if dist[k][j] < INF:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        n = len(source)
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue

            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for L in lens:
                if i + L > n:
                    continue
                s = source[i:i+L]
                t = target[i:i+L]
                if s in id and t in id:
                    dp[i + L] = min(dp[i + L], dp[i] + dist[id[s]][id[t]])

        return -1 if dp[n] == INF else dp[n]
```

### Idea

* **Step 1 - Graph Construction:** Map each unique substring to an ID and build a graph of substring transformations.
* **Step 2 - Floyd-Warshall:** Compute minimum cost to transform any substring to any other substring using all intermediate transformations.
  - `dist[i][j]` = minimum cost to convert substring with ID `i` to substring with ID `j`
* **Step 3 - Dynamic Programming:** Use DP to find minimum cost to convert `source` to `target`.
  - `dp[i]` = minimum cost to convert `source[0:i]` to `target[0:i]`
  - For each position `i`, try:
    - If characters match, move to next position with no cost
    - For each possible substring length `L` that has transformations:
      - If `source[i:i+L]` can be transformed to `target[i:i+L]`, update `dp[i+L]`
* **Key insight:** By processing left-to-right and considering all possible substring transformations at each position, we ensure operations are on disjoint or identical indices.

### Complexity

* **Time:** `O(S³ + n × L × max_len)` - where `S` is number of unique substrings, `n` is string length, `L` is number of distinct lengths
* **Space:** `O(S² + n)` - For distance matrix and DP array
