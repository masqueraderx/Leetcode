'''
Name: 27. Remove Element
Link: https://leetcode.com/problems/remove-element/
TIme: 12/18/2020
'''

class Solution:
    def removeElement(self, nums, val):
        i, j = 0, len(nums)-1
        while i <= j:
            # if equal to value, swap current point with the last point
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return j + 1

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))