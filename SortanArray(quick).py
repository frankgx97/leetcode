class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        quicksort - ac
        ref: https://bubkoo.com/2014/01/12/sort-algorithm/quick-sort/
        '''
        def swap(arr,i,j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
        def quicksort(nums,left,right):
            if (left > right):
                return 
            pivot_index = partition(nums,left,right)
            quicksort(nums,left,pivot_index-1)
            quicksort(nums,pivot_index+1,right)
        
        def partition(arr,left,right):
            pivot = nums[right]
            index = left
            for i in range(left,right):
                if nums[i] < pivot:
                    swap(nums,i,index)
                    index += 1
            swap(nums,right,index)
            return index
        
        quicksort(nums,0,len(nums)-1)
        return nums
