
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal :
            frequency = [0]*26
            for ch in s:
                frequency[ord(ch)-ord('a')] += 1
                if frequency[ord(ch)-ord('a')] == 2:
                    return True
            return False
        first_index = -1
        second_index = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if first_index == -1:
                    first_index = i
                elif second_index == -1:
                    second_index = i
                else:
                    return False
        if second_index == -1:
            return False
        return s[first_index]==goal[second_index] and s[second_index] == goal[first_index]