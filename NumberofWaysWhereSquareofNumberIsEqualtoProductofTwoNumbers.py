class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        dic1 = {}
        dic2 = {}
        for i in range(len(nums1)-1):
            for j in range(i+1, len(nums1)):
                v = nums1[i] * nums1[j]
                if v in dic1:
                    dic1[v] += 1 
                else:
                    dic1[v] = 1
        for i in range(len(nums2)-1):
            for j in range(i+1, len(nums2)):
                v = nums2[i] * nums2[j]
                if v in dic2:
                    dic2[v] += 1
                else:
                    dic2[v] = 1
        ans = 0
        for v in nums1:
            if v*v in dic2:
                ans += dic2[v*v]
        for v in nums2:
            if v*v in dic1:
                ans += dic1[v*v]
        return ans
