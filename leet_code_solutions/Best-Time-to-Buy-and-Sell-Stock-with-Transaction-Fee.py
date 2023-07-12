class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cin_wo_shares = 0
        cin_w_shares = - prices[0] 
        
        for i in range(1,len(prices)):
            
            cin_w_shares = max(cin_wo_shares - prices[i] , cin_w_shares  )
            
            
            cin_wo_shares = max(cin_w_shares + prices[i] - fee , cin_wo_shares  )
        return cin_wo_shares