# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        min_val = 10**6
        A = []
        def dfs(root):       
            nonlocal A  
            if root :
                dfs(root.left)
                A.append(root.val)
                dfs(root.right)
            
        dfs(root)
        print(A)
        # A.sort()
        for i in range(len(A)-1):
            if abs(A[i] - A[i+1]) < min_val:
                min_val =  abs(A[i] - A[i+1])
        return min_val
'''

'''
If you look closely at approach 1, we only use the previous value in the sorted list. This suggests that we don't need to store the entire list, just the previous value!
'''
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = float("-inf")

        def dfs(node):
            nonlocal prev
            if not node:
                return float("inf")
            min_diff = dfs(node.left) # go in sorted in order traversal .
            min_diff = min(min_diff, node.val - prev)
            prev = node.val
            min_diff = min(min_diff, dfs(node.right))
            return min_diff

        return dfs(root)