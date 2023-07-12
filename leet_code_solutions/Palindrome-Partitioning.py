class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]
 
        dp = defaultdict(list)
        '''
        abaabba

        a
        a b , ab (not palindrome)

        '''
        dp[0] = [[s[0]]]
        for i in range(1,len(s)):
            curr = []
            for j in range(  0 , i,1  ):
                if not isPalindrome(s[j+1:i+1]):
                    continue
                tp = copy.deepcopy(dp[j])
                # print(tp , j )
                for k in tp:
                    curr.append( k + [  s[j+1:i+1]    ])
            if isPalindrome(s[0:i+1]):
                curr.append([s[:i+1]])
            # print(curr)
            dp[i] = curr
        return dp[len(s)-1]
 