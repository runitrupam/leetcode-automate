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

// TC = O(height of tree) recursion approach
let isSymmetric_temp = function(root) {
    if(root === null) return true
    function issymm(left , right){
        if ((left === null) && (right === null)) return true
        if ((left === null) && (right !== null)) return false
        if ((left !== null) && (right === null)) return false
        if (left.val !== right.val ) return false
        return (issymm(left.left,right.right) && issymm(left.right,right.left)) ? true : false
    }
    return issymm(root.left,root.right);

};


let isSymmetric = function(root) {
    if(root === null) return true
    var queue = []
    queue.push([root.left,root.right])

    while (queue.length > 0) 
    {
        const [left,right] = queue.pop()
        // console.log( left,right  )
        if ((left === null) && (right === null)) 
            continue
        if ((left === null) && (right !== null)) return false
        if ((left !== null) && (right === null)) return false
        if (left.val !== right.val ) 
            return false
        queue.push(  [left.left,right.right]   )
        queue.push(  [left.right,right.left]   )

    }
    return true

};