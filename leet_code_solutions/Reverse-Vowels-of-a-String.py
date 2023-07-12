class Solution:
    def reverseVowels(self, s: str) -> str:
        
        v = set(['a','e','i','o','u','A','E','I','O','U'])
        
        
        i = 0
        j = len(s) - 1
        if j == 0:
            return s
        
        st = [x for x in s]
        
        while(i < j):
            if st[i] not in v:
                i += 1
            if st[j] not in v:
                j -= 1
            if st[i] in v and st[j] in v and i < j:
                tp = st[i]
                st[i] = st[j]
                st[j] = tp
                i+=1
                j-=1
        return ''.join(st)
        
        