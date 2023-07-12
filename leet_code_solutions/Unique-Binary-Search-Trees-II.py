# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left,right):
            if left > right:
                return [None]
            if left == right:
                return [TreeNode(left)]
            ans = []
            
            for root in range(left,right+1):
                leftNodes = dfs(left , root - 1)
                rightNodes = dfs(root + 1 , right)
                for l in leftNodes:
                    for r in rightNodes:
                        rootnode = TreeNode(root,l,r)
                        ans.append(rootnode)
            return ans
        return dfs(1, n)