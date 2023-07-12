class Solution:
    def pacificAtlantic(self, H: List[List[int]]) -> List[List[int]]:
        # ------------
        # |XXXXXXXXXX|
        # |X        Y|
        # |X        Y|
        # |XYYYYYYYYY|
        # ------------
        # start by traversing the grid from top,left (pacific ocean) and bottom,right (atlantic ocean)
        # dfs each (r,c)
        # visit each r,c neighbors and add to a list (pacific,atlnt) under conditions (r>0,c>0,height>=prevheight,r==ROWS,c==COLS,(r,c) in visit)
        # finally loop through 2 lists (pacific,atlnt) and return the 1 coordinate in boths

        heights = H
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
        '''# go with BFS 15% faster
        dire = [ (0,1) , (1,0) , (-1,0) , (0,-1)  ]
        visitP = set() # visited
        visitA = set() # atlantic

        def bfs(r,c,visit):
            q = deque()
            q.append((r,c))
            visit.add( (r,c)  )

            while q:
                r,c = q.popleft()
                for i,j in dire:
                    if 0 <= i+r < len(H) and 0 <= c + j < len(H[0]) \
                        and (r+i,c+j) not in visit and H[r+i][c+j] >= H[r][c]  :
                                q.append( (r+i,c+j) )
                                visit.add(   (r+i,c+j)  )
            

        # get all positions to be visited by 1st row == pacific 
        # get all positions to be visited by Last row == atlantic
        for c in range(len(H[0])):
            bfs( 0,c,visitP )
            bfs(len(H)-1,c,visitA)
        # print(visitP,visitA)
        # get all positions to be visited by 1st col == pacific 
        # get all positions to be visited by Last col == atlantic
        for r in range(len(H)):
            bfs( r,0,visitP )
            bfs(r,len(H[0])-1,visitA)
        
        return list(  visitP & visitA   )
        '''







'''
        Passes beats only 5 % .. .DFs approach is slow , as same , point reached again . 
        dir = [ (0,1) , (1,0) , (-1,0) , (0,-1)  ]
        seen = set()

        # @cache
        # We can't use cache or dp , as test cases will fail because , lets say , 3 to 4 , u can't go , But u store dp[same row , 4] = False ... But u could have gone from 4 to 3 . 

        def dfs(r,c,ocean):         
            if (r == 0 or c == 0) and ocean == 'p':
                return True
            if (r == len(H) - 1 or c == len(H[0]) - 1 ) and ocean == 'a':
                return True
            seen.add((r,c,ocean))

            for i , j in dir:
                if 0 <= i+r < len(H) and 0 <= c + j < len(H[0]) and (r+i,c+j,ocean) not in seen:
                    if H[r][c] >= H[i+r][j+c] :
                        if dfs(i+r , c+j , ocean ):
                            seen.remove((r,c,ocean))
                            return True
            return False
        # print(dfs(1,4,'p'))

        op = []
        for i in range(len(H)):
            for j in range(len(H[0])):
                if dfs(i,j,'p') and dfs(i,j,'a'):
                    op.append(  [i,j]  )
        return op

'''