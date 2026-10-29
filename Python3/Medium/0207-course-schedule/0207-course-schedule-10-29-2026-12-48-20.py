
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)

        visited = set()
        path = set()

        def dfs(u):
            if u in path:
                return False

            if u in visited:
                return True

            path.add(u)

            for neigh in graph[u]:
                if not dfs(neigh):
                    return False

            path.remove(u)
            visited.add(u)
            return True

        for u in range(numCourses):
            if not dfs(u):
                return False

        return True
