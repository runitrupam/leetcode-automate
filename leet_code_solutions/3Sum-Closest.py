class Solution:
    def threeSumClosest(self, A: List[int], target: int) -> int:
        A.sort()
        closest_diff = None
        closest_sum = None
        for i in range(len(A) - 2 ):

            j = i + 1 
            k = len(A) - 1
            while(j<k):

                curr_sum = A[i] + A[j] + A[k]

                if curr_sum == target:
                    return target
                if curr_sum < target:
                    j+=1
                else:
                    k -= 1
                abs_diff = abs(target - curr_sum)

                if closest_sum is None or abs_diff < closest_diff:
                    closest_sum = curr_sum
                    closest_diff = abs_diff
        return closest_sum

