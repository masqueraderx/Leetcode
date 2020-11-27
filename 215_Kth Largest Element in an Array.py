'''
Name: 215. Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Time: 11/27/2020
'''

class Solution:
    def findKthLargest(self, nums, k):
        # # lazy way
        # nums = sorted(nums, reverse=True)
        # return nums[k-1]

        # Quick Sort
        end = len(nums) - 1
        self.QuickSort(nums, 0, end)
        return nums[-k]

    def Partition(self, nums, left, right):
        tmp = nums[left]
        while left < right:
            while left < right and nums[right] > tmp:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= tmp:
                left += 1
            nums[right] = nums[left]
        nums[left] = tmp
        return left

    def QuickSort(self, nums, left, right):
        if left < right:
            pos = self.Partition(nums, left, right)
            self.QuickSort(nums, left, pos-1)
            self.QuickSort(nums, pos+1, right)


if __name__ == '__main__':
    s = Solution()
    array = [3,2,1,5,6,4]
    print(s.findKthLargest(array, 2))