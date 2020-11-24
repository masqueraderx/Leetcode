'''
Name: 207. Course Schedule
Link: https://leetcode.com/problems/course-schedule/
Time: 11/24/2020
'''

import collections
class Solutions:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        myGraph = collections.defaultdict(list)
        # establish the linked matrix
        for u,v in prerequisites:
            myGraph[u].append(v)
        vis = [0] * numCourses
        for i in range(numCourses):
            if not self.dfs(myGraph, vis, i):
                return False
        return True

    def dfs(self, graph, vis, i):
        # the point being visited is being visited, there is a loop
        if vis[i] == 1: return False
        # if the point is visited and safe, it's safe
        if vis[i] == 2: return True
        # is visiting
        vis[i] = 1
        for j in graph[i]:
            # if there is circle
            if not self.dfs(graph, vis, j):
                return False
        # visited
        vis[i] = 2
        return True

if __name__ == '__main__':
    s = Solutions()
    print(s.canFinish(2, [[1,0],[0,1]]))
