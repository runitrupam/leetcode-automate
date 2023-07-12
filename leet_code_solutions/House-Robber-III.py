# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        
        def rec(root   ):
            if root == None:
                return 0, 0
            if root.left == None and root.right == None:
                return 0, root.val
            l_leaf_max_val_d2 , left_val  = rec(root.left)
            r_leaf_max_val_d2 , right_val = rec(root.right)
            
            return ( max(l_leaf_max_val_d2 , left_val )  + max(   r_leaf_max_val_d2 , right_val    )     ) , root.val + l_leaf_max_val_d2 + r_leaf_max_val_d2       
        
        d2_max_val , leaf_val = rec(root)
        return max( d2_max_val , leaf_val   )