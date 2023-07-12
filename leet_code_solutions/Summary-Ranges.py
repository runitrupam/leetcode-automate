
'''
class Solution:
    def summaryRanges(self, N: List[int]) -> List[str]:
        res = []
        i = 0
        while i < (len(N)):
            j = 1
            while(j<len(N)):
                if i+j < len(N) and N[i] + j == N[i+j] :
                    continue
                elif i+j < len(N) and N[i] + j != N[i+j] :
                    j -= 1
                    break
                elif i+j >= len(N):
                    break
                j += 1
                
            print(i,j)    
            # j -= 1
            if j > 0:
                res.append("{0}->{1}".format(N[i],N[i+j]))
                i = i + j + 1
            elif j <= 0:
                res.append(str(N[i]))
                i = i + 1
        return res
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = [] # [start, end] or [x, y]
        for i, n in enumerate(nums):
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])

        return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]       