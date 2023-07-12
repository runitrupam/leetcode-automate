class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_now = [1000 for i in range(len(cost))]
        min_cost_now[0] = 0
        min_cost_now[1] = 0
        for i in range(2,len(cost)):
            
            min_cost_now[i] = min(min_cost_now[i-1] + cost[i-1] , cost[i-2] + min_cost_now[i-2]   )
        return min(min_cost_now[-1] + cost[-1] , min_cost_now[-2] + cost[-2]  )