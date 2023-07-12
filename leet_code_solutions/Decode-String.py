class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        self.lastkeyends = 0
        
        def helper(i, key=""):
            if i>=n:
                return ""
            
            if s[i].isdigit():
                k = int(s[i])
                j = i + 1
                
                while j < n and s[j].isdigit():
                    k = k * 10 + int(s[j])
                    j += 1
                    
                r = k * helper(j, key) # helper gives key

                if self.lastkeyends == n - 1:
                    return key + r

                return key+r+helper(self.lastkeyends + 1)
            
            if s[i] == '[':       
                return helper(i + 1, "") # helper gives key
            
            if s[i] == ']':
                # key completed
                self.lastkeyends = i
                return key
            else: # s[i] is letter
                if i == n - 1:
                    return key + s[i]
                return helper(i + 1, key+s[i])
               
        return helper(0) 