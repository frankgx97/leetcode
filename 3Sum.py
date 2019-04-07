class Solution:
    def cmp(self,l,s):
        for j in s:
            if set(l) - set(j) == set():
                return False
        return True
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                diff = 0 - (nums[i] + nums[j])
                if diff in nums:
                    for p in [i for i, e in enumerate(nums) if e == diff]:
                        if not (p == i or p == j):
                            solutions.append([nums[i],nums[j],diff])
        finalsolutions = []
        for i in solutions:
            if self.cmp(i,finalsolutions):
                i.sort()
                finalsolutions.append(i)
        return finalsolutions
