class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = dict()
        ds = dict()
        for i in range(97,123,1):
            dp[chr(i)] = 0
            ds[chr(i)] = 0
        
        for j in range(0,len(p) ):
            dp[p[j]] += 1
        
        
        for j in range(0,min(len(p),len(s) )):
            ds[s[j]] += 1
        # print(dp)
        # print(ds)
        
        res = []
        if dp == ds:
            res.append(0)
        
        for j in range( 1, len(s) - len(p) +1 ):
            
            chr_removed = s[j-1]
            chr_added = s[j + len(p)-1]
            ds[chr_removed] -=1
            ds[chr_added] +=1
            
            if ds == dp:
                res.append(j)
        return res