'''
Name: 238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Time: 11/26/2020
'''

class Solution:
    def productExceptSelf(self, nums):
        # # Brute Force (TLE)
        # res = []
        # for i in range(len(nums)):
        #     tmp = nums[i]
        #     nums[i] = 1
        #     prod = 1
        #     for j in range(len(nums)):
        #         prod = prod * nums[j]
        #     res.append(prod)
        #     nums[i] = tmp
        # return res

        # if we know the product of all elements before nums[i]
        # and the product of all elements after nums[i]
        dp1 = [1]
        dp2 = [1]
        res = []
        for i in range(len(nums)-1):
            dp1.append(dp1[i] * nums[i])
            dp2.append(dp2[i] * nums[-i-1])
        for j in range(len(nums)):
            res.append(dp1[j] * dp2[-1-j])
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))