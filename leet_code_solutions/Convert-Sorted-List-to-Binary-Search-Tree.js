/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {

    function recur(head){
        if(head === null) return null
        if(head.next === null) return new TreeNode(val= head.val)

        var count = 0
        var temp = head
        while(temp)
        {
            count += 1
            temp = temp.next
        }

        count = Math.floor(count / 2)

        var i = 0
        temp = head
        while(i !== count-1){
            temp = temp.next
            i+=1
        }
        // console.log(head,count , temp)

        var root =new TreeNode(temp.next.val , null ,null)
        // console.log(this)
        root.right = recur(temp.next.next)
        temp.next = null
        root.left = recur(head)
        return root
    }

    return recur(head)

};