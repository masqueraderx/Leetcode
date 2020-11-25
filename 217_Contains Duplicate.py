'''
Name: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Time: 11/25/2020
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mydict = {}
        for num in nums:
            mydict[num] = mydict.get(num, 0) + 1
        mydict = sorted(mydict, key=lambda x: x[1], reverse=True)
        for i in mydict:
            if i[1] > 1:
                return False
        return True