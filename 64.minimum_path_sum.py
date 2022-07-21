# Optimized 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        cols= len(grid[0])
        rows = len(grid)
        
        t = [[float("inf")]*(cols+1) for i in range(rows+1)]
        t[rows][cols-1] = 0
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                t[i][j] = grid[i][j] + min(t[i+1][j], t[i][j+1])
            
        return t[0][0]