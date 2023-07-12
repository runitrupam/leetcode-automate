class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        
        '''
        dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as

if M[i,j] == 1 then
dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.
        
        '''
        
        r = len(M)
        c = len(M[0])
        max_sq_len = 0
        dp = [[0 for j in range(c+1)] for i in range(r+1)]
        
        for i in range(1,r+1):
            
            for j in range(1,c+1):
                
                if M[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1    
                
                max_sq_len = max(max_sq_len ,  dp[i][j]  )
        
        print(dp)
        return max_sq_len * max_sq_len
        
        '''
        TLE 
        max_sq_len = 0
        
        for i in range(r):
            
            for j in range(c):
                
                if M[i][j] == '1':
                    sq_len = 1
                    flag = True
                    
                    while(  sq_len + i < r and sq_len + j < c and flag ):
                        for k in range( j , sq_len + j + 1 ):
                            
                            if M[i+sq_len][k] == '0':
                                flag = 0
                                break
                           
                        for k in range( i , sq_len + i + 1 ):
                            
                            if M[k][j+sq_len] == '0':
                                flag = 0
                                break
                        if flag :
                            sq_len += 1
                    max_sq_len = max(max_sq_len ,sq_len )
            
        return max_sq_len * max_sq_len
        '''