# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current_k = k
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if (len(stack) == 0):
                break
            node = stack.pop()
            current_k -= 1
            if current_k == 0:
                return node.val
            root = node.right
        return -1