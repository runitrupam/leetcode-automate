class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        d = collections.defaultdict(int)
        t1, t2 = [], []
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    t1.append((i, j))
                if img2[i][j] == 1:
                    t2.append((i, j))
        # print(t1,t2)
        
        res = 0
        for x in t1:
            for y in t2:
                temp = (y[0]-x[0], y[1]-x[1])
                # print(x,y,temp)
                d[temp] += 1
                res = max(res, d[temp])
        # print(d)
        return res