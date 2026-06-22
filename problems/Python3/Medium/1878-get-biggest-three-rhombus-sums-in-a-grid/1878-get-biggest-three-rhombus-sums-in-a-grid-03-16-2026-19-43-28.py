class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        all_sums = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                all_sums.append(grid[row][col])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                border = 1
                while (row+border) < len(grid) and (row-border) >= 0 and (col+border) < len(grid[0]) and (col-border) >= 0:
                    rhombus_sum = 0
                    for i in range(1, border):
                        rhombus_sum += grid[row+i][col-border+i]
                        rhombus_sum += grid[row-i][col-border+i]
                        rhombus_sum += grid[row+i][col+border-i]
                        rhombus_sum += grid[row-i][col+border-i]
                    all_sums.append(rhombus_sum + grid[row][col-border]+grid[row][col+border]+grid[row-border][col]+grid[row+border][col])
                    border += 1
        return sorted(list(set(all_sums)), reverse=True)[:3]