class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def check_isom(s,t):
            dp = dict()
            for i in range(len(s)):

                if s[i] in dp and dp[ s[i] ] != t[i] :
                    return False
                elif s[i] not in dp:
                    dp[s[i]] = t[i]
                else:#s[i] in dp and dp[ s[i] ] == t[i] :
                    pass        
            return True
        if check_isom(s,t) and check_isom(t,s):
            return True
        else:
            return False
        