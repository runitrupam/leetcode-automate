class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        def sub_com(vt , target , n):
            st=[[]]
            a=[[]]
            b=[[]]
            if (sum(vt) < target):
                return [[]]
            elif (sum(vt) == target):
                return [vt]
            if (target == 0):
                return a[:]
            #print(vt)
            for i in range(1,n+1,1):
                #print(i)
                #print(vt[n-i])
                if ((vt[n-i] <= target) and( vt[n-i] != 0)) :
                    x=vt[n-i]
                    #print(x)
                    vt[n-i] = 0
                    a=sub_com(vt[:],target-x,n)


                    for j in range(len(a)):
                        a[j].append(x)
                    #print(a)    



                    t=[]
                    t.append(x)
                    if (len(a)==0):
                        a.append(t)
                    #print('a array',a)    
                    #if (target == x ) :
                      #  print("insert in st , t = x ")
                    for m in a :
                        st.append(m)
                    b = sub_com(vt[:],target,n)
                    target = target - x
                    #print ('target =',target)
                    #print('b array ',b)
                    for m in b :
                        st.append(m)
                    for xcv in a:
                        if sum(xcv) == sum_tar :
                            sty.append(xcv)   
                    for xcv in b:
                        if sum(xcv) == sum_tar :
                            sty.append(xcv)     
                if vt[n-i] > target:
                     vt[n-i]=0 

                for xcv in st:
                    if sum(xcv) == sum_tar :
                        sty.append(xcv)
            st.sort()            
            return list(st for st,_ in itertools.groupby(st))
        
        
        
        
        
        import itertools
        xt=candidates[:]

        xt.sort(reverse=False)
        sum_tar = target
        sty=[[]]
        if (sum(xt) < target):
            return []
        elif (sum(xt) == target):
            return [xt]
        vta=sub_com(xt[:] , target , len(xt))

        x = [1, 2, 3, 2, 2, 2, 3, 4]
        for i in range(len(sty)):
            sty[i] = list(filter(lambda a: a != 0, sty[i]))
        sty.sort()
        sty=list(sty for sty,_ in itertools.groupby(sty))

        #print (vta,'\n knnlj')
        #print(sty)
      
        
        return sty[1:]