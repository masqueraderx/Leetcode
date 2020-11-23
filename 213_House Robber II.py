# Name: 213. House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Time: 11/23/2020
# idea: similar to 198, think of 2 n-1 198 problem.
# 2 dp runs from 1~n-1 and 2~n

class Solutions:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)

        dp1 = [0]*(len(nums)-1)
        dp1[0], dp1[1] = nums[0], nums[1]
        for i in range(2, len(nums)-1):
            dp1[i] = max(nums[i]+dp1[i-2], dp1[i-1])

        dp2 = [0]*(len(nums)-1)
        dp2[0], dp2[1] = nums[1], nums[2]
        for j in range(2, len(nums)-1):
            dp2[j] = max(nums[j+1]+dp2[j-2], dp2[j-1])

        return max(dp1[-1], dp2[-1])

if __name__ == '__main__':
    s = Solutions()
    print(s.rob([2,3,2]))