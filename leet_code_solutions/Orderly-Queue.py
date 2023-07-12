class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        '''
        dacbbea k = 2
        acbbead
        abbeadc
        abeadcb
        aeadcbb
        aadcbbe
        dcbbeaa
        dbbeaac
        deaacbb
        aacbbde
        cbbdeaa
        cdeaabb
        aabbcde
        
        
        
        k = 2
        
        abdcddbbaa
        bbaaabcddd
        bcdddbbaaa
        After trying all combinations , i could reach the lexico smallest string
        dddcbbbaaa
        
        So, the same for k > 2
        '''
        
        
        
        if k == 1:
            mi_n = s
            for i in range(len(s)):
                tp = s[i:] + s[0:i]
                # print(i , tp)
                if tp < mi_n:
                    mi_n = tp
            return mi_n
        
        li = [x for x in s]
        li.sort()
        return ''.join(li)
        
                
                
        
        
        
        