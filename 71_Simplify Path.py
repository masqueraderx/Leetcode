'''
Name: 71. Simplify Path
Link: https://leetcode-cn.com/problems/simplify-path/
Time: Mar, 09, 2021
'''
class Solution:
    def simplifyPath(self, path):
        '''
        :param path: str
        :return: str
        '''
        out = ['/']
        for i in path.split('/'):
            if i:
                if i == '.':
                    continue
                elif i == '..':
                    if len(out) > 1:
                        out.pop(-1)
                    else:
                        continue
                else:
                    try:
                        out.append(out[-1] + i + '/')
                    except:
                        out.append('/')
        if len(out) == 1:
            return out[-1]
        else:
            return out[-1][:-1]

if __name__ == '__main__':
    s = Solution()
    path = "/a/./b/../../c/"
    print(s.simplifyPath(path))