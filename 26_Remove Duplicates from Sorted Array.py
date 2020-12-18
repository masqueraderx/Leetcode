'''
Name: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Time: 12/18/2020
'''

class Solution:
    def removeDuplicates(self, nums):
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        return j+1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))