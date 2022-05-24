class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix = []
        for i in range(numRows):
            if i == 0:
                matrix.append([1])
            elif i == 1:
                matrix.append([1,1])
            else:
                temp = []
                for j in range(i+1):
                    if j == 0:
                        temp.append(1)
                    elif j == i:
                        temp.append(1)
                    else:
                        print("i",i)
                        print(j)
                        num = matrix[i-1][j-1] + matrix[i-1][j]
                        temp.append(num)
                matrix.append(temp)
        return matrix
                