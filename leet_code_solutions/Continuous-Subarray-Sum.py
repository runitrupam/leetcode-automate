class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        The optimal solutions for this kind of problems are always Hashmap + Prefix Sum!

        Note that if we first generate the whole prefix sum list of the input array, then we could get all subarray sum in O(n^2), which is good but not optimal.
        The idea comes: Also take Hashmap into use with Prefix Sum, reduce time to O(n).

        We should initiate a Hashmap
        key is prefix sum % k,
        value is index of the current prefix sum.

        When we reach some position, for example i, whose prefix sum % k is already in the Hashmap, and Hashmap[prefix sum % k] = j, then it means that nums[j+1:i+1] % k == 0, which is what we want! (We need to check i - j >= 2, as given)

        Time: O(n)
        Space: O(min(n, k))
        There could be at most k keys in the Hashmap.

        '''
        n = len(nums)

        mp = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum = prefix_sum % k
            if prefix_sum in mp:
                # I know that sum between mp[prefix_sum] + 1 and i is multiple of K, so I don't have to include mp[prefix_sum]
                if i - mp[prefix_sum] > 1:
                    return True
            else:
                # if prefix_sum doesn't exists, then add its index, otherwise don't update it, i would always prefer to keep the
                # oldest index, so that I can get length of atleast 2
                mp[prefix_sum] = i

        return False
        
        
        '''
        23 2 4 6 7
        7
        6 , 6 7
        4 , 4 6  , 4 6 7
        2, 2 4 ,2 4 6 , 2 4 6 7
        23 , 23 2 , 23 2 4 , 23 2 4 6 ,23 2 4 6 7
        
        
        '''