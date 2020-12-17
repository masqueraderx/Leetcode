'''
Name: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Time: 12/17/2020
'''


class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {'(': ')', '[': ']', '{': '}'}
        stack = []

        # if len(s) <= 1:
        #     return False

        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                # in case of "){"
                if not stack:
                    return False
                mark = stack.pop()
                if mydict[mark] == i:
                    continue
                else:
                    return False
        # in case of "[[[[" or you can uncomment the line above,
        # which will run faster in Leetcode test cases
        if stack:
            return False
        return True

        ## more faster way
        # stack = []
        # left = ['(', '[', '{']
        # right = [')', ']', '}']
        # for char in s:
        #     if char in left:
        #         stack.append(char)
        #     elif char in right:
        #         if len(stack) <= 0:
        #             return False
        #         if left.index(stack.pop()) != right.index(char):
        #             return False
        # return len(stack) == 0