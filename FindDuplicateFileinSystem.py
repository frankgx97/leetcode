class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        ans = []
        for i in paths:
            i = i.split(' ')
            path = i[0]
            for j in i:
                if j == path:
                    continue
                name_content = j.replace('(',')')
                name_content = name_content.split(')')
                fname = name_content[0]
                content = name_content[1]
                pathname = path+'/'+fname
                if content not in dic.keys():
                    dic[content] = [pathname]
                else:
                    dic[content].append(pathname)
        for i in dic.keys():
            if len(dic[i]) > 1:
                ans.append(dic[i])
        return ans
