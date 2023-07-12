'''
Time Complexity and Space Complexity:
Time complexity: O(N log N + N log K), where N is the number of projects and K is the number of projects that we can select. Sorting the "projects" vector takes O(N log N) time, and adding and removing elements from the priority queue takes O(log K) time. The while loop that adds the available projects to the priority queue runs at most N times, and the for loop that selects the projects to complete runs K times.

Space complexity: O(N + K), where N is the number of projects. The space is used to store the "projects" vector. The priority queue used in the solution has a maximum size of K,
'''

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return w + sum(nlargest(k, profits))
        n = len(profits)
        Projects = []
        for i in range(n):
            Projects.append(  (   capital[i],profits[i]    )     )

        Projects.sort() # NlogN

        max_capital = []

        i = 0
        while k > 0:
            while i < n  and  Projects[i][0] <= w :
                heapq.heappush( max_capital , -Projects[i][1]  )
                i += 1
            if len( max_capital) == 0:
                break
            
            w -= heapq.heappop(max_capital)
            k -= 1
        return w


'''
# Not possible to do this using two heaps
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        lesser_capital = []
        greater_capital = []

        Projects = []
        for i in range(n):
            Projects.append(  (   capital[i],profits[i]    )     )
            if capital[i] > w:
                heapq.heappush( greater_capital , ( profits[i] ,  capital[i] )  ) # i want minimum capital
            else:
                heapq.heappush( lesser_capital , ( - profits[i] ,  capital[i] )   ) # i want gt capitals
            # problem for each lesser capital , i want then highest profit . 
            # but each time , ur capital changes , u have to move the greater capital to lesser capital .
'''


