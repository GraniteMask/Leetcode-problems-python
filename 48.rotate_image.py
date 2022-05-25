class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for row in matrix:
            L = len(row)
            for i in range(int(L / 2)):
                temp = row[i]
                row[i] = row[L - i - 1]
                row[L - i - 1] = temp
            
            # or use 
            # row.reverse()