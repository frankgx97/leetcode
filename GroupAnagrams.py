class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortstr(input):
            return ''.join(sorted(input))
        d = dict()
        for i in strs:
            if sortstr(i) in d.keys():
                d[sortstr(i)].append(i)
            else:
                d[sortstr(i)] = [i]
        result = []
        for i in d.keys():
            result.append(d[i])
        return result
