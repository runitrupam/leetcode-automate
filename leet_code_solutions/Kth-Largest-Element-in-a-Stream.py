class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        return self.min_heap[0]
'''
Initialize the class with the value of k and an empty data structure to store the k largest elements encountered so far.
When adding a new element to the stream, check if the size of the data structure is less than k.
If it is less than k, simply add the new element to the data structure.
If it is equal to k, compare the new element with the smallest element in the data structure.
If the new element is larger, remove the smallest element and add the new element.
If the new element is smaller, do not add it to the data structure.
Return the smallest element in the data structure, which represents the kth largest element in the stream.

'''

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)