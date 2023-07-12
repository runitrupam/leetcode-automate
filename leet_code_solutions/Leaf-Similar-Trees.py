# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_recur(self, root: Optional[TreeNode]): # this can also be used 
            if not root.left and not root.right:
                yield root.val
            if root.left:
                yield from self.inorder_recur(root.left)
            if root.right:
                yield from self.inorder_recur(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        
        def inorder(root):
            if root is None:
                yield None
            s = list()
            s.append(root)
            while (s):
                root = s.pop()
                if root.left is None and root.right is None:
                    yield root.val
                
                if root.right:
                    s.append(root.right)
                if root.left:
                    s.append(root.left)
        # item1 = inorder(root1)
        # item2 = inorder(root2)
        item1 = self.inorder_recur(root1)
        item2 = self.inorder_recur(root2)
        # print(item1) # will return object , also item1[0] , 'generator' object is not subscriptable
        for a,b in zip_longest(item1,item2,fillvalue=object()):
            # print(a,b)
            if a!=b :
                return False
        return True

        
        # for i in inorder(root1): # this works
        #     print(i)
        