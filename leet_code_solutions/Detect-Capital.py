class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True
        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper():
            # print(word[1:],word[1:].isupper())
            if word[1:].islower():
                return True
            else:
                return False
        return False

        