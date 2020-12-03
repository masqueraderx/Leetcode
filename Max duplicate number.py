
class Solution:
    def find_max_duplicate(self, nums):
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        mydict = sorted(mydict.items(), key = lambda x:x[1], reverse=True)
        return mydict[0][0]

if __name__ == '__main__':
    nums = [1,2,3,4,4,5,6]
    s = Solution()
    print(s.find_max_duplicate(nums))

