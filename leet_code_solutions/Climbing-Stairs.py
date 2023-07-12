class Solution:
    def climbStairs(self, n: int) -> int:
        d = dict()
        d[1] = 1
        d[2] = 2
        d[3] = 3
        d[4] = 5
        d[5] = 8
        '''
        4 th stair = 3 + 2
        1 2 1
        2 2
        2 1 1
        1 1 2
        1 1 1 1
        '''
        for i in range(6,n+1):
            d[i] = d[i-1] + d[i-2]
        return d[n]