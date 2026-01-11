"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            if not node:
                return None
            newnode = Node(node.val, [])
            visited[node] = newnode
            for c in node.neighbors:
                newc = dfs(c)
                newnode.neighbors.append(newc)
            return newnode
        return dfs(node)
        
        