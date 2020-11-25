'''
Name: 287. Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/
Time: 11/25/2020
'''

class Solution:
    def findDuplicate(self, nums):
        # # Use dict to record replicate times
        # mydict = {}
        # for num in nums:
        #     mydict[num] = mydict.get(num, 0) + 1
        # for k, v in mydict.items():
        #     if v >= 2:
        #         return k

        # 2 pointer
        slow = 0
        fast = 0

        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]

            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow