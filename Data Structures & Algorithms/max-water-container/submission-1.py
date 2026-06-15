class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area_1 = min(heights[l], heights[r]) * (r-l)

            if area_1 > area:
                area = area_1
                
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1
        return area
            