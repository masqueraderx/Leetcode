'''
Name: 324. Wiggle Sort II
Link: https://leetcode.com/problems/wiggle-sort-ii/
Time: 11/27/2020
idea:
step1: resort the array in ascending way
step2: find middle, break the array into left and right part
step3: reconstruct nums by left and right reversely
'''

class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = sorted(nums)
        mid = (1 + len(nums)) // 2
        left = nums[:mid]
        right = nums[mid:]
        nums[::2] = left[::-1]
        nums[1::2] = right[::-1]
        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,1,1,6]
    nums = s.wiggleSort(nums)
    print(nums)
