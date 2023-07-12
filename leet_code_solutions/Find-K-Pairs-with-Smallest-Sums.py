class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Heap initialization 
        queue = [] 
        def push(i, j): 
            # In Python heap is a min-heap 
            # Therefore, we use a tuple, first element is a sum (the priority), then pair itself 
            if i < len(nums1) and j < len(nums2): 
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])     
        push(0, 0) 
        # Set to keep track of pairs we have already pushed into the heap 
        # It's needed because we are doing "push(i+1, j)" and "push(i, j+1)" separately 
        # If not using this visited set, we will end up pushing many duplicate pairs into the heap 
        visited = set() 
        visited.add((0, 0)) 
        result = [] 
        while queue and len(result) < k: 
            _, i, j = heapq.heappop(queue) 
            result.append([nums1[i], nums2[j]]) 
            if i+1 < len(nums1) and (i+1, j) not in visited:  
                push(i+1, j) 
                visited.add((i+1, j)) 
            if j+1 < len(nums2) and (i, j+1) not in visited:  
                push(i, j+1) 
                visited.add((i, j+1)) 
        return result 
                                                                                                                                                                                                                                                                        