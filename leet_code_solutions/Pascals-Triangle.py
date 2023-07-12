class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        if numRows == 1:
            return [[1]]
        
        res = [[1] , [1,1]]
        j = 1
        while len(res) < numRows :
            
            temp = []
            for i in range(len(res[j])):
                
                if i == 0:
                    temp.append(  res[j][i] )
                if i == len(res[j]) - 1 :
                    temp.append(  res[j][i] + res[j][i-1] )
                    temp.append(  res[j][i] )
                elif i != 0 :
                    temp.append(  res[j][i] + res[j][i-1] )
            j+=1
            res.append(temp)
        return res
        '''
    
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal