class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        sets substract - ac
        '''
        n = len(nums)
        s = set()
        for i in range(0,n+1):
            s.add(i)
        return list(s - set(nums))[0]
