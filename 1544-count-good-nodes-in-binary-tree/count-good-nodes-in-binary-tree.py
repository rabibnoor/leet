# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        gnode = [0]
        gnodes = []
        def dfs(root, top):
            if not root:
                return
            if root.val >= top:
                gnode[0] +=1
                #gnodes.append(root.val)
                top = root.val
            dfs(root.left, top)
            dfs(root.right, top)
        dfs(root, root.val)
        #print(gnodes)
        return gnode[0]
        