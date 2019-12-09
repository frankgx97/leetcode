import copy
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        2 sliding windows
        maintain two windows with dictionary
        one counts subarray with k distinct chars,
        the other one counts subarray with 
        O(n^2)
        '''
        r = 0
        left1 = 0
        left2 = 0
        right = 0
        wind1 = {}
        wind2 = {}
        for i in range(len(A)):
            right = i
            if A[i] not in wind1:
                wind1[A[i]] = 1
            else:
                wind1[A[i]] += 1
                
            if A[i] not in wind2:
                wind2[A[i]] = 1
            else:
                wind2[A[i]] += 1
            
            while len(wind1) > K:
                if wind1[A[left1]] > 1:
                    wind1[A[left1]] -= 1
                else:
                    del(wind1[A[left1]])
                left1 += 1
                
            while len(wind2) >= K:
                if wind2[A[left2]] > 1:
                    wind2[A[left2]] -= 1
                else:
                    del(wind2[A[left2]])
                left2 += 1
            r += left2-left1
        return r
