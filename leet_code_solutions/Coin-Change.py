class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}
        # faster than 61%
        def bfs(amount, item):
            if item==0 and amount>=0: return float('inf')-1
            if item>0  and amount==0: return 0
            if item==1 and amount>0: return amount//coins[item-1] if amount%coins[item-1]==0 else float('inf')-1
            if dp.get((item, amount),None) is not None: return dp[(item, amount)]                
            if coins[item-1] <= amount:
                dp[(item, amount)] =  min(bfs(amount, item-1),  1 + bfs(amount-coins[item-1], item))
            else:
                dp[(item, amount)] =  bfs(amount, item-1)
            return dp[(item, amount)] 
            
        res = bfs(amount, len(coins))
        return -1 if res == float('inf') else res 
        '''
        # TC (O(N*amount))
        dp = [float('inf')-1] * (amount+1)
        dp[0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[j] = min(dp[j], 1 + dp[j-coins[i-1]])
        return dp[-1] if dp[-1] != float('inf')-1 else -1
        '''
        
        
        '''
        # only 5 % faster as O(N * amount)
        coins.sort(reverse=False)
        if amount == 0 :
            return 0
        if amount < coins[0] :
            return -1

        @cache
        def dfs(amt):
            
            tmp = float('+inf')
            for c in coins:
                if amt - c == 0:
                    return 1
                elif amt - c > 0:
                    if dfs(amt - c) > -1:
                        tmp = min(tmp, dfs(amt - c) + 1)
                elif amt - c < 0:
                    break
            if tmp >= float('+inf'):
                return -1
            return tmp'''
            
            
            
            
            
            
        # if dfs(amount) >= float('+inf'):
        #     return -1
            
        return dfs(amount)