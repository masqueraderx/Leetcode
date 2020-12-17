'''
Name: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/
Time: 12/17/2020
'''

class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ''
        if len(strs) == 0:
            return prefix

        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(s[i] == c for s in strs):
                prefix += c
            else:
                break
        return prefix


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
