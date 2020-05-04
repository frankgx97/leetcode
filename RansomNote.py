class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = dict(collections.Counter(magazine))
        for i in ransomNote:
            if i not in freq or freq[i] == 0:
                return False
            else:
                freq[i] -= 1
        return True
