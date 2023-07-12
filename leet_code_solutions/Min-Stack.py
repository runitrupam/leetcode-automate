class MinStack:
    def __init__(self):
        self.s1 = list()
        self.minval = float('inf')

    # O(1) As using list of list and stores min_val so far  ,, MONOTONIC STACK
    def push(self, val: int) -> None:
        if not self.s1:
            self.minval = val 
        else:
            self.minval = min(val   , self.s1[-1][1]  )

        self.s1.append(   [   val , self.minval     ]    )
        # print(self.s1 , 'pushed' )
        
    def pop(self) -> None:
        if self.s1:
            self.s1.pop()
            # print(self.s1 ,'popped ')

        else:
            return None

    def top(self) -> int:
        if self.s1:
            # print(self.s1 , 'top')
            return self.s1[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.s1:
            # print(self.s1 ,'getmin')
            return self.s1[-1][1]
        else:
            return None

    '''
    # Monotonic stack --> Strictly decreasing stack
    def __init__(self):
        self.s1 = list()
        self.ms = list() # monotonic stack

    def push(self, val: int) -> None:
        self.s1.append(val)
        temp_s = []
        while(  len(self.ms) > 0 and self.ms[-1] < val  ):
            temp_s.append( self.ms.pop()  )
        self.ms.append(val)
        while(temp_s):
            self.ms.append( temp_s.pop()  )
    def pop(self) -> None:
        if self.s1:
            val = self.s1.pop()
            temp_s = []
            while(  len(self.ms) > 0 and self.ms[-1] != val  ):
                temp_s.append( self.ms.pop()  )
            self.ms.pop()
            while(temp_s):
                self.ms.append( temp_s.pop()  )
        else:
            return None

    def top(self) -> int:
        if self.s1:
            return self.s1[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.ms:
            return self.ms[-1]
        else:
            return None
    '''


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()