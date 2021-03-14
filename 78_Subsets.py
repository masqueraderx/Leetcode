'''
Name: 78. Subsets
Link: https://leetcode-cn.com/problems/subsets/
Time: Mar, 14, 2021
Idea: backtracking: for loop plus iteration
'''

import copy
class Solution:
    def subset(self, nums):
        '''

        :param nums: list[int]
        :return: list[list[int]]
        '''

        res = []
        temp = []
        def dfs(nums, res, start, temp):
            x = copy.deepcopy(temp)
            res.append(x)
            for i in range(start, len(nums)):
                temp.append(nums[i]) #choose the left node
                dfs(nums, res, i+1, temp)
                temp.remove(nums[i]) # Or choose the right node
        dfs(nums, res, 0, temp)
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subset(nums))

