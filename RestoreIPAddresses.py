class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def assemble(arr):
            r = ""
            for i in arr:
                r += (i+'.')
            return r[:-1]
        
        def dfs(candidate, path):
            if len(path) > 4:
                return
            if len(path) == 4 and candidate == '':
                a = assemble(path)
                if a not in result:
                    result.append(a)
                
            for i in range(1,4):
                if len(candidate) < i:
                    return
                if int(candidate[:i]) >=0 and int(candidate[:i]) <= 255:
                    if (int(candidate[:i])>0 and candidate[:i][0] == '0') or (int(candidate[:i])==0 and len(candidate[:i])>1):
                        return
                    dfs(candidate[i:], path+[candidate[:i]])
        result = []
        dfs(s, [])
        return result
