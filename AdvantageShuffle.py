class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        '''
        Sort and return the next larger item. --optimized by binary search
        Time: nlogn
        '''
        def bs(arr, target):
            l = 0
            r = len(arr) - 1
            ans = 0; 
            while (l <= r): 
                mid = (l + r) // 2; 
                if (arr[mid] <= target): 
                    l = mid + 1; 
                else: 
                    ans = mid; 
                    r = mid - 1; 

            return ans; 
        A.sort()
        r = []
        for i in B:
            index = bs(A, i)
            r.append(A[index])
            del A[index]
        return r
