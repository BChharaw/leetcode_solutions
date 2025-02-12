class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while(left <= right):
            max_water = max(max_water, (right-left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return max_water