class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def split(s):
            sym = ['!','?',',',';','.',' ',"'"]
            arr = []
            substr = ''
            for i in s:
                if i not in sym:
                    substr += i
                else:
                    if len(substr)>0:
                        arr.append(substr.lower())
                        substr = ''
            arr.append(substr.lower())
            return arr
                
        paragraph = split(paragraph)
        dic = {}
        for i in paragraph:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        most = ''
        ma = 0
        for i in dic.keys():
            if dic[i] > ma and i not in banned:
                most = i
                ma = dic[i]
        return most
            
        
        
