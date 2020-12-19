'''
Name: 459. Repeated Substring Pattern
Link: https://leetcode.com/problems/repeated-substring-pattern/submissions/
Time: 12/19/2020
'''

class Solution:
    def repeatedSubstringPattern(self, s: str):
        l = len(s)
        for i in range(1, l // 2 + 1):
            if l % i == 0:
                sub = s[:i]
                repeat = l // i
                if sub * repeat == s:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern("abcabcabcabc"))