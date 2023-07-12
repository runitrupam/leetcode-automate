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
 * @return {TreeNode[]}
 */
var findDuplicateSubtrees = function(root) {
    const map = new Map();
    const result = [];

    function traverse(node){

        if (!node) return '#';

        const l = traverse(node.left)
        const r = traverse(node.right)

        const sub_tree_key = `${node.val},${l},${r}`; // note here , is necessary as left val = 1 , right val = 1 will create issue in keys
        console.log(sub_tree_key , l ,r )
        
        const count = map.get(sub_tree_key   ) || 0
        if (count === 1){
            result.push(node)
        }
        map.set(sub_tree_key, count + 1) ;

        return sub_tree_key ; 
    }
    traverse(root)
    return result
};








/*
# Python SOLUTION
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        sub_tree_dict = {}
        sub_tree_id_dict = {}
        # sub_tree_id_list = []

        def traverse(node):
            
            if node is None:
                return None

            l = traverse(node.left) # will return. some int. or None
            r = traverse(node.right)
            key = (node.val,l,r)
            if sub_tree_dict.get(key):
                sub_tree_dict[key] += 1
                if sub_tree_dict[key] == 2:
                    res.append(node)
            else:
                sub_tree_dict[key] = 1
            
            if sub_tree_id_dict.get(key) is None:
                sub_tree_id_dict[key] = len(sub_tree_id_dict.keys())

            return sub_tree_id_dict[key]
        traverse(root)
        # print( 'sub_tree_id_dict := ',sub_tree_id_dict  )
        # print( 'sub_tree_dict := ',sub_tree_dict  )

        return res

'''
class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    ans = []
    count = collections.Counter()

    def encode(root: Optional[TreeNode]) -> str:
      if not root:
        return ''

      encoded = str(root.val) + '#' + \
          encode(root.left) + '#' + \
          encode(root.right)
      count[encoded] += 1
      if count[encoded] == 2:
        ans.append(root)
      return encoded

    encode(root)
    return ans



'''



*/

