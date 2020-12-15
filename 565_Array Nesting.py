'''
Name: 565. Array Nesting
Link: https://leetcode.com/problems/array-nesting/
Time: 12/15/2020
Idea: loop through nums and mark visited. In the following loop,
forget it because it is a subset.
'''

class Solution:
    def arrayNesting(self, nums):
        step, ans = 0, 0
        vis = [False] * len(nums)
        for i in range(len(nums)):
            while not vis[i]:
                vis[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([5,4,0,3,1,6,2]))