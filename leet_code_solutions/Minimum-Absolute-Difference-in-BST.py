
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Initialize variables for previous value and minimum difference
        prev = float('-inf')  # Initialize prev to negative infinity
        min_diff = float('inf')  # Initialize min_diff to positive infinity
        
        def inorderTraversal(root):
            nonlocal prev, min_diff
            if not root:
                return
            
            # In-order traversal: visit the left subtree
            if root.left:
                inorderTraversal(root.left)
            
            # Compare the current node's value with the previous value
            if (root.val - prev) < min_diff:
                min_diff = root.val - prev
            
            # Update the previous value to the current node's value
            prev = root.val
            
            # In-order traversal: visit the right subtree
            if root.right:
                inorderTraversal(root.right)
                
        # Start the in-order traversal from the root of the binary tree
        inorderTraversal(root)
        
        # Return the minimum difference between any two nodes in the tree
        return min_diff