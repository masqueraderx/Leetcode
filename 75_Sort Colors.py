'''
Name: 75. Sort Colors
Link: https://leetcode.com/problems/sort-colors/
Time: 11/27/2020
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums)-1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1

if __name__ == '__main__':
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)