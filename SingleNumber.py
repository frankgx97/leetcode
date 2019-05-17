class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            if i in hashtable.keys():
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        for i in hashtable.keys():
            if hashtable[i] == 1:
                return i
