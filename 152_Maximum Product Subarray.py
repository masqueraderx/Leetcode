'''
Name: 152. Maximum Product Subarray
Link: https://leetcode.com/problems/maximum-product-subarray/
Time: 11/26/2020
Idea:
dp1 used to record maximum product nums[i]
dp1 = max(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i])
dp2 used to record minimum product num[i]
dp2 = min(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i])
'''


class Solution:
    def maxProduct(self, nums):
        dp1 = [nums[0]]
        dp2 = [nums[0]]
        maxp = nums[0]
        for i in range(1, len(nums)):
            dp1.append(max(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i]))
            dp2.append(min(nums[i], dp1[i-1]*nums[i], dp2[i-1]*nums[i]))
            maxp = max(maxp, dp1[i])
        return maxp

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
