'''
Name: 229. Majority Element II
Link: https://leetcode.com/problems/majority-element-ii/
Time: 11/27/2020
'''

class Solution:
    def majorityElement(self, nums):
        mydict = {}
        res = []
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        for k,v in mydict.items():
            if v > len(nums)//3:
                res.append(k)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([3,2,3]))