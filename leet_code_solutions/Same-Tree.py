# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        ps = []
        qs = []

        ps.append(p)
        qs.append(q)
        while(ps and qs):
            p_temp = ps.pop()
            q_temp = qs.pop()

            if p_temp is None and q_temp is None:
                # return True
                continue
            elif p_temp is None or q_temp is None:
                return False

            elif p_temp.left is None and q_temp.left:
                return False
            elif p_temp.left  and q_temp.left is None:
                return False
            elif p_temp.right is None and q_temp.right:
                return False
            elif p_temp.right and q_temp.right is None:
                return False

            elif p_temp.val != q_temp.val:
                return False
            
            ps.append(p_temp.right)
            ps.append(p_temp.left)
            
            qs.append(q_temp.right)
            qs.append(q_temp.left)
        if ps or qs:
            return False
        return True


        '''
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        '''