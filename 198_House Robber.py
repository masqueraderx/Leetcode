# Name: 198. House Robber
# Link: https://leetcode.com/problems/house-robber/
# Time: 11/23/2020
# idea: dp: dp function
# if rob, nums[i]+dp[i-2]
# if not rob, dp[i-1]

class Solutions:
    def rob(self, nums):

        if len(nums) == 0:
            return 0
        elif len(nums) < 2:
            return max(nums)

        dp = [0]*len(nums)
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])

        return max(dp)

if __name__ == '__main__':
    s = Solutions()
    print(s.rob([1,2,3,1]))