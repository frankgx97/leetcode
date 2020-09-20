class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        window = 1
        left = 0
        ans = 0
        for right in range(len(nums)):
            window *= nums[right]
            while left <= right and window >= k:
                window = window//nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
