from collections import Counter
from collections import OrderedDict

class Solution:
    def topKFrequent(self, words: List[str], k_Num: int) -> List[str]:
        # print(Counter(words))
        # print(set(words))
        
        dp = dict() #OrderedDict()
        for j in words:
            dp[j] = dp.get(j,0) + 1
        li = list()
        for k in dp:
            li.append([k,dp[k]])
        
        li.sort(key = lambda x : x[0] )
        li.sort(key = lambda x : x[1] , reverse = True)        
        p = 0
        res = []
        while( p < k_Num and p < len(li) ):
            res.append(li[p][0])
            p+=1
        return res
        