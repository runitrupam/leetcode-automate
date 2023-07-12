/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.head = head
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    var result = null
    var count = 1
    var head = this.head
    while(head)
    {   
        // gives a number b/w 1 and count inclusive
        if(Math.floor((Math.random() * count) + 1) == count){
            result = head.val
        }
        count += 1
        head = head.next
    }
    return result;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */