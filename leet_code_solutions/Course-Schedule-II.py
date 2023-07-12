class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        task_done_before = defaultdict(list) # tasks to be done before this one
        task_dependent = defaultdict(list) # tasks dependent on me 

        for t1,t2 in prerequisites :
            task_done_before[t1].append(t2)
            task_dependent[t2].append(t1)

        # If all taska are dependent on others  , then cycle is found .
        if len(task_done_before.keys()) == numCourses:
            return []

        s = list() # USING DFS approach.  ,,, u can use a Queue , for BFS approach .

        # At least one task won't be present
        for i in range(numCourses):
            if i not in task_done_before:
                s.append(i)

        # print(task_done_before , s , task_dependent)
        visited = set()
        res = []
        while(s):
            task_to_complete = s.pop()
            if task_to_complete in visited:
                continue
            can_complete = 1            
            if task_to_complete in task_done_before:
                for t2 in task_done_before[task_to_complete]:
                    if t2 not in visited:
                        can_complete = 0
                        break
            if can_complete == 1:
                visited.add(task_to_complete)
                res.append(task_to_complete)
                if task_to_complete in task_dependent:
                    for j in task_dependent[task_to_complete]:
                        s.append(j)
            # print(visited ,task_to_complete )

        # Some tasks coudn't be completed
        if len(res) != numCourses:
            return []
        return res


                


