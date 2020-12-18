'''
Name: 80. Remove Duplicates from Sorted Array II
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Time: 12/18/2020
'''

class Solution:
    # 因为要求每个数最多重复2次。所以如果当前数据长度小于等于2，则不动，i指针往前走。
    # 如果大于2的数组，当前的元素如果比其前面的第二个数大则一定可以加入。
    def removeDuplicates(self, nums):
        i, j = 0, 0
        while j < len(nums):
            if i < 2 or nums[j] > nums[i-2]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))