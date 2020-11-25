'''
Name: 925. Long Pressed Name
Link: https://leetcode.com/problems/long-pressed-name/
Time: 11/24/2020
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False

        # if there is still some characters left *unmatched* in the origin string,
        # then we don't have a match.
        # e.g.  name = "abc"  typed = "aabb"
        if i != len(name):
            return False
        # In the case that there are some redundant characters left in typed
        # we could still have a match.
        # e.g.  name = "abc"  typed = "abccccc"
        else:
            while j < len(typed):
                if typed[j] != typed[j - 1]:
                    return False
                j += 1

        return True

