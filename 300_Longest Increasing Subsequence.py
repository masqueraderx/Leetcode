# Name: 300. Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Time: 11/23/2020
# Idea: dp function: dp[i] = max(1, dp[j]+1)

class Solutions:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        # initialization: the LIS of every number is itself
        dp = [1]*len(nums)
        ans = -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = max(1, dp[j]+1)
            ans = max(ans, dp[i])
        print(dp)
        return ans

if __name__ == '__main__':
    s = Solutions()
    print(s.lengthOfLIS([1,2,3,1,2,3,1,2,3]))