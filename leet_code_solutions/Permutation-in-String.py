'''

abcd --> bcda  , acdb , cdab ...



'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dp = dict()
        for c in s1:
            if c in dp:
                dp[c] += 1
            else:
                dp[c] = 1
        orig_dp = dp.copy()
        start = -1
        end = -1
        if s2[0] in dp and dp[ s2[0] ] > 0:
            dp[ s2[0] ] -= 1
            start = 0
            end = 0
            if 1 == len(s1):
                return True
        n2 = len(s2)
        # print(dp,start ,end)
        for p in range(1,n2):

            ch = s2[p]
            # print(ch , dp)
            if ch in dp and dp[ch] > 0:
                if start == -1:
                    start = end = p
                else:
                    end += 1
                dp[ch] -= 1
                
                if end - start + 1 == len(s1):
                    return True
            elif ch in dp and dp[ch] == 0:
                # print(start,end , ch)
                while start <= end and dp[ch] == 0:
                    dp[s2[start]] += 1
                    start += 1
                dp[ch] -= 1
                end += 1
                if end - start + 1 == len(s1):
                    return True
            else:
                start = end = -1
                dp = orig_dp.copy()
            # print(p, start , end , dp )
        return False



            
