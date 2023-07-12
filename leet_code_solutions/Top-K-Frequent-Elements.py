class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for i in nums:
            if i in d:
                d[i] = d.get(i, 0) + 1
            else:
                d[i] = 1

        sorted_tuple = sorted(d.items(), key=lambda x:x[1], reverse=True)
        
        return [sorted_tuple[i][0] for i in range(k)]