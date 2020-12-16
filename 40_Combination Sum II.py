'''
Name: 40. Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/
Time: 12/16/2020
'''


class Solution:
    def combinationSum2(self, candidates, target):

        def dfs(cand, target, index, path, tmp):
            if target == 0:
                path.append(tmp)
                return
            if target < 0:
                return
            for i in range(index, len(cand)):
                # 这个判断保证不重复例如1，1，2，5，6，7，10，第二个1就会被跳过
                if i > index and cand[i] == cand[i - 1]:
                    continue
                dfs(cand, target - cand[i], i + 1, path, tmp + [cand[i]])

        res = []
        candidates.sort()
        dfs(candidates, target, 0, res, [])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))