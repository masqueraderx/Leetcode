'''
Name: 11. Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Time: 12/22/2020
'''

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height)-1
        area = 0
        while left <= right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return area

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))