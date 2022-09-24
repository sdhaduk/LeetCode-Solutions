class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while r > l:
            min_height = min(height[r], height[l])
            area = min_height * (r-l)
            max_area = max(max_area, area)
            
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
                
        return max_area
                
            
            
            
            