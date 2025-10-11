"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    all_nodes = []
    gen_nodes = []
    def traverse(self, node):
        if node:
            self.all_nodes.append(node)
            copy = Node()
            copy.val = node.val
            self.gen_nodes.append(copy)
            #print(node.val)
            for n in node.neighbors:
                if n:
                    try:
                        idx = self.all_nodes.index(n)
                    except:
                        idx = -1
                    if idx == -1:
                        newcopy = self.traverse(n)
                        copy.neighbors.append(newcopy)
                    else:
                        copy.neighbors.append(self.gen_nodes[idx])

            return copy


    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.all_nodes = []
        self.gen_nodes = []
        copy = self.traverse(node)
        return copy


        