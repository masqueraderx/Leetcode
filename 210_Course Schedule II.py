'''
Name: 210. Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Time: 11/24/2020
'''

import collections
class Solutions:
    def findOrder(self, numCourses: int, prerequisites):
        myGraph = collections.defaultdict(list)
        for u,v in prerequisites:
            myGraph[u].append(v)
        vis = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(myGraph, vis, path, i):
                return []
        return path

    def dfs(self, graph, vis, path, i):
        if vis[i] == 1: return False
        if vis[i] == 2: return True

        vis[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, vis, path, j):
                return False

        vis[i] = 2
        path.append(i)
        return True

if __name__ == '__main__':
    s = Solutions()
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))