class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        
        if len(p) <= 1:
            return 0
        
        max_till_now = p[-1]
        res = 0
        for i in range(len(p) -2 ,-1,-1):
            
            if max_till_now > p[i]:
                res=max(res,  max_till_now - p[i] )
            else:
                max_till_now = p[i]
        return res