class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        lookup = {}
        words_set = set(words)
        ans = []

        def dfs(word, words_set):
            if word == "":
                return True

            for i in range(len(word)):
                if word[:i+1] in words_set:
                    if dfs(word[i+1:], words_set):
                        return True
            return False

        for word in words:
            words_set.remove(word)
            if dfs(word, words_set):
                ans.append(word)
            words_set.add(word)
        return ans