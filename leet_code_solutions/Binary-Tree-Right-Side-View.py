# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def recu(root , h):
            if root is None:
                return
            if len(res) < h + 1:
                res.append(root.val)
            res[h] = root.val
            recu(root.left,h+1)
            recu(root.right,h+1)
        recu(root,0)
        return res