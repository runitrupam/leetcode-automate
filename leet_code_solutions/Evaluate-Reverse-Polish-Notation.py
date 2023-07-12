class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []
        # print(tokens)
        for t in tokens:
            # print(t)
            if t == '*':
                res.append( int(res.pop()) * int(res.pop()) )
            elif t == '+':
                res.append( int(res.pop()) + int(res.pop()) )
            elif t == '/':
                b,a  = int(res.pop()) , int(res.pop())
                # print(a,b)
                res.append( a / b )
            elif t == '-':
                b,a  = int(res.pop()) , int(res.pop())
                # print(a,b)
                res.append( a - b )
            else:
                # print('inside this else')
                res.append(t)
        # print(res)
        return int(res[0])