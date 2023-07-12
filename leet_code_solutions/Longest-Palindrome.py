class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dp = dict()

        for j in s:
            if j in dp:
                dp[j]+=1
            else:
                dp[j] = 1
        
        total_odd_length_chars = 0
        for j in dp.keys():
            if dp[j] %2 != 0:
                total_odd_length_chars+=1
        
        if total_odd_length_chars > 1:
            return len(s) +1 - total_odd_length_chars
        else:
            return len(s)