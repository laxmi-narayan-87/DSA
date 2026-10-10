"""Adjacency-list graph and iterative BFS/DFS traversals."""

from collections import deque
from typing import Generic, Hashable, TypeVar

V = TypeVar("V", bound=Hashable)


class Graph(Generic[V]):
    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self.adjacency: dict[Hashable, list[Hashable]] = {}

    def add_vertex(self, vertex: V) -> None:
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, source: V, target: V) -> None:
        self.add_vertex(source)
        self.add_vertex(target)
        self.adjacency[source].append(target)
        if not self.directed:
            self.adjacency[target].append(source)

    def bfs(self, start: V) -> list[V]:
        if start not in self.adjacency:
            return []
        visited = {start}
        order: list[V] = []
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            order.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: V) -> list[V]:
        if start not in self.adjacency:
            return []
        visited: set[V] = set()
        order: list[V] = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)
            order.append(vertex)
            # Reverse preserves adjacency insertion order in the visit sequence.
            stack.extend(reversed(self.adjacency[vertex]))
        return order


if __name__ == "__main__":
    graph = Graph[int]()
    for edge in ((1, 2), (1, 3), (2, 4), (3, 5)):
        graph.add_edge(*edge)
    print(graph.bfs(1))
    print(graph.dfs(1))
    print(graph.bfs(99))  # [] for a missing start vertex
