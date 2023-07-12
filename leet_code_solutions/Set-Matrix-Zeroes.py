class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #print(matrix)
        y_axis = set()
        for i in range(len(matrix)):
            flag = 0
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    y_axis.add(j)
                    flag = 1
          
                    
            if flag == 1:
                matrix[i] = [0 for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0 and j in y_axis:
                    matrix[i][j] = 0
                    
        #print(matrix)
        #print(y_axis)
                    
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        