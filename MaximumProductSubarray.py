import math
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        maintain max and min
        * it looks like a sliding window, but it's not
        iterate the arr, for both ma and mi, in each step, choose between
        1. multiply with previous result
        2. abandon previous result, let current result = itself
        ref: https://www.cntofu.com/book/186/problems/152.maximum-product-subarray.md
        '''
        ma = 1
        mi = 1
        r = -math.inf
        for i in nums:
            tempmin = mi
            mi = min(i, min(ma*i,tempmin*i))
            ma = max(i, max(ma*i,tempmin*i))
            r = max(ma,r)
        return r
            
