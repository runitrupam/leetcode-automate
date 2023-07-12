class Solution:
    def minFallingPathSum(self, M: List[List[int]]) -> int:
        m = len(M)
        n =len(M[0])
        dp = copy.deepcopy(M)
        # dir = [  (-1,0) , (-1,1) , (-1,-1)  ]
        # print(dp)
        for i in range(1,m):

            for j in range(n):
                mn = float('+inf')
                for p,q in [    (-1 + i,j) , (-1+i,1+j) , (-1+i,-1+j)    ]   :
                    # print(p,q)
                    if  0<=p<m and 0<=q<n:
                        mn = min( mn , dp[p][q]        )
                dp[i][j] = mn + dp[i][j]
        # print(dp)




        return min(dp[-1])