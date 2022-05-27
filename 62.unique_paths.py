class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        
        if m == 1 and n==1:
            return 1
        
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            matrix.append(row)
        
        
        for i in range(m-1, -1, -1):  # -1 to include 0th position
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    matrix[i][j] = 0
                elif j == n-1:
                    matrix[i][j] = 1
                elif i == m-1:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i][j+1] + matrix[i+1][j]
        return matrix[0][0]
                    