# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        h1 = list1
        h2 = list2
        h3 = ListNode()
        t3 = h3
        while (h1 and h2):
            if h1.val < h2.val:
                t3.next = ListNode(h1.val)
                t3 = t3.next
                h1 = h1.next
            else:
                t3.next = ListNode(h2.val)
                t3 = t3.next
                h2 = h2.next
        while (h1):
            t3.next = ListNode(h1.val)
            t3 = t3.next
            h1 = h1.next
        while (h2):
            t3.next = ListNode(h2.val)
            t3 = t3.next
            h2 = h2.next
        
        return h3.next