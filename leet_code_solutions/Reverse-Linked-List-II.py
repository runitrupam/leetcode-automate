# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            t = head
            count = 1
            if left == right :
                return head
            while(t):
                if count == left:
                    left = t
                if count == right:
                    right = t
                count+=1
                t = t.next
            
        
            def reverseList(head):
                st = head
                t = head
                old = None

                while(t):
                    # nxt = t.next
                    # t.next.next = t
                    # print(t.val)
                    nxt = t.next

                    t.next = old
                    old = t
                    t = nxt

                return old
            old_right_nxt = right.next
            right.next = None
            old_left = left
            op = reverseList(left)
            
            old_left.next = old_right_nxt
            t = head
            while(t):
                if t.next == old_left:
                    t.next = op
                    break
                t = t.next
            if old_left == head :
                return op
            return head
            