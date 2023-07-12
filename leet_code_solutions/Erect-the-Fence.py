class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        '''
        
                This solution employs Andrew's monotone chain convex hull algorithm. Time complexity is log-linear: O(N*logN). Space complexity is linear: O(N).

        Comment. What's being asked in the problem (in mathematical terms) is basically constructing a convex hull (but I'll keep calling it a fence). The list of key idea here is the following:

        First, locate a starting tree, namely, the one that definitely belongs to the fence. To do that, we x-sort the points and take the leftmost one (i.e., with the minimal x). This will be the beginning of the fence.
        But now we have a problem, namely, that there are points that lie either below or above that starting tree. Thus, we'll be constructing two fences, upper and lower, then join them.
        To construct an upper fence, we iterate through the x-ordered list of points and check whether the addition of each new point will make us a left (counterclockwise) or a right (clockwise) turn with respect to the direction specified by the last 2 trees in the fence.
        This data is enconded in the angle between two vectors (AB and AC) formed by the two last points (A and B) and the candidate point C. We call this angle positive (negative, zero) if AC lies to the right of (lies to the left of, is collinear to) AB. This angle (to be more precise, it's sine) can be extracted from the cross product of vectors AB and AC, namely, from AB x AC = |AB| * |AC| * sin(AB,AC). Sine function has the same sign as the angle, thus using the sign of cross product is our way to detect the change in direction. (It is known from geometry that cross product can be computed from the coordinates of the vectors, see code.)
        ...
        Python. Note that we can use numpy here for cross product, but for some reason it's slow and gives TLE.


        
        
        '''
        # don't solve no one will ask this .
        trees = sorted(trees)                                 # [1] make an x-ordered list of points
        #trees = [np.array(t) for t in sorted(trees)]         #     (for a numpy solution, use this)
        U, L = [], []
        
        def cross(A, B, C):                                   # [2] this function computes cross product
            x1, y1, x2, y2, x3, y3 = chain(A, B, C)           #     between vectors A-C and C-B
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
            #return np.cross(A-C,C-B)                         #     (for a numpy solution, use this)
                
        for t in trees:                                       # [3] according to Andrew's algorithm,
            while len(U) >= 2 and cross(t,U[-1],U[-2]) < 0:   #     we add points to upper (lower)
                U.pop()                                       #     convex hulls if they make a
            U.append(t)                                       #     counterclockwise (clockwise) turn
                                                              #     with respect to the last two 
            while len(L) >= 2 and cross(t,L[-1],L[-2]) > 0:   #     points in the convex hull
                L.pop()                                       
            L.append(t)

        return set(tuple(T) for T in (U+L))    