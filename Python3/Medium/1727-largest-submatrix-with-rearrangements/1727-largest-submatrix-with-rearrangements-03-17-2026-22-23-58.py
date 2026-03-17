class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    prefix[j] += 1
                else:
                    prefix[j] = 0
            temp = sorted(prefix, reverse=True)
            for k in range(n):
                if temp[k] == 0:
                    break
                ans = max(ans, temp[k] * (k + 1))
        return ans