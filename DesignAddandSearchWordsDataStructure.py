class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        #if self.search(word):
        #    return
        curr = self.trie
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr['*'] = ''
        return

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word, curr_trie):
            if word == '' and '*' in curr_trie:
                return True
            if word == '' and '*' not in curr_trie:
                return False
            if word[0] != '.':
                if word[0] not in curr_trie:
                    return False
                return dfs(word[1:], curr_trie[word[0]])
            else:
                for k in curr_trie:
                    if dfs(word[1:], curr_trie[k]):
                        return True
                return False
        return dfs(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
