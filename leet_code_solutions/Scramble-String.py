"""
Complexity
Time complexity: O(n4)O(n^4)O(n 
4
 )
since for each character in s1, we are trying out all possible splits of the string which takes O(n2)O(n^2)O(n 
2
 ) time and we are calling the recursion twice for each split which takes another O(n2)O(n^2)O(n 
2
 ) time. And for each such problem, we are storing it in a dictionary which takes O(1)O(1)O(1) time. So overall time complexity is O(n4)O(n^4)O(n 
4
 ).

Space complexity: O(n3)O(n^3)O(n 
3
 )
since we are using a dictionary to store previously solved problems and the depth of the recursion tree can go up to n. Therefore, the space complexity of this solution is O(n^3)
 ).


"""

'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Base cases

        n = len(s1)

        # If both strings are not equal in size
        if len(s2) != n:
            return False

        # If both strings are equal
        if s1 == s2:
            return True

        # If code is reached to this condition then following this are sure:
        # 1. size of both string is equal
        # 2. string are not equal
        # so size is equal (where size==1) and they are not equal then obviously false
        # example 'a' and 'b' size is equal, string are not equal
        if n == 1:
            return False

        key = s1 + " " + s2

        # Check if this problem has already been solved
        if key in self.mp:
            return self.mp[key]

        # For every iteration it can two condition
        # 1. We should proceed without swapping
        # 2. We should swap before looking next
        for i in range(1, n):
            # ex of without swap: gr|eat and rg|eat
            without_swap = (
                # Left part of first and second string
                self.isScramble(s1[:i], s2[:i])
                and
                # Right part of first and second string;
                self.isScramble(s1[i:], s2[i:])
            )

            # If without swap gives us the right answer then we do not need
            # to call the recursion with swap
            if without_swap:
                return True

            # ex of with swap: gr|eat rge|at
            # here we compare "gr" with "at" and "eat" with "rge"
            with_swap = (
                # Left part of first and right part of second
                self.isScramble(s1[:i], s2[n-i:])
                and
                # Right part of first and left part of second
                self.isScramble(s1[i:], s2[:n-i])
            )

            # If with swap gives us the right answer then we return True
            # otherwise, the for loop does its work
            if with_swap:
                return True

        self.mp[key] = False
        return False

    # for storing already solved problems
    mp = {}

'''

class Solution:
    def isScramble(self, first: str, second: str) -> bool:
        @cache
        def dp(a: str, b: str) -> bool:
            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            return any(
                dp(a[:i], b[:i]) and dp(a[i:], b[i:]) or \
                dp(a[:i], b[-i:]) and dp(a[i:], b[:-i])
                for i in range(1, len(a))
            )

        return dp(first, second)