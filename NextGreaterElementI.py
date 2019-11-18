class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        mono decrease stack - ac
        mono stack is a good option for finding the max/min item on one side of amn array
        ex. buy and selling stocks
        '''
        stack = []
        dic = {}
        for i in range(len(nums2)):
            if not stack or stack[-1] > nums2[i]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] > stack[-1]:
                    dic[stack.pop(-1)] = nums2[i]
                stack.append(nums2[i])
        while stack:
            dic[stack.pop(-1)] = -1
        r = []
        for i in nums1:
            r.append(dic[i])
        return r
