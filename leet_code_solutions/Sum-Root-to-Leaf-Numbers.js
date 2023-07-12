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
 * @return {number}
 */
var sumNumbers = function(root) {
    
    function bfs(node,pref_sum){
        if(node == null) return 0
        pref_sum = pref_sum * 10 + node.val
        if (node.left == null  && node.right == null ){
            return pref_sum
        }

        return bfs(node.left,pref_sum) + bfs(node.right , pref_sum) 
    }
    return bfs(root,0)

};