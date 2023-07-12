# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def max_depth(root):
            l , r = 0,0
            if root.left:
                l =  1 + max_depth(root.left)
            if root.right:
                r =  1 + max_depth(root.right)
            return max(l,r)
        return 1 + max_depth(root)