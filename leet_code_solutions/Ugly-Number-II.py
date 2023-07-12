class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''
        store the index , value of each multiple of 2 , 3 , 5 being used
        
        
        '''
        
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
        
        
        
        
        '''
        Using map but tle
        count = 0
        
        
        li = [1,2,3,4,5,6,8,9,10,12]
        sp = set(li)       

        if n <= 10:
            return li[n-1]
        count = 10
        i = 13
        while(  count < n  ):
            if i % 2 == 0 and int(i/2) in sp:
                sp.add(i)
                count +=1
            elif i % 3 == 0 and int(i/3) in sp:
                sp.add(i)
                count +=1
            elif i % 5 == 0 and int(i/5) in sp:
                sp.add(i)
                count +=1
            print(sp)
            if count == n:
                return i
            
            i+=1
        '''