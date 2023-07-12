# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count = 0
        dq = deque()
        res = []
        if root:
            # count += 1
            dq.append(root)
            # res.append([root.val])
        while(dq):
            curr_list = []
            for i in range(len(dq)):
                curr = dq.popleft()
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

                curr_list.append(curr.val)
            # print(curr_list)
            if count %2 != 0 :
                curr_list.reverse()
            res.append(curr_list)
            count += 1

        # print(dq)
        return res