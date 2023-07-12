class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:        
        stopBus = defaultdict(list)
        n = len(routes)
        
        for bus in range(n):
            for stop in routes[bus]: 
                stopBus[stop].append(bus)
        
        q = deque([(source, 0)])
        busTaken = set()
        
        while q:
            stop, buses = q.popleft()
            if stop == target: return buses
            
            for bus in stopBus[stop]:
                if bus not in busTaken:
                    busTaken.add(bus)
                    for route in routes[bus]:
                        q.append((route, buses + 1))
        
        return -1