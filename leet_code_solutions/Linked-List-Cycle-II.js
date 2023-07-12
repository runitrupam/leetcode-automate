/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */

/*
TC = O(N) 
SC = O(N)

var detectCycle = function(head) {
    const nodemap = new Set();
    var temp = head;
    while(temp){
        if( nodemap.has(temp)      )
        {
            return temp
        }
        else
        {    
            nodemap.add(temp); 
        }
        temp = temp.next
        // nodemap.forEach (function(nd) {
        //         console.log(nd) ;
        //     })
        // console.log(nodemap)
    }
    return null
};
*/


// SC = O(1)
var detectCycle = function(head) {
    if(head === null || head.next === null)
        return null;
    let slow = head;
    let fast = head;

    while(fast && fast.next )
    {
        
        slow = slow.next
        fast = fast.next.next
        if (slow === fast) 
            break
    } 
    if (slow !== fast) 
        return null

    slow = head
    while( slow !== fast  )
    {
        slow = slow.next
        fast = fast.next 
    }
    return slow
};