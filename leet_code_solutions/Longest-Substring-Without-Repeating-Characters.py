class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''Time complexity :O(n).
        n is the length of the input string.
        It will iterate n times to get the result.

        Space complexity: O(m)
        m is the number of unique characters of the input.
        We need a dictionary to store unique characters.

            There are two cases if s[r] in seen:
            case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
            case2: s[r] is not inside the current window, we can keep increase the window

        
        '''
        #beats only 40%
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            """
            If s[r] not in seen, we can keep increasing the window size by moving right pointer
            """
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


'''
        Beats 70%
        # Time complexity:
        # O(N) --> Worst case also same . As i pointer is inc by 1 each time .

        # Space complexity:s
        # O(N) --> dict used
        i = 0
        j = 0
        dp = defaultdict(int)
        ma_x = 0
        k = 0
        while(i<=j and j < len(s)):

            dp[s[j]] += 1

            if dp[s[j]] == 2:

                while(s[i] != s[j] ):
                    dp[s[i]] -= 1
                    i+=1
                    k-=1 # decreas the length if not same character , But if char matches , u del 1 and add 1 char.
                dp[s[i]] -= 1
                i+= 1                
            else:
                k+=1
                ma_x = max(ma_x,k)
            j+=1
            # print(dp,i,j,k)
        return ma_x

'''
'''
Beats 5% only .
d = [0 for x in range(256)]
k = 0
ma_x = 0 
for j in range(len(s)):
    d = [0 for x in range(256)]
    k = 0
    for i in s[j:]:
        #print(i,ord(i))
        d[ord(i)] +=1
        if(d[ord(i)] != 2):
            k+=1
            ma_x = max(ma_x,k) 
        else:
            break
return ma_x    
'''    
        