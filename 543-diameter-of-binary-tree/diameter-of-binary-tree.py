# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxdia = [0] 
        def dfs(root):
            #nonlocal maxdia 
            if not root:
                return 0
            left = right = 0
            left  = dfs(root.left)
            right = dfs(root.right)
            
            height = max(left, right) + 1
            dia = left + right
            if dia > maxdia[0] :
                maxdia[0] = dia
            return height
        dfs(root)
        return maxdia[0]

            

        

        
        

        