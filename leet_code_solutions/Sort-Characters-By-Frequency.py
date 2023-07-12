class Solution:
    def frequencySort(self, s: str) -> str:
        dp = dict()
        for ch in s:
            if ch in dp:
                dp[ch] += 1
            else:
                dp[ch] = 1
            
        L = []
        for j in dp:
            L.append(  [ j , dp[j] ]   )
        
        L.sort(key = lambda x : x[1],reverse = True)
        # print(L)
        
        res = ''
        for d in L:
            res = res + d[0] * d[1]
        # print(res)
        return res
            
        