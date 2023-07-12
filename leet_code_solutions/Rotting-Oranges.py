class Solution:
    def orangesRotting(self, G: List[List[int]]) -> int:
        '''
        BFS approach is used . ---> (Because if u go for DFS (At start only there are more bad oranges , which kept increasing . there are multiple paths , so TLE), )
        I store the minute passed , in the queue .
        seen = set --> to store the bad oranges , already added in Queue . 
        Run the code until all the bad oranges are popped out . 
        TLE --> O( N * M)
        '''

        queue = deque()
        dire = [ (0,1) , (1,0) ,(-1,0) ,(0,-1) ]
        minutes = 0
        all_oranges = set()
        seen = set()
        for i in range(len(G)):
            for j in range(len(G[0])):
                if G[i][j] == 2:
                    queue.append((i,j,minutes))
                    seen.add( (i,j) )
                elif G[i][j] == 1:
                    all_oranges.add((i,j ))
        # print(queue ,all_oranges ,seen)
        max_minutes = 0
        while(queue):
            r,c , minutes = queue.popleft() 
            for i , j in dire:
                if  0 <= r + i < len(G) and  0 <= c + j < len(G[0]) :
                    if (r + i,c+j) not in seen and   G[r+i][c+j] == 1:
                        # print((r + i,c+j) ,   )
                        all_oranges.remove( (r + i,c+j) )
                        queue.append((i+r,j+c,minutes+1))
                        seen.add( (i+r,j+c) )
            max_minutes = max(max_minutes , minutes)
        if len(all_oranges) !=0:
            return -1
        return max_minutes
                    
