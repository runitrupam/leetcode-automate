class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # n C r
        r = rowIndex
        ans = [1]*(r+1)
        up = r
        down = 1
        for i in range(1, r):
            ans[i] = ans[i-1]*up//down;
            up = up - 1
            down = down + 1
        return ans;
        
        
        '''
        numRows = 1 + rowIndex 
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[ rowIndex]
        '''