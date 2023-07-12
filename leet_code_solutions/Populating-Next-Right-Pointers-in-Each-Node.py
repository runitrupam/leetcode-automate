"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    global c_goodNodes
    def c_goodNodes(root,level):
        #print(level , root.val)
        global level_nodes
        
        if len(level_nodes) < level :
            level_nodes.append([root])
        else:
            level_nodes[level-1].append(root)
        #print(level_nodes,level,root.val)  
        if root.left != None :
            c_goodNodes(root.left,(level + 1)  ) 
        if root.right != None :
            c_goodNodes(root.right,(level + 1)    )    
        
            
    def connect(self, root: 'Node') -> 'Node':
        global level_nodes 
        level_nodes = []
        if root == None : 
            return root
        c_goodNodes(root,1)
        for i in range(len(level_nodes)):
            for j in range(len(level_nodes[i])):
                #print(i,level_nodes[i][j].val)
                if j != len(level_nodes[i]) - 1:
                    level_nodes[i][j].next = level_nodes[i][j+1]
                else:
                    level_nodes[i][j].next = None
        return root        
    '''
    global c_goodNodes  # or use self(has same instance or memory as the object of class)
    def c_goodNodes(root,parent,grandparent):
        if root.left != None:
            root.left.next = root.right
        if root.right != None:
            if parent.left == root :
                root.next = None
        if root == grandparent :
            if root.right != None :
                c_goodNodes(root.right,root)        
            if root.left != None :
                c_goodNodes(root.left,root)
        
        if level == 0:
            root.next = None
        count = 1
        while level != count:
            if count %2 != 0:
                right_so_far = right_so_far.right
            else:
                right_so_far = right_so_far.left

            count +=1
            
        #print(root.val , min_so_far)
        if root.val != None and root.next!= None:
            if root != parent.right:
                root.next = parent.right
            if root != parent.left:
                root.next = parent.left 
                
        if root.right != None :
            c_goodNodes(root.right,root)        
        if root.left != None :
            c_goodNodes(root.left,root)
        
                
            
        
    def connect(self, root: 'Node') -> 'Node':
        
        global head
        head = root
        count = 0
        if root == None:
            return root
        root.next = None
        if root.left != None:
            root.left.next = root.right
        if root.right != None:
            root.next = None
        grandparent = root  
        parent = root
        c_goodNodes(root.left,parent,grandparent)
        c_goodNodes(root.right,parent,grandparent)

        return count'''