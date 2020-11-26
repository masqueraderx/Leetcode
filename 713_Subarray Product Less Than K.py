'''
Name: 713. Subarray Product Less Than K
Link:
Time: 11/26/2020
Idea: slide window
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        left = 0
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            while i >= left and prod >= k:
                prod /= nums[left]
                left += 1
            res += i - left + 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6], 100))

