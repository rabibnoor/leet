class Solution(object):
    visited = {}
    def dfs(self, adj, key):
        if key in adj:
            val = adj[key]
            for k in val:
                #print(key, k)
                if k in self.visited and self.visited[k] == 1:
                    return False
                if k in self.visited and self.visited[k] == 2:
                    continue
                
                self.visited[k] = 1
                ret = self.dfs( adj, k)
                if ret == False:
                    return False
                self.visited[k] = 2
            self.visited[key] = 2

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.visited = {}
        adj = {}
        courses = numCourses
        prereq = prerequisites
        for p in prereq:
            n = p[0]
            m = p[1]
            if n in adj:
                adj[n][m] = 1
            else:
                adj[n] = {}
                adj[n][m] = 1
            
            
        #print(adj)
        for k in adj:
            if k not in self.visited:
                self.visited[k] = 1
                ret = self.dfs(adj, k)
                if ret == False:
                    return False
        return True
        
        