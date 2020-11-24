# Name: 50. Pow(x, n)
# Link: https://leetcode.com/problems/powx-n/
# Time: 11/24/2020

class Solutions:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1 / x, -n
        if n == 0:
            return 1
        # even
        if abs(n) % 2:
            return x * self.myPow(x, abs(n)-1)
        # odd
        else:
            L = self.myPow(x, abs(n)//2)
            return L*L

if __name__ == '__main__':
    s = Solutions()
    print(s.myPow(2.00000, 10))
