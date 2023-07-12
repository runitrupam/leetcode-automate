class monotonic_stack:
    def __init__(self):
        self.ms = []
        self.slave_s = []
    
    def add(self,arr):
        x = arr[0]
        pos = arr[1]
        # top/head should be least.
        while( self.ms and self.ms[-1][-0] < x   ):
            self.slave_s.append(self.ms.pop())
        self.ms.append( arr  )
        while self.slave_s:
            self.ms.append(self.slave_s.pop())
        # print(self.ms)
    def delete(self):
        if self.ms:
            return self.ms.pop()
        else:
            return 0

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:


        obj = monotonic_stack()
        res = [0] * len(T)

        for k in range(len(T)-1,-1,-1):
            if k != len(T) - 1:
                # c = 1
                while obj.ms and obj.ms[-1][0] <= T[k]:
                    obj.delete()
                    # c+=1
                if obj.ms and obj.ms[-1][0] > T[k]:
                    res[k] =  obj.ms[-1][1] - k
                obj.add([T[k],k] )
            else:
                obj.add([T[k],k])
            # print(obj.ms , res)
        return res
        