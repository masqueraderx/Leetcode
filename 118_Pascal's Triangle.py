'''
Name: 118. Pascal's Triangle
Link: https://leetcode.com/problems/pascals-triangle/
Time: 12/20/2020
'''

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                res[i].append((res[i-1][j-1] if j > 0 else 0) + (res[i-1][j] if j < i else 0))
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
