# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_diam = 0
        
        def height(node):
            if node is None :
                return 0
            l =  height(node.left)
            r =  height(node.right) 
            self.max_diam = max(self.max_diam ,l+r)
            return max(l,r ) + 1
        
        height(root)
        return self.max_diam