# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def divide(self,head):
        s = head
        f = head.next
        while(f and f.next):
            s = s.next
            f = f.next.next
        return s

    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
            
        nums.sort()                                # sorting use O(nlogn) time complexity
        curr = head
        for i in nums:
            curr.val = i
            curr = curr.next
            
        return head