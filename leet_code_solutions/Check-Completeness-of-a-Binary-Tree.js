/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

/*
push -> O(1)

pop -> O(1)

shift -> O(N)

slice -> O(N)

splice -> O(N)

TC = O(N)
*/
var isCompleteTree = function(root) {
    var index = 0
    var q = []
    q.push(root)
    null_flag = false
    // console.log(q , q.length , index)
    while(  index < q.length  ){
        node = q[index]
        if (node == null) {
            null_flag = true
            index += 1
            continue
        }
        if (null_flag == true && node !== null ) 
            return false
        q.push(node.left)
        q.push(node.right)
        index += 1
        // console.log(q , q.length , index,null_flag)

    }
    return true

};