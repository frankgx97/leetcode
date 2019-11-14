class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        binary search - ac
        use two binary searches
        first bs find the index from which was rotated, aka pivot
            first calc the mid = (l+r)//2, if arr[mid] > arr[mid+1], means mid+1 is the pivot of the rotation
            otherwise compare arr[mid] with arr[left], if arr[mid] < arr[left], means the pivot is on the left part of the current mid,
            on the contrary, continue search on the right part.
            note that when arr[mid] == arr[left], we should always continue the search on the right part.
        now we have the index of the pivot. we can know which part(left or right) our target is in through a simple comparsion.
        then do a normal bs on that part.
        '''
        def find_index(nums, left,right):
            if len(nums) == 1:
                return 0
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                mid = (left + right) //2
                if nums[mid] > nums[mid+1]:
                    #is rotate pivot
                    return mid+1
                else:
                    if nums[mid] < nums[left]:
                        #continue on left
                        right = mid -1
                    else:
                        #continue on right
                        left = mid + 1

        def bs(nums,left,right,target):
            while left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1
        
        if not nums:
            return -1
        pivot = find_index(nums,0,len(nums)-1)
        #print(pivot)
        if nums[pivot] == target:
            return pivot
        elif pivot == 0:
            return bs(nums,0,len(nums)-1,target)
        elif target >= nums[0] and target <= nums[pivot-1]:
            #search on left
            return bs(nums,0,pivot-1,target)
        else:
            #search on right
            return bs(nums,pivot,len(nums)-1,target)
