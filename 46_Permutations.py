'''
Name: 46. Permutations
Link: https://leetcode.com/problems/permutations/
Time: 12/16/2020
'''

class Solution:
    #将整组数中的所有的数分别与第一个数交换，这样就总是在处理后n-1个数的全排列。
    def permute(self, nums):
        ans = []

        def dfs(start, nums):
            if start == len(nums):
                ans.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start+1, nums)
                nums[i], nums[start] = nums[start], nums[i]
        dfs(0, nums)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))