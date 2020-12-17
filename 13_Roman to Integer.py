'''
Name: 13. Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/
Time: 12/17/2020
'''

class Solution:
    def romanToInt(self, s):
        mydict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if mydict[s[i]] < mydict[s[i+1]]:
                res -= mydict[s[i]]
            else:
                res += mydict[s[i]]
        res += mydict[s[-1]]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))