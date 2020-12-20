'''
Name: 58. Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/
Time: 12/20/2020
'''

class Solution:
    def lengthOfLastWord(self, s):
        split_str = s.split(" ")
        for word in split_str:
            if len(word) != 0:
                return len(word)
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))