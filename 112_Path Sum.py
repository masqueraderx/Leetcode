# Name: 112. Path Sum
# Link: https://leetcode.com/problems/path-sum/
# Time: 11/23/2020
# Idea: DFS

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solutions:
    def hasPathSum(self, root: TreeNode, sum: int):
        if not root.left and not root.right:
            if sum == 0:
                return True
            else:
                return False

        else:
            return self.hasPathSum(root.left, sum - root.left.val) or \
                   self.hasPathSum(root.right, sum - root.right.val)