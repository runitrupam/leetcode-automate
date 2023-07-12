class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        '''

        y + x -c = 0
        1 + 4 = c

        '''
        if len(points)<=2: return len(points)

        # y = mx + c
        # c = y - mx
        def straight_line(p1 , p2):
            if p2[0] - p1[0] == 0:
                return (p2[0]) # y changes , but x is fixed ,,, x = 5
            m = ( p2[1] - p1[1])  /( p2[0] - p1[0])
            y_intercept = p1[1] - m * p1[0]
            return (m,y_intercept)

        def line(p1,p2):
            # Vertical line
            if p2[0]-p1[0] == 0:
                return (p1[0])
            slope = (p2[1]-p1[1]) / (p2[0]-p1[0])                
            b = p1[1] - slope * p1[0]
            return (slope,b)

        ma_x = 1
        for i in range(len(points)):
            dp = defaultdict(int) # I am initializing it again , So that same points taken , won't be taken again .
            for j in range(i+1,len(points)):
                tup = straight_line(points[i] ,points[j]   )
                dp[tup] += 1
                ma_x = max(ma_x ,dp[tup] )
            # print(dp)
        return ma_x + 1
             