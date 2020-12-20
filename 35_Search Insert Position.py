'''
Name: 35. Search Insert Position
Link: https://leetcode.com/problems/search-insert-position/
Time: 12/20/2020
'''

class Solution:
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] < target:
                i += 1
            else:
                return i
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5))