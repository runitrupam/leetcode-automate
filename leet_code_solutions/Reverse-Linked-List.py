# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st = head
        t = head
        old = None
        
        while(t):
            nxt = t.next
            t.next = old
            old = t
            t = nxt
            
        return old
          
        