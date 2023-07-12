class Solution:
    def calculate(self, s: str) -> int:
        currNum, numStack,sign = 0,[],'+'
        digits = set( [x for x in '0123456789']  )
        '''
        "1-1+1"

        stack stores ,
        1 , -1 , 1
        sum(numStack)
        gives 1 
        '''
        for i,char in enumerate(s):
            if char in digits:
                currNum = currNum*10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    numStack.append(currNum)
                elif sign == '-':
                    numStack.append(-currNum)
                elif sign == '*':
                    numStack.append(numStack.pop() * currNum)
                elif sign == '/':
                    numStack.append(int(numStack.pop() / currNum))
                sign = char
                currNum = 0
        
        return sum(numStack)