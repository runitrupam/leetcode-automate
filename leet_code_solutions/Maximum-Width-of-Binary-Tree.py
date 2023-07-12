# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_length = len(queue)
            _, level_start = queue[0]
            
            for i in range(level_length):
                node, index = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2*index))
                
                if node.right:
                    queue.append((node.right, 2*index+1))
                    
            max_width = max(max_width, index - level_start + 1)
            
        return max_width

'''
TLE
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = deque()
        q.append(root)
        max_width = 1
        while(q):

            # print(q)                
            n = len(q)

            #width check
            last_node_pos = -1
            for j in range(n-1 , -1 , -1):
                if q[j] :
                    last_node_pos = j
                    break
            if last_node_pos == -1:
                break
            first_node_found = False
            for i in range(n):
                node = q.popleft()
                if i > last_node_pos :
                    break
                if node is None and first_node_found :
                    q.append(None)
                    q.append(None)
                elif node is not None :
                    first_node_found = True
                    max_width = max( max_width , last_node_pos - i + 1)
                    q.append(node.left)
                    q.append(node.right)
        return max_width
'''            