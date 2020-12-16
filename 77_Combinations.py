'''
Name: 77. Combinations
Link: https://leetcode.com/problems/combinations/
Time: 12/16/2020
'''

class Solution:
    def combine(self, n, k):
        self.count = 0
        ans = []

        def dfs(start, path):
            if self.count == k:
                ans.append(path)
                return
            for i in range(start, n+1):
                self.count += 1
                dfs(i, path+[i])
                self.count -= 1

        dfs(1, [])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))