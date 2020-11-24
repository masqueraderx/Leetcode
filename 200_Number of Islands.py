# Name: 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Time: 11/24/2020

class Solution:
    def numIslands(self, grid):
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = '0'
            if x-1 >= 0 and grid[x-1][y] == '1':
                dfs(x-1, y)
            if x+1 < row and grid[x+1][y] == '1':
                dfs(x+1, y)
            if y-1 >= 0 and grid[x][y-1] == '1':
                dfs(x, y-1)
            if y+1 < col and grid[x][y+1] == '1':
                dfs(x, y+1)
        sum = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    sum += 1
                    dfs(i, j)
        return sum

if __name__ == '__main__':
    s = Solution()
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid))