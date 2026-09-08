class Solution:
    def get_height(self, i, j, heights):
        return (j -i)* min(heights[i], heights[j])
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        max_area = (j -i)* min(heights[i], heights[j])
        while i < j:
            area = (j -i)* min(heights[i], heights[j])
            if area > max_area:
                max_area = area
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return max_area