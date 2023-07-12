# class StockSpanner:

#     def __init__(self):
        

#     def next(self, price: int) -> int:
        

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, p: int) -> int:
        c, s = 1, self.stack
        while s and s[-1][0] <= p:      # [1] obtain total count of consecutive days with stock
            c += s.pop()[1]             #     price not greater than today's price
        s.append((p,c))                 # [2] collapse counted subintervals into one with aggregated count
        return c
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)