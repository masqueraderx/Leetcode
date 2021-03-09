'''
Name: 299. Bulls and Cows
Link: https://leetcode-cn.com/problems/bulls-and-cows/
Time: Mar, 09, 2021
'''


class Solution:
    def getHint(self, secret, guess):
        '''
        :param secret: str
        :param guess: str
        :return: str
        '''
        a = 0
        new_s = []
        new_g = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                continue
            new_s.append(int(secret[i]))
            new_g.append(int(guess[i]))

        b = 0
        for g in new_g:
            if g in new_s:
                b += 1
                new_s.pop(new_s.index(g))

        res = str(a) + 'A' + str(b) + 'B'
        return res

if __name__ == '__main__':
    s = Solution()
    secret = "1807"
    guess = "7810"
    print(s.getHint(secret, guess))