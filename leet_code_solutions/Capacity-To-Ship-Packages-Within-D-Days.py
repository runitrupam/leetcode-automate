class Solution:
    def shipWithinDays(self, W: List[int], days: int) -> int:
        def count_days(W,max_capacity):
            days = 1
            curr_cap = 0
            for w in W:
                if w + curr_cap > max_capacity:
                    days+=1
                    curr_cap = w
                else:
                    curr_cap += w
            return days

        l = max(W)
        r = sum(W)

        while(l < r):
            m = l + (r-l)// 2
            #  this line will fail the code cause , u can decrease the cap. more
            # if count_days(W, m ) == days:
            #     return m
            if count_days(W, m ) <= days:
                r = m
            else:
                l = m+1
        return l 
            