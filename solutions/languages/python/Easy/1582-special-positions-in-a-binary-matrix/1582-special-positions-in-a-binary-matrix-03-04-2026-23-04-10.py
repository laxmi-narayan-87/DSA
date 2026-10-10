class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        special = 0
        for i in range(m):
            if sum(mat[i]) == 1:
                j = mat[i].index(1)
                if sum(mat[k][j] for k in range(m)) == 1:
                    special += 1
        return special