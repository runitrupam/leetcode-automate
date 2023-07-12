"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        res = []
        
        def pre(root):
            
            if root is None:
                return
            res.append(root.val)
            for j in root.children:
                pre(j)
        pre(root)
        return res
        