class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        hashtable - ac
        ref https://www.cnblogs.com/lightwindy/p/9546153.html
        '''
        dic = {0:1}
        ans = 0
        su = 0
        for i in range(len(nums)):
            su = su + nums[i]
            if su-k in dic:
                ans += dic[su-k]
            if su not in dic:
                dic[su] = 1
            else:
                dic[su] += 1
        return ans
