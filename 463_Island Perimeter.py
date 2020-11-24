'''
Name: 463. Island Perimeter
Link: https://leetcode.com/problems/island-perimeter/
Time: 11/24/2020
'''

class Solutions:
    def islandPerimeter(self, grid):
        row, col = len(grid), len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    perimeter += 4
                    # if there is 1 right hand side
                    if i+1 < row and grid[i+1][j]:
                        perimeter -= 2
                    # if there is 1 below
                    if j+1 < col and grid[i][j-1]:
                        perimeter -= 2
        return perimeter

if __name__ == '__main__':
    s = Solutions()
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(s.islandPerimeter(grid))