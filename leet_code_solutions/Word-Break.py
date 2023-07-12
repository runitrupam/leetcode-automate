class TrieNode:
    def __init__(self):
	    # using hashmap to store the child of current node
        self.mp = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        # MEMO. 301 means the maximum length of s.
        self.failed = [False] * 301
    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.mp:
                node.mp[ch] = TrieNode()
            node = node.mp[ch]
        node.isEnd = True
    
    def search(self, s, start):
        if self.failed[start]:
            return False
        if start >= len(s):
            return True
        node = self.root
        for i in range(start, len(s)):
            if s[i] not in node.mp:
                return False
            node = node.mp[s[i]]
            if node.isEnd:
                if self.search(s, i+1):
                    return True
                self.failed[i+1] = True

        return False

            

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp = [False for i in range(len(s)+1)]
        words = set(wordDict)
        dp[0] = True
        
        for i in range(1,len(s)+1):
            
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]
        '''
        words = set(wordDict)
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.search(s, 0)
        # trie
        