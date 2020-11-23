# Name: 57. Insert Interval
# Link: https://leetcode.com/problems/insert-interval/
# Time: 11/23/2020
# Idea: Same with 56
class Solutions:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])

        # Merge intersections
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            # intersections
            elif res[-1][1] >= interval[0]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)
        return res

if __name__ == '__main__':
    s = Solutions()
    print(s.insert([[1,3],[6,9]], [2,5]))