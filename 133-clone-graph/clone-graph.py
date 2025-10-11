"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    all_nodes = {}
    def traverse(self, node):
        if node:
            copy = Node()
            copy.val = node.val
            self.all_nodes[node] = copy
            
            #print(node.val)
            for n in node.neighbors:
                if n:
                   
                    if n not in self.all_nodes:
                        newcopy = self.traverse(n)
                        copy.neighbors.append(newcopy)
                    else:
                        copy.neighbors.append(self.all_nodes[n])

            return copy


    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.all_nodes = {}
        copy = self.traverse(node)
        return copy


        