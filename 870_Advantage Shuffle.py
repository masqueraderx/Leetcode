'''
Name: 870. Advantage Shuffle
Link: https://leetcode.com/problems/advantage-shuffle/
Time: 11/29/2020
Idea: Use your weakest horse to beat opponent's weakest horse
If win, then add to the res
else, use it to beat opponent's best horse (to consume opponent's resource)
'''

import collections

class Solution:
    def advantageCount(self, A, B):
        A = collections.deque(sorted(A))
        B = collections.deque(sorted((b, i) for i, b in enumerate(B)))
        res = [-1]*len(A)
        while A:
            a = A.popleft()
            b = B[0]
            if a > b[0]:
                B.popleft()
            else:
                b = B.pop()
            res[b[1]] = a
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount([2,0,4,1,2], [1,3,0,0,2]))

