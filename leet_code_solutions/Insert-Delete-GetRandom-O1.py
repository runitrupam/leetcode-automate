import random
class RandomizedSet:

    def __init__(self):
        self.dt = {}
        self.A = list()
        
    def insert(self, val: int) -> bool:
        if val in self.dt:
            return False
        else:
            self.dt[val] = len(self.A) # O(1)
            self.A.append(val)
            # print(self.A)
            return True

    def remove(self, val: int) -> bool:
        if val in self.dt:
            ind = self.dt[val]
            last_val = self.A[-1]
            self.A[ind] = last_val  # change the val of last element and the elem at ind.
            self.A.pop()                     # O(1)
            self.dt[last_val] = ind # change the dict val to position 
            # print(self.A,val , self.dt)

            self.dt.pop(val) # O(1)
            return True
        else:
            return False

    def getRandom(self) -> int: 
        # print(self.A)
        index = random.randint(0,len(self.A)-1)
        return self.A[index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()