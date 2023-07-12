class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:


        dp = dict()

        for i,ch in enumerate( order):
            dp[ch] = i
        # print(dp)

        def check_order( s1 , s2 ):
            nonlocal dp
            if s1 == s2:
                return True
            n1 = len(s1)
            n2 = len(s2)
            if n1 > n2:
                if s1[:n2] == s2:
                    return False

            for i in range( min( len(s2) ,  len(s1))):
                # print(  s1[i]  , s2[i]   , dp[ s1[i] ] , dp[s2[i]] )
                if  s1[i]  == s2[i]:
                    continue
                elif dp[ s1[i] ] > dp[s2[i]]:
                    return False
                elif dp[ s1[i] ] < dp[s2[i]]:
                    return True
            return True 
        
        for j in range( 0,len(words)-1):
            if check_order(   words[j]  , words[j+1]  ) == False:
                return False
        return True