class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # TC = O(N*M*M)
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]



        '''
        dp = [[] for i in range(1+target)]
        candidates.sort()
        for a in range(1,target+1):

            for c in candidates:

                if a - c > 0 and dp[a-c]:
                    for j in dp[a-c]:
                        # print(j)
                        dp[a].append(  [c] + j       )
                elif a ==c:
                    dp[a].append( [c])
                elif c > a:
                    break
                # print(dp)
            # print(a,dp)
        res = []
        s = set()
        for j in dp[-1]:
            j.sort()
            if tuple(j) not in s:
                res.append(j)
                s.add(tuple(j))
        return res
        '''