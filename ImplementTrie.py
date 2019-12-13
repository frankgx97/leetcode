class TrieNode:
    def __init__(self,v):
        self.v = v
        self.is_end = 0
        self.nodes = [None]*26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for i in range(len(word)):
            if current.nodes[ord(word[i]) - ord('a')] == None:
                new_node = TrieNode(word[i])
                current.nodes[ord(word[i]) - ord('a')] = new_node
                current = new_node
            else:
                current = current.nodes[ord(word[i]) - ord('a')]
                continue
        current.is_end = 1
        return
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for i in range(len(word)):
            if current.nodes[ord(word[i]) - ord('a')] == None:
                return False
            else:
                current = current.nodes[ord(word[i]) - ord('a')]
        if current.is_end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for i in range(len(prefix)):
            if current.nodes[ord(prefix[i]) - ord('a')] == None:
                return False
            else:
                current = current.nodes[ord(prefix[i]) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

[1,2,3,4,4]
