class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        rows, cols = defaultdict(list), defaultdict(list)       # [1] all stones within the same row
        for s, (r, c) in enumerate(stones):                     #     and within the same column
            rows[r].append(s)                                   #     belong to the same connected
            cols[c].append(s)                                   #     component; let's store this data
        
        seen, n = set(), len(stones)
        
        def dfs(s):                                             # [2] this function is used to explore a
            if s in seen : return 0                             #     connected component of each stone by
            seen.add(s)                                         #     making recursive calls to adjacent
            r, c = stones[s]                                    #     stones; it returns 1/0 depending on
            for ss in chain(rows[r], cols[c]): dfs(ss)          #     whether the component was already 
            return 1                                            #     explored, thus, allowing to count them
                
        c = sum(dfs(s) for s in range(n))                       # [3] count the number of connected components

        return n - c                                            # [4] in each component, 1 stone will remain