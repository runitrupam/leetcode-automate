class Solution:
    def maxProfit(self, P: List[int]) -> int:
        
        left_min = P[0]
        left = [0] * len(P)
        
        
        right = [0] * len(P)
        right_max = P[len(P)-1] 
        
        for i in range(1,len(P)):
            left_min = min(left_min , P[i] )
            left[i] = max( left[i-1] , P[i] - left_min  )
        #print(left)    
        
        for j in range(len(P)-2,-1,-1):
            right_max = max(right_max , P[j] )
            right[j] = max ( right[j+1] , right_max - P[j] )
        #print(right)  
        
        ret = 0
        for i in range(len(P)):
            ret = max(ret , left[i] + right[i])
        return ret    