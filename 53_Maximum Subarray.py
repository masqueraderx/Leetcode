# Name: 53. Maximum Subarray
# Linke: https://leetcode.com/problems/maximum-subarray/
# Time: 11/23/2020
# Idea : dp, the dp function is max(dp[i-1]+nums[i], nums[i])

class Solutions:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

if __name__ == '__main__':
    s = Solutions()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))