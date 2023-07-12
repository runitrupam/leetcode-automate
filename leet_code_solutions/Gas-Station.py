'''
Here's the plan:

First, it is possible to complete the circuit if and only if the total amount of gas on the circuit is sufficient to drive the circuit. More formally: sum(gas) >= sum(cost).
The starting station can be determined by starting at some stationa(say, a = 0) and noting whether a station b on the circuit is unreachable due to lack of gas. If all are reachable, then a is our answer. If not, the start is not anor is any station between a andb.
We reset the tank to zero and repeat.
The last station that is unreachable in this process, say stationz, is our answer.
Why does this work? Recall there's enough gas to complete the circuit. If it were possible to "borrow" gas to get to the next station, the station requiring the most borrowed gas overall is stationz. Thus, starting at stationz is the answer.


'''

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        if sum(gas) < sum(cost): return -1   #   Example: gas = [1,2,3,4,5]  cost = [3,4,5,1,2]
                                             #
        tank = idx = 0                       #   i  gas  cost   tank        start
                                             #  ––– –––  ––––   –––––––––   –––––
        for i in range(len(gas)):            #   start = 0              0     0
                                             #   0   1    3    0+1-3 = -2     1    reset tank to 0, start to 0+1 = 1
            tank+= gas[i]-cost[i]            #   1   2    4    0+2-4 = -2     2    reset tank to 0, start to 2+1 = 2 
            if tank < 0: tank, idx = 0, i+1  #   2   3    5    0+3-5 = -2     3    reset tank to 0, start to 2+1 = 3
                                             #   3   4    1    0+4-1 =  3     3    
        return idx                           #   4   5    2    3+5-2 =  6     3
                                             #
                                             #  See explanation in problem description to verify that i = 3 works