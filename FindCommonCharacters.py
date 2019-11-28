class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        '''
        dictionary - ac
        init the dictionary with the first string in the list
        store each char(key) and freq(value) of the string in the dictionary
        iterate the rest of the list
        stat the each char(key) and freq(value) of the string in a temp dictionary
        compare with dic and temp dic,
        - if some key do not exist in tempdic, remove it from dic,
        - if some key exist in both dic, but have differnet freq, set dic[key] to the smaller value
        use key*freq to build the result
        '''
        if not A:
            return []
        dic = {}
        for i in A[0]:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for i in range(1,len(A)):
            tempdic = {}
            for j in A[i]:
                if j not in tempdic:
                    tempdic[j] = 1
                else:
                    tempdic[j] += 1
            rm = []
            for j in dic:
                if j not in tempdic:
                    # caution: removing keys during iteration is not allowed
                    rm.append(j)
                else:
                    dic[j] = min(tempdic[j],dic[j])
            for j in rm:
                dic.pop(j)
        
        r = []
        for i in dic:
            r += [i]*dic[i]
        
        return r
