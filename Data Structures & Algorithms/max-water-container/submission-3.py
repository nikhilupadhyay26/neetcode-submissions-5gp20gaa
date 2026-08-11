class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            area = max(area, height * width)

            if heights[l] < heights[r] and l < r:
                l = l + 1
            elif heights[l] > heights[r] and l < r:
                r = r - 1
            else:
                l = l + 1
            
        return area
