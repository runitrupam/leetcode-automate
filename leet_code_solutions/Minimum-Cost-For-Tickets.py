'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = dict()
        def rec(curr_dt , index ):
            # print( curr_dt , index   )
            if (curr_dt , index ) in dp:
                return dp[ (curr_dt , index ) ]
            if index >= len(days):
                dp[ (curr_dt , index ) ] = 0
                return 0
            if curr_dt < days[index]:
                pass1 = rec( 0 + days[index]   , index + 1 ) + costs[0]
                pass7 = rec( 6 + days[index]  , index+1 ) + costs[1] 
                pass30 = rec( 29 + days[index]  , index+1 ) + costs[2]
                dp[ (curr_dt , index ) ] = min( pass1 , pass7 , pass30   )
                return dp[ (curr_dt , index ) ]
            if curr_dt >= days[index]:
                dp[ (curr_dt , index ) ] = rec(curr_dt , index + 1)
                return dp[ (curr_dt , index ) ]
        
        rec(0,0)
        # print(dp)
        return dp[(0,0)]
'''
'''
1. i in days list:
we have three option:
a) 1-pass: dp[i] = dp[i-1] + costs[0]
b) 7-pass: dp[i] = dp[i-7] + costs[1]
c) 30-pass: dp[i] = dp[i-30] + costs[2]
in order to avoid negative index:
a) 1-pass: dp[i] =dp[max(0,i-1)] + costs[0]
b) 7-pass: dp[i] = dp[max(0,i-7)] + costs[1]
c) 30-pass: dp[i] = dp[max(0,i-30)] + costs[2]
2. i not in days:
dp[i] = dp[i-1]
which simply means we don't have to spend money, and total costs remains same
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp=[0 for i in range(days[-1]+1)]
        dy = set(days)
        for i in range(days[-1]+1):
            if i not in dy: dp[i]=dp[i-1]
            else: dp[i]=min(dp[max(0,i-7)]+costs[1],dp[max(0,i-1)]+costs[0],dp[max(0,i-30)]+costs[2])
        return dp[-1]