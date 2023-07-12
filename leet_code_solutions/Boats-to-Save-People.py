
'''

1 2 2 3 --> l=3

1,3 x = c += 1 , j -=1 , i = i
1,2 yes , c+= 1 , i+=1 , j-=1

if i >= j:
    c+=1
    return c


TC = O(N * logN)
this can be reduced as there is a constraint on the weight of people.
which have to be less than weight

SO TC = O(N)

'''



class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        #people.sort() or below step to sort in O(N).
        count = [0] * (limit+1)
        for p in people:
            count[p] += 1

        idx = 0
        for val in range(1, limit+1):
            while count[val] > 0:
                people[idx] = val
                idx += 1
                count[val] -= 1

        # Pointers approach 
        i = 0
        j = len(people) - 1
        c = 0
        while( i <= j):
            if people[i] + people[j] <= limit:
                i+=1
                j-=1
                c+=1
            else:
                j-=1
                c+=1

        return c