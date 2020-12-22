'''
Name: 17. Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Time: 12/22/2020
'''

class Solution:
    def letterCombinations(self, digits):
        return list(self.recur(digits))

    def recur(self, x):
        mydict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(x) == 0:
            return []

        for i in mydict[x[0]]:
            if len(x) == 1:
                yield i
            else:
                for j in self.recur(x[1:]):
                    yield i + j

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))