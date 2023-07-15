class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        
        visited = dict()
        freq = 0
        l = 0
        res = 0
        for r in range(n):
            visited[s[r]] = 1 + visited.get(s[r],0)
            
            freq = max(freq , visited[s[r]])
            
            while(   r-l+1 - freq   > k ):
                
                visited[s[l]] -=1
                l+=1
            res = max(res, r-l+1 )
        return res
            
            