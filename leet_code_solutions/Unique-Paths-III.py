
'''
The time complexity of brute force DFS is definitely asymptotically larger than that of dynamic programming.
Since DFS makes 4 recursive calls in the procedure, DFS takes time O(4^(m * n)), where m is the height and n is the width of grid.
Using DP, there are 2^(m * n) distinct subsets of visited cells, and we start from any one of them to visit the remaining unvisited ones. Each cell is at most adjacent to 4 cells, thereby implying the running time O(4 * (m * n) * 2^(m * n)) = O((m * n) * 2^(m * n)).

Let's denote m * n by s = m * n, then DFS takes O(4^s) while DP takes O(s * 2^s) time.
Since

lim(n -> ∞)(4^s / (s * 2^s)) = ∞

we have T(DFS) = ω(T(DP)), or DFS takes exponentially more time than DP.


'''
class Solution:
    def uniquePathsIII(self, G: List[List[int]]) -> int:
        '''
        As the m,n <= 20 
        can be done using recursion .
        '''

        r = len(G)
        c = len(G[0])
        empty = 1
        global res
        for i in range(r):
            for j in range(c):
                if G[i][j] == 1:
                    start_r = i
                    start_c = j
                elif G[i][j] == 0:
                    empty += 1
        res = 0
        def dfs(x,y,empty):
            global res
            if not(  0 <= x < r and 0 <= y < c  and G[x][y] >= 0  ): return 

            if G[x][y] == 2:
                res += empty == 0 # empty is taken 1 more , as here we are checking this .
                # print(res,empty)
                return 
            G[x][y] = -2
            dfs(x,y+1,empty - 1)
            dfs(x,y-1,empty - 1)
            dfs(x+1,y,empty - 1)
            dfs(x-1,y,empty - 1)
            G[x][y] = 0

        dfs(start_r,start_c,empty)
        return res

