'''
Our queue will be ordered so that the senators with earlier voting power come first (to the left of the queue).
To goal is to have the earliest senator of each queue fight each other to see who gets to eliminate the other depending on their position.
Obviously, the one with the earlier position will win.
The loser is removed from the queue since they are no longer active.
The winner will go to the end of the queue for the next round.
We keep doing this until one queue is empty which means there are no more senators on the team.

Tc = O(N)


'''

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQ = deque()
        dQ = deque()
        
        for i,c in enumerate(senate):
            if c == "R":
                rQ.append(i)
            else:
                dQ.append(i)
        while dQ and rQ:
            d,r = dQ.popleft(), rQ.popleft()
            
            if d < r:
                dQ.append(d+len(senate))
            else:
                rQ.append(r+len(senate))
        return "Radiant" if rQ else "Dire"