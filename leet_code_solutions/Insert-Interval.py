class Solution:
    def insert(self, I: List[List[int]], newI: List[int]) -> List[List[int]]:
        import bisect
        pos = (bisect.bisect_left(I, x = newI[0] ,   key = lambda x : x[0]     ))
        # print(pos)
        I.insert( pos, newI  )
        # I.append(newI)
        # I.sort()
        # print(I)
        res = list()
        res.append(   [  I[0][0] , I[0][1]       ]     )
        
        for i in range(1,len(I)):
            if res[-1][1] >= I[i][0] :
                res[-1][1] = max(    res[-1][1]   , I[i][1]   )
            else:
                res.append( [  I[i][0] , I[i][1] ]    )
        return res