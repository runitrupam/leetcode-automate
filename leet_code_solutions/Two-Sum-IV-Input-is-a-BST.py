# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        dp = dict()
        def inorder(root , k):
            if root == None:
                return 
            inorder(root.left,k)          
            val = root.val
            
            if val not in dp:
                dp[val] = 1
            else:
                dp[val] += 1
            inorder(root.right,k)
        inorder(root,k)
        print(dp)
        for j in dp.keys():
            if j == k - j and dp[j] > 1 :
                return True
            elif j!= k-j and k-j in dp :
                return True
        return False