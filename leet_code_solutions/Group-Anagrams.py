class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())
        '''# from collections import Counter
        dp = dict()
        # res = []
        for s in strs:
            # print(s)
            # t = sorted(s)
            t = ''.join(sorted(s)) 
            # res.append(  [t , s] )
            if t in dp:
                dp[t].append(s)
            else:
                dp[t] = [s]
        # print(dp.keys())
        return (list(dp.values()))
        # print(dp)
        # print(strs)'''