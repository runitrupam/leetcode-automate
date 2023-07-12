'''
The three dimensions of the solution to this problem are: the currently available crime, the number of selected members, and the lower limit of the current profit

According to the above analysis, we can define a three-dimensional array dp as the state of dynamic programming, where dp[i][j][k] means that j employees are selected in the first i crime, and The total number of profitable plans where the working profit is at least k. Assuming that the length of the group array is len, then without considering the modulo operation, the final answer is:

∑i=0ndp[len][i][minProfit]\sum_{i=0}^n dp[len][i][minProfit]∑ 
i=0
n
​
 dp[len][i][minProfit]

So we can create a new three-dimensional array dp[len+1][n+1][minProfit+1] and initialize dp[0][0][0]=1. Next, we analyze the state transition equation. For each crime i, we have two cases of being able to work and unable to work according to the upper limit of the current number of workers j:

If the current crime i cannot be done, then obviously:
dp[i][j][k]=dp[i−1][j][k]dp[i][j][k] = dp[i−1][j][k]dp[i][j][k]=dp[i−1][j][k]

If the current crime i can be done, assume the current group number is group[i], and the work profit is profit[i], then without considering the modulo operation, there are:
dp[i][j][k]=dp[i−1][j][k]+dp[i−1][j−group[i]][max(0,k−profit[i])]dp[i][j][k] = dp[i−1][j][k]+dp[i−1][j−group[i]][max(0,k−profit[i])]dp[i][j][k]=dp[i−1][j][k]+dp[i−1][j−group[i]][max(0,k−profit[i])]

Since the third dimension we defined is that the working profit is at least k rather than the working profit is exactly k, the third dimension on the right side of the above state transition equation is max(0,k−profit[i]) and not k−profit[i]

Complexity
Time complexity:
O(len×n×minProfit)O(len×n×minProfit)O(len×n×minProfit), where len is the length of the array group.
The total number of states that need to be calculated by dynamic programming is O(len×n×minProfit)O(len×n×minProfit)O(len×n×minProfit), and the time of each state needs O(1)O(1)O(1) time to calculate.

Space complexity:
O(n×minProfit)O(n×minProfit)O(n×minProfit)
To implement space optimization, we need to create a two-dimensional array dp with n+1 rows and minProfit+1 columns.




'''



class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        
        length = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD
        
        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD