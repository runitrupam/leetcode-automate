var Trie = function() {
    this.root = {}
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    var node = this.root
    // console.log(node)
    for(const w of word ){
        // if (!node.has(w)){
        if (!(w in node)){
            node[w] = {}
        }
        node = node[w]
    }
    node['#'] = '#'
    // console.log(node)
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    var node = this.root
    for(const w of word ){
        if (!(w in node)){
            return false
        }
        node = node[w]
    }
    if (!('#' in node)){
            return false
        }
    return true
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    var node = this.root
    for(const w of prefix ){
        if (!(w in node)){
            return false
        }
        node = node[w]
    }
    return true
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */