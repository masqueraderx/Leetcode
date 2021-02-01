'''
Name: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Time: 02/01/2021
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        '''
        :param strs: list of strings
        :return: list
        '''
        window = defaultdict(list)
        for str in strs:
            string = ''
            for i in sorted(str):
                string += i
            window[string].append(str)
        return window.values()


if __name__ == '__main__':
    s = Solution()
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(test))



