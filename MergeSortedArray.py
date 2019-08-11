class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i <= len(nums1) - 1:
            if i > m-1:
                nums1.pop(i)
            else:
                i += 1
        i = 0
        for j in nums2:
            for i in range(len(nums1)):
                if nums1[i] > j:
                    nums1.insert(i, j)
                    break
                elif i == len(nums1)-1:
                    nums1.append(j)
            if len(nums1) == 0:
                nums1.append(j)
        return
