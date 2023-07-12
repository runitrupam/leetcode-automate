class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        res = 0
        curr_zeros = 0
        for i in range(len(flowerbed)):

            empty = flowerbed[i]
            if empty == 0:
                curr_zeros += 1
            elif empty == 1 and curr_zeros > 0:
                if curr_zeros%2 == 0:
                    res += (curr_zeros - 1)//2
                else:
                    res += (curr_zeros)//2              
                # if res >= n:
                #     return True

                curr_zeros = 0
        # print(curr_zeros,res)          
        if curr_zeros > 0 and curr_zeros%2 == 0:
            res += (curr_zeros - 1)//2
        else:
            res += (curr_zeros)//2    
        # print(curr_zeros,res)          
        if res >= n:
            return True
        return False
'''
0 0 0, 0 0 0, 0 0 0

2 = 0
3 = 1
4 = 1
5 = 2
6 = 2
7 = 3
8 = 3
9 = 4
10 = 4
'''