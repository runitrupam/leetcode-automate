from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from heapq  import heappush ,heapify , heappop
        if n == 0:
            return len(tasks)
        
        dp = Counter(tasks)
        heap = [-val for val in dp.values()]
        heapify(heap)
        queue = deque()
        timetaken = 0
        while(heap or queue):
            timetaken += 1
            if heap:
                freq = - heappop(heap)
                freq -= 1
                if freq:
                    queue.append([  freq, timetaken+n  ])
            while queue and queue[0][1] == timetaken:
                heappush(heap,-  queue.popleft()[0] )
            
        return timetaken
        
        
        
        
        
        
        
        
        
        if n == 0:
            return len(tasks)
        
        # Count frequency of each task
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] += 1
            else:
                hashmap[task] = 1
        
        # Build a max-heap of all the frequencies
        heap = [-val for val in hashmap.values()]
        heapq.heapify(heap)
        
        # Initialize a queue to hold the tasks which are waiting for cool down period
        queue = deque() # [frequency, timeAtWhichItCanStartExecuting]
        
        timeTaken = 0
        # Iterate till all the tasks are processed.
        while heap or queue:
            timeTaken += 1
            # Pick the task from heap having the maximum frequency.
            if heap:
                frequency = -heapq.heappop(heap)
                # Since only one task can be processed in a unit time. So process the task.
                frequency -= 1
                # Now if this task is left then it will have to wait for the cooldown period. So, enque the task till its cooldown period is expired.
                if frequency:
                    queue.append([frequency, timeTaken + n])
                    
            # Now process the tasks whose cooling period is expired.
            while queue and queue[0][1] == timeTaken:
                heapq.heappush(heap, -queue.popleft()[0])
        
        return timeTaken
        '''
        TLE
        if n == 0:
            return len(tasks)
        dp = Counter(tasks)
        B = []
        for k in dp:
            B.append([k,dp[k]])
        B.sort(key = lambda x : x[1] , reverse = True)        
        ind = 0
        total_tasks = len(tasks)
        curr_used_tasks = {}
        time = 0
        while(total_tasks):
            keys_used = list( curr_used_tasks.keys())
            for key in keys_used:
                curr_used_tasks[key] -= 1
                if curr_used_tasks[key] == 0:
                    curr_used_tasks.pop(key)
            idle = 1
            for ind in range(len(B)):
                k,c = B[ind]
                if dp[k] > 0 and not(curr_used_tasks.get(k,0 )):
                    dp[k] -= 1
                    total_tasks -= 1
                    curr_used_tasks[k] = 1 + n 
                    idle = 0
                    B[ ind  ][1] -= 1
                    B.sort(key = lambda x : x[1] , reverse = True)
                    if B[-1] == 0:
                        B.pop()
                    # print(k)
                    break
            time += 1
            if idle:
                pass
                # print('idle')
            
            # print(curr_used_tasks,dp)

        return time
        '''
            
            
            
            
        
        