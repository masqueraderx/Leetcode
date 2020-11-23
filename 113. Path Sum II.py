# Name: 113. Path Sum II
# Link: https://leetcode.com/problems/path-sum-ii/
# Time: 11/23/2020
# Idea: DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solutions:
    def pathSum(self, root: TreeNode, sum: int):

        def dfs(root, cursum, path):
            if not root.left and not root.right:
                if cursum == sum:
                    ans.append(path)
                    return
            if root.left:
                dfs(root.left, root.left.val+cursum, path+[root.left.val])
            if root.right:
                dfs(root.right, root.right.val+cursum, path+[root.right.val])

        ans = []
        if not root:
            return []
        dfs(root, root.val, [root.val])
        return ans