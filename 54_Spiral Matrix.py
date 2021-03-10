'''
Name: Spiral Matrix
Link: https://leetcode-cn.com/problems/spiral-matrix/
Time: Mar, 10, 2021
'''

class Solution():
    def SpiralOrder(self, matrix):
        '''
        :param matrix: list[list[int]]
        :return: list
        '''
        # define move direction
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di = 0 # define move index
        # define coordinates
        x, y = 0, 0
        # define size of matrix
        m, n = len(matrix), len(matrix[0])
        # define res to store results
        res= []
        for _ in range(m * n):
            res.append(matrix[x][y])
            matrix[x][y] = 'v'

            # watch next step
            x_next, y_next = x + dx[di], y + dy[di]

            # if it's inside the matrix and not visited, then move it
            if 0 <= x_next < m and 0 <= y_next < n and matrix[x_next][y_next] != 'v':
                x, y = x_next, y_next
            # else it's time to change direction (according to dx, dy)
            else:
                di = (di + 1) % 4
                x += dx[di]
                y += dy[di]
        return res

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.SpiralOrder(matrix))