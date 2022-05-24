# Brute - additional memory approach

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        column = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    print(i,j)
                    row.append(i)
                    column.append(j)
                    
        print(row, column)
                    
        for o in range(len(row)):
            for k in range(len(matrix)):
                for l in range(len(matrix[k])):
                    if l == column[o]:
                        matrix[k][l] = 0
                    if k == row[o]:
                        matrix[k][l] = 0