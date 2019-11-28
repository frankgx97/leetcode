class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
        two pointers - ac
        left keeps moving right and stop if meet a odd item
        right pointer do the same
        swap the left and right
        '''
        left = 0
        right = len(A)-1
        
        while left < right:
            while left <= len(A)-1 and A[left] %2 != 1 :
                left += 1
            while right >= 0 and A[right] %2 != 0:
                right -= 1
            if left < right:
                temp = A[left]
                A[left] = A[right]
                A[right] = temp
        return A
