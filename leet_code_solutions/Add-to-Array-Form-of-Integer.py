'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        x = 1
        N = 0
        for i in range(len(num) -1 , -1 , -1 ):
            N = x * num[i] + N
            x = x * 10
        N = N + k
        print(N)
        
        return [int(j) for j in str(N)]
''' 
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        carry = 0

        for i in range( len(num) - 1 , -1 , -1  ):
            

            carry += num[i] + k%10

            num[i] = carry % 10 
            carry = carry // 10
            k = k // 10
        
        # print(k,carry , num )
        while k or carry:
            carry += k % 10 
            num.insert(0, carry % 10  )
            k = k//10
            carry = carry // 10
        return num
