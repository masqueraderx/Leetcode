# Name: 74. Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Time: 11/23/2020

class Solutions:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l, r = 0, len(matrix[0])
        m = False
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                num = i
                m = True
                break
        if m:
            while l < r:
                mid = l + (r - l) // 2
                if matrix[num][mid] > target:
                    r = mid
                elif matrix[num][mid] < target:
                    l = mid + 1
                else:
                    return True
        return False

if __name__ == '__main__':
    s = Solutions()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
