# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Time: 11/23/2020

class Solution:
    def merge(self, intervals):
        # Sort according to the first element
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            # Intersections
            elif interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            # No intersections
            else:
                res.append(interval)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))