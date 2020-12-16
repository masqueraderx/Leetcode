'''
Name: 39. Combination Sum
Link: https://leetcode.com/problems/combination-sum/
Time: 12/16/2020
'''

class Solution:
    def combinationSum(self, candidates, target):

        def dfs(cand, target, index, path, tmp):
            for i in range(index, len(cand)):
                if cand[i] + sum(tmp) == target:
                    path.append([cand[i]] + tmp)
                elif cand[i] + sum(tmp) < target:
                    dfs(cand, target, i, path, tmp+[cand[i]])
                else:
                    return
        res = []
        candidates = sorted(candidates)
        dfs(candidates, target, 0, res, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))