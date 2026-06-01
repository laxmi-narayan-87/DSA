class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascaltriangle=[]
        for i in range(numRows):
            row=[1]*(1+i)
            for j in range(1,i):
                row[j]= pascaltriangle[i-1][j-1]+pascaltriangle[i-1][j]
            pascaltriangle.append(row)
        return pascaltriangle