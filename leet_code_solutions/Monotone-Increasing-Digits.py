class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
      
        st = str(n)
        st2 = st
        for i in range(len(st)):
            if i+1 < len(st) and st[i] > st[i+1]:
                st2 = st[:i]
                st2 += str(int(st[i]) - 1 )
                #st[i] = str(int(st[i]) - 1 )
                for j in range(i+1,len(st)):
                    st2 += '9'
                j = i    
                #print(st2)
                while j>0 and st2[j] < st2[j-1] :
                    st2 = st2[:j-1] + str(int(st2[j-1]) - 1 ) + '9' + st2[j+1:]
                    j-=1
                break    
        return int(st2)        