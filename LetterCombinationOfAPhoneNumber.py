class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        for i in range(0, len(digits)):
            size = len(result)
            for k in range(0,size):             #迭代result
                for j in digitmap[digits[i]]:   #迭代字母表
                    result.append(result[k] + j)
            result = result[size:]
            if i == 0 :                         #如果是第一轮迭代
                for j in digitmap[digits[i]]:
                    result.append(j)
        return result
