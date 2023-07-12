class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        dp --> coins = [2,4,5] ,, amt = 20
        1 2 3 4 5 6 7 8 9 10
        0 1 0 1 0 1 0 1 0 1 0 ...........20 , using coin 2 only 
        0 1 0 2 0 2 0 3 0 4 0.......        , using coin 2 , 4 both
        
        
        '''
        if amount == 0:
            return 1

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
            # print(dp)
        return dp[amount]
        '''
        
        coins.sort()
        # print(coins)
        @cache
        def dfs(i,amt):
            # print(i,coins[i],amt)
            if amt == 0:
                return 1
            
            if amt < 0 :
                return 0
            
            total = 0
            for j in range( i, len(coins)):
                if coins[j] > amt:
                    break
                total += dfs(j,amt-coins[j])
            return total
        return dfs(0,amount)
        '''