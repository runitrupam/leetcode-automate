class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def lcm(self,a,b):
        return (a*b)/self.gcd(a,b) 
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        LC_M = self.lcm(a,b)
        seq = set()
        for i in range(1,int(LC_M/a) + 1,1):
            seq.add(a*i)
        #print(LC_M/a,int(LC_M/b))    
        for j in range(1,int(LC_M/b) + 1,1):
            seq.add(b*j)
        cand = sorted(list(seq))
        #print(cand)
        #print(int((n-1) / len(cand) ),LC_M)
        ans = (int((n-1) / len(cand) ))*LC_M  + cand[n % len(cand) - 1]
        #print(ans)
        return int(ans)%(10**9+7)
     