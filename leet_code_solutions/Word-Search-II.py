class Trie:

    def __init__(self):
        self.children = dict()
        self.endOfWord = False
        '''
        Here a dictionary of dict concept is used . 
        And for the whole word inserted , we add a # as a key .
        O(len(word)) --> For all cases
        '''
    # def __str__(self):
    #     return self.children
    # def __repr__(self):
    #     return str(self.children.values)   
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.endOfWord = True




class Solution:
    def findWords(self, B: List[List[str]], words: List[str]) -> List[str]:
        obj = Trie()
        for w in words:
            obj.insert(w)
        
        words = set(words)
        r = len(B)
        c = len(B[0])
        res = set()
        
        def dfs(node , r , c , word):
            # print(r,c, word )
            if r < 0 or c < 0 or r >= len(B) or c >= len(B[0]) or B[r][c] == '#' or B[r][c] not in node.children:
                return
            word += B[r][c]
            node = node.children[B[r][c] ]

            if node.endOfWord and word in words:
                res.add(word)
                node.endOfWord = False # to keep checking for next words having this one as a prefix
                words.remove(word)
                
            temp = B[r][c]   
            B[r][c] = '#' # To not use the same letter again
            dfs(node,r + 1,c,word  )
            dfs(node,r ,c + 1,word  )
            dfs(node,r - 1,c,word  )
            dfs(node,r,c - 1,word  )
            B[r][c] = temp
        
        for i in range(r):
            for j in range(c):
                dfs(obj,i,j,""  )
                obj = Trie()
                for w in words:
                    obj.insert(w)
                
        return list(res)
        
        
        
        