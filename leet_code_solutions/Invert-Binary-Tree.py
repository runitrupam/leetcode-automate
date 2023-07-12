# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def recu(node):
            if node is None:
                return None
            temp = node.left
            node.left = recu(node.right)
            node.right = recu(temp)
            return node
        return recu(root)