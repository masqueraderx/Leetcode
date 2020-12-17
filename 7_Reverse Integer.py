'''
Name: 7. Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/
Time: 12/17/2020
'''

class Solution:
    def reverse(self, x):

        # # Find the divisor and remains
        # remaining = []
        # res = 0
        # flag = False
        # if x<0:
        #     flag = True
        #     x = -x
        # while x:
        #     remaining.append(x%10)
        #     x = x//10
        # for num in remaining:
        #     res = res*10 + num
        # if flag:
        #     res = -res
        # return res if -pow(2,31) <= res <= pow(2,31)-1 else 0

        # convert int to str and reverse it
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0:
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)