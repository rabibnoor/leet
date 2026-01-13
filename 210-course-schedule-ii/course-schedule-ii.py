class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = {}

        for i in prerequisites:
            if i[0] in adj:
                adj[i[0]].append(i[1])
            else: 
                adj[i[0]] = [i[1]]
        visited = {}
        ret = []
        print(adj)
        def dfs(v):
            if visited.get(v) == 2:
                #print("v", v)
                return True
            visited[v] = 1
            if v in adj:
                #print(v)
                for k in adj[v]:
                    #print(v,"k",k)
                    if k in visited:
                        if visited[k] == 1:
                            return False
                        if visited[k] == 2:
                            
                            #print(v,"k",k, 2)
                            continue
                    
                   #print(v,"k",k, 1)
                    if not dfs(k):
                        return False
            
            visited[v] = 2
            ret.append(v)
            return True
           

        for i in range(numCourses):
            if i in adj:
               if not dfs(i):
                    return []

        for i in range(numCourses):
            if i not in visited:
                ret.append(i)
    
        #ret.reverse()
        #print(ret)
        return ret

                
                
                
