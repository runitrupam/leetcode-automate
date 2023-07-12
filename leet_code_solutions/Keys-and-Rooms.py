class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        seen = set()
        st = list()
        seen.add(0)
        for j in rooms[0]:
            seen.add(j)
            st.append(j)
        
        while(st):
            ro = st.pop()
            for new_room in rooms[ro]:
                if new_room not in seen:
                    st.append(new_room)
                    seen.add(new_room)
            # print(st,rooms[ro])
        if len(seen) == len(rooms):
            return True
        return False