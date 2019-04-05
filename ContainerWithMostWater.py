class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max=0
        while right - left > 0:
            area = (right - left) * min(height[left], height[right])
            if area > max:
                max = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max
