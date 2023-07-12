class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = [intervals[0]]

        for i in range(1,len(intervals)):

            if intervals[i][0]<=res[-1][-1] and intervals[i][-1]>= res[-1][-1]:
                res[-1][-1] = intervals[i][-1]

            elif intervals[i][0]>res[-1][-1]:
                res.append(intervals[i])
        return res
        
        
        '''intervals.sort(key=lambda x: x[0])

        res = []

        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max( res[-1][1]  ,   i[1]  )
            else:
                res.append( [  i[0] , i[1]    ]   )
        return res'''