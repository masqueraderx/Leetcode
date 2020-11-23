#Name: 986. Interval List Intersections
#Link: https://leetcode.com/problems/interval-list-intersections/
#Time: 11/23/2020
# Idea: similar to 56, find the intersection part, use two-pointer to
# determine which pointer should move (of course the larger end point,
# becasue only in this way can we find more intersections

class Solution:
    def intervalIntersections(self, A, B):
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            # If intersection
            if low <= high:
                res.append([low, high])

            # Greedy
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res

if __name__ == '__main__':
    a = [[0,2],[5,10],[13,23],[24,25]]
    b = [[1,5],[8,12],[15,24],[25,26]]
    s = Solution()
    print(s.intervalIntersections(a,b))

