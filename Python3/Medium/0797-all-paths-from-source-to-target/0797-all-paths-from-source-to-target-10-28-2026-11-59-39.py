class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result=[]
        path=[]
        n=len(graph)
        def dfs(node):
            path.append(node)
            if node==n-1:
                result.append(path[:])
            else:
                for neigh in graph[node]:
                    dfs(neigh)
            path.pop()
        dfs(0)
        return result
                
            