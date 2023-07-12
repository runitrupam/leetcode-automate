class Solution:
    def canJump(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True

        i = 0
        res = A[0]
        i = 1

        while(res > 0 and i < len(A)):
            res = max(res - 1 , A[i])
            if res <= 0 or i == len(A) - 1 :
                if i == len(A)-1:
                    return True
                else:
                    return False
            # print(res,i)
            i+=1
        return False