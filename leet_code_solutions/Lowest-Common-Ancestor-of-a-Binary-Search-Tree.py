
class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        while(node):
            
            if node == p or node == q :
                return node
            if node.val < p.val and node.val < q.val:
                node = node.right
            elif node.val > p.val and node.val > q.val:
                node = node.left
            else:
                return node
        return root
            
        
        