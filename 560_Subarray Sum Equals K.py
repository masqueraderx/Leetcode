'''
Name: 560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/
Time: 11/26/2020
'''

class Solution:
    def subarraySum(self, nums, k):
        # #Cumulative sum (TLE)
        # dp = [0] * (len(nums) + 1)
        # count = 0
        #
        # for i in range(1, len(nums) + 1):
        #     dp[i] = dp[i - 1] + nums[i - 1]
        #
        # for j in range(len(nums)):
        #     for l in range(j + 1, len(nums) + 1):
        #         if dp[l] - dp[j] == k:
        #             count += 1
        #
        # return count

        # Hashmap
        res = 0
        sum = 0
        mydict = {}
        mydict[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in mydict:
                res += mydict[sum-k]
            mydict[sum] = mydict.get(sum, 0) + 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([-1,-1,1], 0))
