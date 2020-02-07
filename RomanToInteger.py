class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        mapping - ac
        create a dict to map roman to integer
        traverse the roman, add up each item
        if one is larger than the previous one, minus double of the previous one.
        '''
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            res += map[s[i]]
            if i > 0 and map[s[i-1]] < map[s[i]]:
                res -= map[s[i-1]]*2
        return res
