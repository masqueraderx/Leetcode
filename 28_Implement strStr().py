'''
Name: 28. Implement strStr()
Link: https://leetcode.com/problems/implement-strstr/
Time: 12/19/2020
'''

class Solution:
    def strStr(self, haystack: str, needle: str):
        i, j = 0, 0
        lenH, lenN = len(haystack), len(needle)

        if lenN == 0:   return 0
        if lenH < lenN: return -1

        while i < lenH:
            if haystack[i] == needle[j]:
                tmp = i
                while j < lenN and tmp < lenH:
                    if haystack[tmp] != needle[j]:
                        j = 0
                        break
                    tmp += 1
                    j += 1
                if j == lenN:
                    return i
            i += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))
