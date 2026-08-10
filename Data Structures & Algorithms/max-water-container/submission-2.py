class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if l == r:
                return area
            area2 = (r - l) * min(heights[l], heights[r])
            if area2 > area:
                area = area2
            
            if heights[l] <  heights[r]:
                l = l + 1
            elif heights[l] >  heights[r]:
                r = r - 1
            else:
                r = r - 1

        return area