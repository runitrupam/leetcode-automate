class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        dict = defaultdict(int)
        dict[0] =1
        output = 0
        Sum = 0
        for n in nums:
            Sum +=n
            m = Sum%k
            output += dict[m]
            dict[m]+=1
        return output
        '''
        # TLE
        div = k
        pref = [nums[0]]
        for k in range(1,len(nums)):
            pref.append(  pref[-1] + nums[k] )
        # print(pref)

        # suffix = [0] * len(nums)
        # suffix[-1] = nums[-1]
        # for k in range(len(nums)-2,-1,-1):
        #     suffix[k] = suffix[k+1] + nums[k]
        # print(pref,suffix)

        n =len(nums)
        res = 0
        k = div
        for i in range(n):
            if nums[i] % k == 0:
                res += 1
            for j in range(i+1,n):
                su_m = pref[j] - ( pref[i-1] if i > 0 else 0 )
                # print(i,j,su_m)
                if su_m % k == 0:
                    res += 1
        return res
        '''
            
                