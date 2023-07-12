# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [] 
        # print(root.val)

        # x = self.preorderTraversal(root.left) if root.left else []
        # print(x)
        return ([root.val] + ( self.preorderTraversal(root.left) if root.left else [] )+( self.preorderTraversal(root.right)  if root.right else []))