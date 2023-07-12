class Solution:
    def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
        '''
        n = len(G)
        res = []
        seen = set([0])
        def bfs( node , temp_list ):
            nonlocal seen , res, n
            # print(temp_list , node , n-1)
            if node == n-1:
                res.append(temp_list)
                return
            for k in G[node]:
                if k not in seen:
                    seen.add(k)
                    bfs( k , temp_list + [k] )
                    seen.remove(k)
        bfs(0,[0])
        return res
        '''


        n = len(G)
        backG = defaultdict(list)
        for g in range(n):
            for node in G[g]:
                backG[node].append(g)
        print(backG)

        n = len(G)
        res = []
        seen = set([n-1])
        def backtrack( node , temp_list ):
            nonlocal seen, res, n, backG
            # print(temp_list , node ,backG[node] )
            if node == 0:
                temp_list.reverse()
                res.append(temp_list)
                return
            for k in backG[node]:
                if k not in seen:
                    seen.add(k)
                    backtrack( k , temp_list + [k] )
                    seen.remove(k)
        backtrack(n-1,[n-1])
        return res



