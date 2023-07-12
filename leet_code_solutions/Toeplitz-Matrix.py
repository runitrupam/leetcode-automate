class Solution:
    def isToeplitzMatrix(self, M: List[List[int]]) -> bool:        
        for i in range(1,len(M)):
            for j in range(1,len(M[0])):
                if M[i-1][j-1] != M[i][j]:
                    return False
        return True
        
        '''
        
        m = len(M)
        n = len(M[0])
        
        for i in range(m):
            j = 0
            
            while( j < m - i - 1 and j < n - 1 and j < m - 1):
                
                if M[i + j][j] != M[i + j + 1][j + 1]:
                    return False
                j += 1
        for k in range(1,n):
            j = 0
            while( j < n - k - 1 and j < n - 1 and j < m - 1):
                
                if M[j][k+j] != M[j + 1][k + j + 1]:
                    return False
                j += 1
        return True
        '''
            