class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        compare each char in string - ac
        time: O(n)
        '''
        def compare(a,b):
            for i in range(min(len(a),len(b))):
                if order.index(a[i]) > order.index(b[i]):
                    return False
                elif order.index(a[i]) < order.index(b[i]):
                    return True
            if len(a) > len(b):
                return False
            else:
                return True
        for i in range(1,len(words)):
            if not compare(words[i-1],words[i]):
                return False
        return True
