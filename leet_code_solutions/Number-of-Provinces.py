class Solution:
    def findCircleNum(self, G: List[List[int]]) -> int:

        n = len(G)
        seen = set()
        prov = 0
        for i in range(n):
            st = []
            if i not in seen:
                prov  += 1
                st.append(i)
                seen.add(i)
                while(st):
                    
                    g = st.pop()
                    for k in range(n):
                        if k not in seen and G[g][k] == 1 and g!=k:
                            st.append(k)
                            seen.add(k)
                    # print(g , st)
        return prov