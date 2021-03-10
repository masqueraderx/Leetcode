'''
Name: 55. Jump Game
Time: Mar, 10, 2021
Link: https://leetcode-cn.com/problems/jump-game/
'''

class Solution:
    # 思路一：
    def canJump(self, nums):
        '''
        :param nums: list[int]
        :return: bool
        '''
        max_pos = 0
        for i in range(len(nums)-1):
            # 如果最大能到达的位置 < 当前索引
            if max_pos < i:
                return False
            # 跟新最大能到达的位置
            max_pos = max(max_pos, nums[i] + i)
        # 最后判断是否可以到达 最后一个索引
        if max_pos >= len(nums) - 1:
            return True
        return False

    # 思路二
    def canJump2(self, nums):
        '''
        :param nums: list[int]
        :return: bool
        '''
        # 倒序遍历
        i = len(nums)-1
        for j in range(len(nums)-2, -1, -1):
            # 如果j不能到达i
            if i - j <= nums[j]:
                # 把i位往前移
                i = j
        return i == 0


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1,0,4]
    print(s.canJump(nums))