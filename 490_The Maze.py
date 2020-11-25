'''
Name: Train on BFS (Maze and shortest path)
Time: 11/25/2020
Note: this is not a leetcode problem, i used it to
enhance my understanding on BFS
'''

from collections import deque

maze = []
dis = []
move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solutions:
    def bfs(self, start, destination, maze):
        dis[start[0]][start[1]] = 0
        q = deque()
        begin = Node(start[0], start[1])
        end = Node(destination[0], destination[1])
        q.append(begin)
        while q:
            point = q.popleft()
            if point.x == end.x and point.y == end.y:
                break
            for i in range(4):
                dx = point.x + move[i][0]
                dy = point.y + move[i][1]
                if (0 <= dx < row and 0 <= dy < col and maze[dx][dy] == 1 and dis[dx][dy] == float('inf')):
                    q.append(Node(dx, dy))
                    dis[dx][dy] = dis[point.x][point.y] + 1
                    pre[dx][dy] = point

        print('shortest path is: ', dis[row-1][col-1])
        stack = []
        point = end
        while True:
            stack.append(point)
            if point.x == begin.x and point.y == begin.y:
                break
            prev = pre[point.x][point.y]
            point = prev

        print('The path is:')
        while stack:
            point = stack.pop()
            print('(%d, %d)' % (point.x, point.y))


if __name__ == '__main__':
    maze = [[1, 1, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1]]
    row, col = len(maze), len(maze[0])
    dis = []
    dis = [[float('inf')] * col for _ in range(row)]
    pre = [[None for _ in range(col)] for _ in range(row)]
    s = Solutions()
    s.bfs([0,0], [5,4], maze)