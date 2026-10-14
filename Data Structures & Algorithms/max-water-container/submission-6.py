class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        curr =(right - left) * min(heights[left], heights[right])
        for i in range(len(heights)): 
            if right == left:
                break

            if (right - left) * min(heights[left], heights[right]) > curr:
                curr = (right - left) * min(heights[left], heights[right])

            if heights[left] > heights[right]: 
                right -= 1
            else: 
                left += 1

        return curr
