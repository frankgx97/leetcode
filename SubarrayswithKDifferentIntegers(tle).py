import copy
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        sliding window - tle
        maintain a window with a dictionary
        O(n^2)
        '''
        r = 0
        left = 0
        right = 0
        wind = {}
        for i in range(len(A)):
            if A[i] not in wind:
                wind[A[i]] = 1
            else:
                wind[A[i]] += 1
            right = i
            if len(wind) < K:
                continue
            elif len(wind) >= K:
                local_wind = copy.copy(wind)
                local_left = left
                while len(local_wind) >= K:
                    if len(local_wind) == K:
                        r += 1
                    if local_wind[A[local_left]] > 1:
                        local_wind[A[local_left]] -= 1
                    else:
                        del(local_wind[A[local_left]])
                    local_left += 1
        return r
