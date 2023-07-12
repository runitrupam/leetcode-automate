# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    # TC = O(1) for next , has_next
    # SC = O(N all nodes)
    def __init__(self, root: Optional[TreeNode]):
        
        self.nodes = []
        
        self.index = -1
        
        # call dfs in initialization
        self.dfs(root)

    def next(self) -> int:
        
        self.index += 1
        
        return self.nodes[self.index]
        
    def hasNext(self) -> bool:
        
        return self.index + 1 < len(self.nodes)
        
    
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        self.nodes.append(root.val)
        self.dfs(root.right)
        
''' 
    # TC = O(H)
    # SC = O(Height)


    def __init__(self, root: Optional[TreeNode]): # O(height) , space comp same 
        self.arr = []
        cur = root
        while(cur):
            self.arr.append(cur)
            cur = cur.left
        # print(self.arr)
        return None
    def next(self) -> int: # O(height of right tree)
        tp = self.arr.pop()
        cur = tp.right
        while(cur):
            self.arr.append(cur)
            cur = cur.left
        # print(self.arr)
        return tp.val
    def hasNext(self) -> bool: # O(1)
        # print('hasnext',self.arr)
        if len(self.arr) !=0 :
            return True
        else:
            return False
'''

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()