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
