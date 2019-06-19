class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.result = False
        self.d([], s, wordDict)
        return self.result
    
    def d(self, queue, s, wd):
        if s == '' and queue == []:
            self.result = True
            return
        if s == '' and queue != []:
            if ''.join(queue) in wd:
                self.result = True
                return
            else:
                return

        for word in wd:
            if ''.join(queue) == word:
                self.d([],s, wd)
            else:
                self.d(queue+[s[0]], s[1:], wd)
