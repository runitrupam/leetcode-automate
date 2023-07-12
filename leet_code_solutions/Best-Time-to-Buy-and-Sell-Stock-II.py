class Solution:
    def maxProfit(self, P: List[int]) -> int:
        
        
        curr_min = P[0]
        profit = 0
        i = 0
        for i in range(1,len(P)):
            
            if P[i] < P[i-1]:
                profit += P[i-1] - curr_min
                curr_min = P[i]
        profit += P[i] - curr_min
        return profit