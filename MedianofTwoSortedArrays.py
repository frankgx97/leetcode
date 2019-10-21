class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        selected = []
        
        if l%2 == 0:
            selected = [l//2-1,l//2]
        else:
            selected = [l//2]
        
        target = []
        count = -1
        
        while len(nums1) > 0 or len(nums2) > 0:
            count += 1
            temp = 0
            curr = None
            
            if len(nums1) == 0:
                curr = nums2
            elif len(nums2) == 0:
                curr = nums1
            elif nums1[0] < nums2[0]:
                curr = nums1
            else:
                curr = nums2
            temp = curr[0]
            curr.pop(0)
            
            if count in selected:
                target.append(temp)
            if count > max(selected):
                break
        if len(target) == 2:
            return sum(target)/2
        else:
            return target[0] 
