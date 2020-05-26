class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        prfix sum & hash map
        if current 0, minus 1,
        if current 1, add 1
        use hashmap to store prefix sum and its index {value:index}
        ref: https://zxi.mytechroad.com/blog/hashtable/leetcode-525-contiguous-array/
        time: O(n)
        space: O(n)
        
        '''
        p = {0:-1}
        curr = 0
        mx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr -= 1
            else:
                curr += 1
            if curr not in p:
                p[curr] = i
            mx = max(mx, i-p[curr])
        return mx
