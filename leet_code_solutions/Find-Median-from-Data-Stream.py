from heapq import heapify , heappush,heappop
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap , stores 1st half of sorted array
        self.right = [] # min heap ,stores 2nd half of sorted array
        heapify(self.left)
        heapify(self.right)
    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or -self.left[0] > num :
            heappush(self.left,-num)
        else:
            heappush(self.right,num)
        
        if len(self.left) > len(self.right) + 1 :
            ele = heappop(self.left)
            heappush(self.right, -ele)
        elif len(self.right) > len(self.left) + 1 :
            ele = heappop(self.right)
            heappush(self.left, -ele)
        # print(num , self.left , self.right)
    def findMedian(self) -> float:
        
        if len(self.left) > len(self.right):
            # ele = heappop(self.left)
            return -self.left[0]
        elif len(self.right) > len(self.left):
            # ele = heappop(self.right)
            return self.right[0]
        else:
            return ( -self.left[0] +  self.right[0])/2.0
        
        
'''        
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr=SortedList([])

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        
    def findMedian(self) -> float:
        n=len(self.arr)
        if(n%2==0):
            return(self.arr[n//2]+self.arr[n//2-1])/2
        else:
            return(self.arr[n//2])
'''
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()