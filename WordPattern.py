class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        '''
        dict - ac
        encode a list of string with char from 'a'
        ex: "dog cat cat dog" -> "abba"
        use a dict to store the map from string to encoded char
        '''
        def get_pattern(s):
            currletter = 'a'
            str_pattern = ''
            dic = {}
            for i in s:
                if i not in dic:
                    dic[i] = currletter
                    str_pattern += currletter
                    currletter = chr(ord(currletter)+1)
                else:
                    str_pattern += dic[i]
            return str_pattern
        
        str = str.split(' ')
        if get_pattern(str) == get_pattern(list(pattern)):
            return True
        else:
            return False
