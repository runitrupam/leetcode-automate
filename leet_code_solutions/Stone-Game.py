class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a,b = 0,0
        l = 0
        h = len(piles)-1
        while l<h:
            a += max(piles[l],piles[h])
            b += min(piles[l],piles[h])
            l += 1
            h -= 1
        return a>b