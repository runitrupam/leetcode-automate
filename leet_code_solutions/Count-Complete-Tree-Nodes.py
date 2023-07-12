# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        head = root
        def recu(head):
            
            if head :
                # print(head)
                self.count +=1
                recu(head.left)
                recu(head.right)
        recu(head)
        return self.count
            
            