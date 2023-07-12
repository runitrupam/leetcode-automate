class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
                
        
        def rec(node,left,right):
            
            if not node:
                
                return True
            
            
            if not (node.val < right and node.val > left):
                
                return False
            
            return rec(node.left,left,node.val) and rec(node.right,node.val,right)
        
        
        return rec(root,float("-inf"),float("inf"))