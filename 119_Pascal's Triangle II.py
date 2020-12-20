'''
Name: 119. Pascal's Triangle II
Link: https://leetcode.com/problems/pascals-triangle-ii/
Time: 12/20/2020
'''

class Solution:
    def getRow(self, rowIndex):
        res = [[1]]
        for i in range(1, rowIndex + 1):
            res.append([])
            for j in range(i + 1):
                res[i].append((res[i-1][j-1] if j > 0 else 0) + (res[i-1][j] if j < i else 0))
        return res[rowIndex]

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))