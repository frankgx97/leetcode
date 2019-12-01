class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        use index to access the array - ac
        each time check if arr[index+1] is equal to arr[index]
        if yes, remove item of index+1,
        else index++
        
        O(n) time and constant space
        '''
        p=0
        while p < len(nums):
            if p + 1 < len(nums):
                if nums[p+1] == nums[p]:
                    nums.pop(p+1)
                else:
                    p += 1
            else:
                break
        return len(nums)
        
        '''
        O(n) time and space solution
        '''
        dup = []
        for i in nums[:]:
            if i not in dup:
                dup.append(i)
            else:
                nums.remove(i)
        return len(nums)
