# 94 Binary Tree Inorder Traversal

# Stack
class Solution(object):
            def inorderTraversal(self, root):
                res,s = [],[(root,False)]
                while s:
                    node,v = s.pop()
                    if node:
                        if v:
                            res.append(node.val)
                        else:
                            s.append((node.right,False))
                            s.append((node,True))
                            s.append((node.left,False))
                return res

# Recursion
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        self.dfs(root.left,res)
        res.append(root.val)
        self.dfs(root.right,res)

#144. 二叉树的前序遍历

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left,res)
        self.dfs(root.right,res)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = [root]
        while s:
            node = s.pop()
            if node:
                res.append(node.val)
                s.append(node.right)
                s.append(node.left)
        return res

# 145. 二叉树的后序遍历


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root,res)
        return res

    def dfs(self,root,res):
        if not root:
            return
        self.dfs(root.left,res)
        self.dfs(root.right,res)
        res.append(root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = [(root,False)]
        while s:
            node, v = s.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    s.append((node,True))
                    s.append((node.right,False))
                    s.append((node.left,False))
        return res
        
