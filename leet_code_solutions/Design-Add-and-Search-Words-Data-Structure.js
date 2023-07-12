/*

 * *Time: O(M) - well defined words, words wihtout ...
 * *Time: O(N x 26^M) - N = number of keys and 26^M for undefined words
 * *Space: O(1) - well defined words
 * *Space: O(M) - undefined words
 */

class WordDictionary {
  constructor() {
    this.root = {};
  }

  addWord(word) {
    let node = this.root;

    for (const char of word) {
      if (!node[char]) node[char] = {};

      node = node[char];
    }

    node.isEnd = true;
  }

  search(word) {
    const traverse = (node, i) => {
      const char = word[i];

      // reached end of word, check if word exists
      if (i === word.length) return node.isEnd || false;

      // if wildcard, iterate every possible keys and check if word exists
      // if valid char exist, recursively check if other characters of the word exist
      // else return false
      if (char == '.') {
        for (const key in node) {
          if (traverse(node[key], i + 1)) return true;
        }
      } else if (node[char]) return traverse(node[char], i + 1);

      return false;
    };

    return traverse(this.root, 0);
  }
}