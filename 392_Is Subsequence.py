# Name: 392. Is Subsequence
# Link:
# Time: 11/23/2020
# Idea: 2 Pointer

class Solutions:
    def isSubsequence(self, s: str, t: str):
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solutions()
    print(s.isSubsequence("abc", "ahbgdc"))