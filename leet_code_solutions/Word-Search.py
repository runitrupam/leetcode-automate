

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(board),len(board[0])
        
        counter = Counter()
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] += 1
        
        # less char in board
        # print(set(word) , set(counter.keys())   )
        if len(set(word)) > len(set(word).intersection(set(counter.keys()))):	
            return False
        
        # inverse word if it's better
        if counter[word[0]] > counter[word[-1]]:                                
             word = word[::-1]  
                
        def backtrack(i,j,k,visited):
            if board[i][j] == word[k]:
                if k==len(word)-1:
                    return True
                for xn,yn in directions:
                    x,y = i+xn,j+yn
                    if 0<=x<m and 0<=y<n and (x,y) not in visited:
                        if backtrack(x,y,k+1,visited.union({(x,y)}))==True:
                            return True
            return False
        
        for i, j in product(range(m), range(n)):
            if backtrack(i,j,0,{(i,j)}):
                return True
        return False