# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def qpush(self,node, myQ):
        myQ.append(node)
 
    def qpop(self,myQ):
       node = myQ.pop(0)
       return node
    
    def bfs(self,myQ, ret):
        if not myQ:
            return ret
        item = self.qpop(myQ)
        node = item[0]
        level = item[1]
        #print("now",(node.val), (level), len(myQ))

        
        #print(ret)
        #print(len(ret))
        if len(ret) < level+1:
            ret.append([node.val])
        else:
            ret[level].append(node.val)

        if node.left:
            self.qpush((node.left, level+1), myQ)
        
        if node.right:
            self.qpush((node.right, level+1), myQ)
        
        #print("q",[v[0].val for v in myQ])
        #print("ret", ret)
        self.bfs(myQ, ret)
        return ret

        

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        myQ = []
        self.qpush((root, 0), myQ)
        

        return self.bfs(myQ, [])

      
        