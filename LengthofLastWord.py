class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split(' ')
        while '' in sp:
            sp.remove('')
        if sp == []:
            return 0
        return len(sp[-1])
