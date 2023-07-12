class MyQueue:
    #Amortized solution .
    # After push u go to search in master or slave once only ,after move func. is called. 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.slave.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.master:
            self.move()
        return self.master.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.master:
            return self.slave[0]
        return self.master[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.master) and not len(self.slave)

    def move(self) -> None:
        while self.slave:
            self.master.append(self.slave.pop())    
    
    
    '''
    #O(N)
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)        

    def pop(self) -> int:
        while(self.s1):
            x = self.s1.pop()
            self.s2.append(x)
        if self.s2:
            res = self.s2.pop()
            while(self.s2):
                x = self.s2.pop()
                self.s1.append(x)
            return res
        return

    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        if self.s1:
            return False
        else:
            return True
    '''

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()