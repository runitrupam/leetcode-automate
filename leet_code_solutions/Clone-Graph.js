/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;

    let newnode = new Node(node.val);
    let queue = [node]
    let visited = new Map()
    // visited[node.val] = newnode;
    visited.set( node.val, newnode)
    // console.log(  visited )
    // BFS Approach 
    while(  queue.length > 0  ){
        let currentNode = queue.shift()
        for (let neighbor of currentNode.neighbors) {
            if(!visited.has(neighbor.val)){
                let newNeighbour = new Node( neighbor.val  )
                // visited[neighbor.val] = newNeighbour;
                visited.set( neighbor.val, newNeighbour)

                queue.push(  neighbor )
            }
            visited.get(currentNode.val).neighbors.push(visited.get(neighbor.val));

        }
    }
    return newnode

};