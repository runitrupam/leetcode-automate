# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = 0

        def inorder(head):
            nonlocal res
            # print(res)
            if head is None :
                return
            if low <= head.val <= high:
                res += head.val
            if head.val <= low:
                inorder(head.right)
            elif head.val >= high:
                inorder(head.left)
            else:
                inorder(head.left)
                inorder(head.right)
        inorder(root)
        return res

            