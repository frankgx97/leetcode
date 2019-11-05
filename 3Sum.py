class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sorting and two pointers - ac
        sort the list
        iterate through the list to select the first item, then select the other two items from both sides into the center of the list.
        some points should be noticed:
        - in each iteration, left starts at i+1, to avoid duplicates
        - when a solution found, skip the numbers that are the same with the numbers that current pointer is pointing to.
        - avoid situations that i == left or i == right or left == right
        - we can break the loop after nums[i] become positive(there'll be no solution when all candidates are positive.)
        '''
        nums.sort()
        r = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            left = i+1
            right = len(nums)-1
            while left < right:
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                if left >= right:
                    break
                if nums[i] + nums[left] + nums[right] == 0:
                    curr = [nums[i], nums[left], nums[right]]
                    r.append(curr)
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
        return r
