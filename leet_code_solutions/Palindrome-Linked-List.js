/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    
    s = head
    f = head
    
    // Get the middle
    while(f && f.next){
        f = f.next.next
        s = s.next
        
    }
    
    // Reverse the 2nd half
    p = s
    s = s.next
    p.next = null
    while(s)
        {
            temp = s.next
            s.next = p
            p = s
            s = temp        
        }
    
    s = p
    f = head
    // check for paln
    while( s && f)
        {
            if (s.val !== f.val) return false
            s = s.next
            f = f.next
        }
    
    return true
    
};