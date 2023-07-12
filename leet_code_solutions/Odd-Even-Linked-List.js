/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var oddEvenList = function(head) {
    if(!head) return head
    odd = head , even = head.next
    e_head = even
    while(even && even.next)
        {
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next  
        }
    odd.next = e_head
    return head
    
    
    /*
    if(!head) return head
    let count = 1
    odd = null
    even = null
    e_head = null
    o_head = null
    tp = head
    while(tp)
        {
            if (count%2 === 0)
                {  
                    // console.log(count,even)
                    if(even) {
                        even.next = tp 
                        even = even.next}
                    else {
                        even = tp , e_head = even}
                }
            else
                {
                    // console.log(count,odd)

                    if(odd) odd.next = tp , odd = odd.next
                    else {
                        odd = tp, o_head = odd}
                }
            
            count = count + 1
            tp = tp.next
        }
    // console.log(count,even)
    // console.log(count,odd)

    odd.next = e_head
    if (even) even.next = null
    return o_head
    */
};