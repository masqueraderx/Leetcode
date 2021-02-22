import collections

class Solution():
    def findPairs(self, nums, k):
        '''
        :param nums: list
        :param k: int
        :return: number of unique k-pairs in the array
        '''
        res = 0
        mydict = collections.Counter(nums)
        for num in set(nums):
            if k > 0 and num + k in mydict:
                res += 1
            if k == 0 and mydict[num] > 1:
                res += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([3, 1, 4, 1, 5], 2))