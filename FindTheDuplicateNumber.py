class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = []
        for i in nums:
            if i not in hashmap:
                hashmap.append(i)
            else:
                return i
