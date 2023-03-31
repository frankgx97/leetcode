class Trie:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        curr = self.trie
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]    
        curr['*'] = '*'
        
    def search(self, word: str) -> bool:
        curr = self.trie
        for i in word:
            if i not in curr:
                return False
            else:
                curr = curr[i]
        return '*' in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for i in prefix:
            if i not in curr:
                return False
            else:
                curr = curr[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
