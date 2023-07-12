class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        res = 0
        curr_max = 0
        
        for v in values:
            
            res = max(res, curr_max + v  )
            
            curr_max = max(curr_max , v) - 1
        
        return res
            