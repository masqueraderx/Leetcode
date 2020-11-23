# Name: 240. Search a 2D Matrix II
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Time: 11/23/2020

class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                l, r = 0, len(matrix[0])
                while l < r:
                    mid = l + (r - l) // 2
                    if matrix[i][mid] < target:
                        l = mid + 1
                    elif matrix[i][mid] > target:
                        r = mid
                    else:
                        return True
        return False