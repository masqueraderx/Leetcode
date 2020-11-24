'''
Name: 695. Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/
Time: 11/24/2020
'''

class Solutions:
    def maxAreaOfIsland(self, grid):
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            # visited
            grid[x][y] = 0
            count = 1
            if x-1 >= 0 and grid[x-1][y] == 1:
                count += dfs(x-1, y)
            if x+1 < row and grid[x+1][y] == 1:
                count += dfs(x+1, y)
            if y-1 >= 0 and grid[x][y-1] == 1:
                count += dfs(x, y-1)
            if y+1 < col and grid[x][y+1] == 1:
                count += dfs(x, y+1)
            return count

        area = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        return area

if __name__ == '__main__':
    s = Solutions()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(s.maxAreaOfIsland(grid))