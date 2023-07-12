/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
    if (inorder.length == 0 || postorder.length == 0) {
        return null;
    }
    var rootVal = postorder[postorder.length - 1];
    var root = new TreeNode(rootVal);
    var rootIndex = inorder.indexOf(rootVal);
    var leftInorder = inorder.slice(0, rootIndex);
    var rightInorder = inorder.slice(rootIndex + 1);
    var leftPostorder = postorder.slice(0, leftInorder.length);
    var rightPostorder = postorder.slice(leftInorder.length, postorder.length - 1);
    root.left = buildTree(leftInorder, leftPostorder);
    root.right = buildTree(rightInorder, rightPostorder);
    return root;
};