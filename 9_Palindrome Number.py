'''
Name: 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/
Time: 12/17/2020
Idea: similar to 7_Reverse Interger
'''

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            string_x = str(x)
            rever = string_x[::-1]
            return True if x==int(rever) else False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))