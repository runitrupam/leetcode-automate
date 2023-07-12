# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def rec(node,h):
            
            if node is None:
                return h,1
            
            left,f1 = rec(node.left,h+1) 
            right,f2 = rec(node.right,h+1)
            if f1 == 0 or f2 == 0:
                return h,0
            if abs(left - right) > 1:
                return h,0
            return max(left,right),1
        h,res = rec(root,0)
        return res