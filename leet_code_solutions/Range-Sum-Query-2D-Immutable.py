class NumMatrix:

    def __init__(self, M: List[List[int]]):
        r = len(M)
        c = len(M[0])
        
        self.integral_image = [ [ 0 for x in range(c) ] for y in range(r) ]
        # print(integral_image)
        
        for i in range(r):
            summ = 0
            
            for j in range(c):
                
                summ += M[i][j]
                self.integral_image[i][j] = summ
                if i > 0:
                    self.integral_image[i][j] += self.integral_image[i-1][j]
        # print(self.integral_image)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        integral_image = self.integral_image
        # for i in integral_image:
        #     print(i)
        # print(row1 , row2 , col1 ,col2  )
        op = integral_image[row2][col2]
        if row1 > 0 :
            op -= integral_image[row1 - 1][col2]
        if col1 > 0 :
            op -= integral_image[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            op += integral_image[row1 - 1][col1 - 1]
        return op

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)