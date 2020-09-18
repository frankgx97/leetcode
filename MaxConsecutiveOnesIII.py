class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left, right, zeros, maxx = 0, 0, 0, 0
        while right < len(A):
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            
            maxx = max(maxx, right - left + 1)
            right += 1
            #print(A[left:right+1])
        return maxx
