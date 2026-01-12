class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        vis = {}
        for a, b in prerequisites:
            if a in vis:
                vis[a][b] = 1
            else:
                vis[a] = {b: 1}

        stack = {}   # recursion stack
        done = {}    # fully processed nodes

        def dfs(node):
            if node in done:
                return True
            if node in stack:
                return False
            if node not in vis:
                done[node] = True
                return True

            stack[node] = True
            for nei in vis[node]:
                if not dfs(nei):
                    return False
            del stack[node]
            done[node] = True
            return True

        for k in vis:
            if not dfs(k):
                return False
        return True
