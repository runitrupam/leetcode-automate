# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        
        cnt = 0
        hm = defaultdict(int)
        hm[0] += 1
        #curr_sum is treated as a prefix sum
        def recu(node,curr_sum):
            
            nonlocal cnt
            if node is None:
                return 
            curr_sum += node.val
            # print( node.val , curr_sum , hm  )

            # print(hm[ curr_sum - target  ])
            cnt += hm[  curr_sum - target ] # if prefix sum from head - target , is in map , add the count
            hm[curr_sum] += 1
            recu(node.left,curr_sum)
            recu(node.right,curr_sum)
            hm[curr_sum] -= 1 # imp as , i don't want nodes of left tree to be matched with the right tree .

        recu(root,0)
        return cnt
        
        '''
        5% faster
        self.count = 0
        def dfs(root,curr_sum):
            if root is None:
                return 
            curr_sum += root.val
            
            if curr_sum  == target :
                self.count += 1
            
            dfs(root.right,curr_sum)
            dfs(root.left,curr_sum)
        
        dq = deque()
        dq.append(root)
        # bfs
        while(dq):
            curr_node = dq.popleft()
            dfs(curr_node , 0)
            if curr_node:
                dq.append(curr_node.left)
                dq.append(curr_node.right)
        return self.count
        '''            