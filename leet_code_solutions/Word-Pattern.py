class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:


        
        s_list = s.split(' ')
        if len(s_list) != len(pattern) or len(set(pattern)) != len(set(s_list)):
            return False
        dp = dict()
        for i in range(len(pattern)):
            w = s_list[i]
            if pattern[i] not in dp:
                dp[pattern[i]] = w
            elif dp[pattern[i]] != w:
                return False
            # print(dp)
        return True
        

