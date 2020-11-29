'''
Name: 455. Assign Cookies
Link: https://leetcode.com/problems/assign-cookies/
Time: 11/29/2020
'''

class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1,2,3], [1,1]))