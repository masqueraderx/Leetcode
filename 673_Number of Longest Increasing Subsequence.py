# Name: 673. Number of Longest Increasing Subsequence
# link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# Time: 11/23/2020
# Idea: similar to 300, but you need to count the numbers of LIS

class Solutions:
    def findNumberOfLIS(self, nums):
        dp = [[1,1] for _ in range(len(nums))]
        ans = 1
        for i in range(len(nums)):
            count = 0
            # Find the LIS
            for j in range(i):
                if nums[i] > nums[j] and dp[i][0]+1 > dp[j][0]:
                    dp[i][0] = max(1, dp[j][0]+1)
            # Count the number of LIS
            for j in range(i):
                if dp[j][0] == dp[i][0]-1 and nums[i] > nums[j]:
                    count += dp[j][1]
                    dp[i][1] = max(dp[i][1], count)
            ans = max(ans, dp[i][0])
        print(dp)
        return sum([dp[i][1] for i in range(len(dp)) if dp[i][0] == ans])

if __name__ == '__main__':
    s = Solutions()
    print(s.findNumberOfLIS([1,3,5,4,7]))