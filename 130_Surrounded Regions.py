# Name: 130. Surrounded Regions
# Link: https://leetcode.com/problems/surrounded-regions/
# Time: 11/23/2020
# DFS

class Solution:
    def solve(self, board):
        row, col = len(board), len(board[0])
        def dfs(x, y, connected):
            board[x][y] = 'm'
            connected.append((x, y))
            if x-1 >= 0 and board[x][y] == 'O':
                dfs(x-1, y)
            if x+1 < row and board[x][y] == 'O':
                dfs(x+1, y)
            if y-1 >= 0 and board[x][y] =='O':
                dfs(x, y-1)
            if y+1 < col and board[x][y] == 'O':
                dfs(x, y+1)
            return connected

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    connected = dfs(i, j, [])
                    flag = True

                    # Judge whether it's surrounded region is on the border or not
                    for x,y in connected:
                        if x == 0 or x == row-1 or y == 0 or y == col-1:
                            flag = False
                            break
                    # change the region
                    if flag:
                        for d in connected:
                            board[d[0]][d[1]] = 'X'
                    else:
                        for d in connected:
                            board[d[0]][d[1]] = 'O'

if __name__ == '__main__':
    s = Solution()
    maze = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s.solve(maze)
    print(maze)
