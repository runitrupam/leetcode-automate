class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest_palindrome =s[0]
        # odd window
        for i in range(len(s)):
            if i != 0 and i != len(s)-1 :
                
                j = 1
                while(i-j >=0 and i+j <= len(s)-1 and s[i-j ] == s[i+j]):
                    
                    j+=1
                if j>1:
                    if 2 * j + 1 > len(longest_palindrome):
                        longest_palindrome = s[i-j+1:i+j]
        # even  window              
        for i in range(len(s)):
            if i!=len(s)-1 :
                
                j = 0
                while(i-j >=0 and i+j+1 <= len(s)-1 and s[i-j ] == s[i+j+1]):
                    
                    j+=1
                if j>=1:
                    if 2 * j > len(longest_palindrome):
                        longest_palindrome = s[i-j+1:i+j+1]                
        return longest_palindrome                
                        
            