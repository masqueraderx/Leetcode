'''
Name: 187. Repeated DNA Sequences
Link: https://leetcode-cn.com/problems/repeated-dna-sequences/
Time: Mar, 9, 2021
'''
class Solution:
    def findRepeatedDnaSequences(self, s):
        '''
        :param s: str
        :return: list
        '''
        mydict = {}
        for i in range(len(s)):
            if s[i:i+10] not in mydict:
                mydict[s[i:i+10]] = 1
            else:
                mydict[s[i:i+10]] += 1
        res = []
        for k, v in mydict.items():
            if v > 1:
                res.append(k)
        return res

if __name__ == '__main__':
    s = Solution()
    str = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(s.findRepeatedDnaSequences(str))