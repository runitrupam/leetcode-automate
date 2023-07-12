
'''
#
stat = 0 ,,, you are buying the stock now ,
     u can sell later OR ,
         u skip this one and go to buy next one .
stat = 1 you have bought previously , u can sell now , or go to the next day stock to sell . 
    Also if u sell , u can only buy the 2 days after stock . 
'''

class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def helper(index,stat):
            if index>=len(prices):
                return 0
            else:
                if stat==0:
                    return max(-prices[index]+helper(index+1,1),helper(index+1,0))
                elif stat==1:
                    return max(prices[index]+helper(index+2,0),helper(index+1,1))
        return helper(0,0)