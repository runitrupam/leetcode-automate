class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dfs(i,j):

            if i == len(word1) or j == len(word2):
                return len(word1) - i + len(word2) - j
            
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            else:
                ins = dfs(i,j+1)
                dele = dfs(i+1,j)
                repla = dfs(i+1,j+1)
                return 1 + min(ins, dele , repla)
        return dfs(0,0)