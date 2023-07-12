class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        A = asteroids.copy()
        prev_len = 0
        while( prev_len != len(A)   ):
            prev_len = len(A)
            res = []
            for i in range(len(A)):
                # print(res, i , A[i])
                if res and res[-1] >= 0 and A[i] < 0 and abs(A[i]) > res[-1]:
                    res[-1] = A[i]
                elif res and res[-1] >= 0 and A[i] < 0 and abs(A[i]) == res[-1]:
                    res.pop()
                elif res and res[-1] <= 0 and A[i] > 0 : #and abs(res[-1]) < A[i]:
                    #res[-1] = A[i]
                    res.append(A[i])
                # elif res and res[-1] == -1 * A[i]:
                #     res.pop()
                elif not res or (  res[-1] >= 0 and A[i] >= 0     ) \
                         or (  res[-1] <= 0 and A[i] <= 0     )  :
                    res.append(A[i])
            A = res
            # print(res)
        return A
        '''

        class Solution:
        def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            stack = []

            for a in asteroids:
            if a > 0:
                stack.append(a)
            else:  # A < 0
                # Destroy previous positive one(s)
                while stack and stack[-1] > 0 and stack[-1] < -a:
                stack.pop()
                if not stack or stack[-1] < 0:
                stack.append(a)
                elif stack[-1] == -a:
                stack.pop()  # Both explode
                else:  # stack[-1] > current
                pass  # Destroy current, so do nothing

            return stack




        '''