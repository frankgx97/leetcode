class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
        two pointers
        - For each index "i" in sorted_nums, find maximum "j" such that sorted_nums[i] + sorted_nums[j] <= target and j >= i.
        - From i+1 to j, we can either pick or leave each element.
        - Therefore, res += 2**(j-i)
        '''
        mod = 10 ** 9 + 7
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += 2 ** (right - left)
                left += 1
        return ans % mod
