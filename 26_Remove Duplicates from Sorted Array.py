'''
Name: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Time: 12/18/2020
'''

class Solution:
    def removeDuplicates(self, nums):
        # j = 0
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[j]:
        #         nums[j+1] = nums[i]
        #         j += 1
        # return j+1

        # 因为要求每个数最多重复1次。所以如果当前数据长度小于等于1，则不动，i指针往前走。
        # 如果大于1的数组，当前的元素如果比其前面的第二个数大则一定可以加入。
        # i: slow point; j: fast point
        i, j = 0, 0
        while j < len(nums):
            if i < 1 or nums[j] > nums[i-1]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))