class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def calc(n1, n2):
            def twosum(target_idx, array):
                ans = set()
                dic = {}
                for i in range(len(array)):
                    for j in range(i+1,len(array)):
                        if n1[target_idx] ** 2 == array[i] * array[j]:
                            ans.add((target_idx, i, j))
                return ans
            ans = set()
            for i in range(len(n1)):
                ans = ans | twosum(i, n2)
            return ans
        return len(calc(nums1,nums2)) + len(calc(nums2,nums1))
