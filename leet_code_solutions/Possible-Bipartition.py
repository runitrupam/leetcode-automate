class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        @cache
        def dfs(node , group):
            if groups[node] == -1:
                groups[node] = group
            else:
                return groups[node] == group
            for n in adjDict[node]:
                if not dfs(n , 1 - group):
                    return False
            return True
        adjDict , groups = defaultdict(list) , [-1 for i in range(N)]
        for u , v in dislikes:
            adjDict[u - 1].append(v - 1) # 0 indexing
            adjDict[v - 1].append(u - 1) # 0 indexing
        for i in range(N):
            if groups[i] == -1 and not dfs(i , 0):
                return False
        return True