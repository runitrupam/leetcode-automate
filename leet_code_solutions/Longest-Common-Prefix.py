class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        '''
        ["flower","flow","flight"]
        ["dog","racecar","car"]
        ["","fdsd"]
        [""]
        ["as","asd"]
        ["ab", "a"]
        
        '''
        
        j = 1
        curr_prefix = strs[0]
        while(j < len(strs) and len(curr_prefix) >= 1):
            
            for k in range( 0  , min(    len(curr_prefix)  , len(strs[j])   )    ):
                
                if strs[j][k] != curr_prefix[k]:
                    curr_prefix = '' + curr_prefix[:k]
                    break
            # print( curr_prefix   , min(    len(curr_prefix)  , len(strs[j])   )  )
            curr_prefix = '' + curr_prefix[:  min(    len(curr_prefix)  , len(strs[j])   )   ]

            j+=1
        return curr_prefix
                