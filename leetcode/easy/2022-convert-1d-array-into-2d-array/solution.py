class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr=[]
        if m*n<len(original):
            return arr
        for i in range(0,m):
            a=[]
            for j in range(n):
                a.append(original[i*n+j-1])
            arr.append(a)
        return arr
