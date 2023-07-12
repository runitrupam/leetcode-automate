# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, A: List[int]) -> Optional[TreeNode]:

        def recu(A,i,j):
            if i < 0 or j >= len(A) or i > j:
                return None
            mid = (i+j)//2 
            head = TreeNode(A[  mid  ])
            head.left = recu(A,  i , mid - 1   )
            head.right = recu(A, mid + 1 , j  )
            return head
        return recu(A,0,len(A)-1)