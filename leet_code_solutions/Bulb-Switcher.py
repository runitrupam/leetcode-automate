class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))

'''
# TLE
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [1 if x%2 !=0 else 0 for x in range(0,n+1)]
        on_count = 1
        for i in range(3,n+1):
            dp[i] += 1
            if dp[i] %2 != 0:
                on_count += 1
            k = i + i
            while( k < n+1):
                dp[k]+=1
                k+=i
        # print(dp)
        return on_count
'''
'''
1   Y
2 X 
3 x
4   y
5 x
6 x
7 x
8 x
9   y
'''