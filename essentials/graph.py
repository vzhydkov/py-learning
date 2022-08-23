from typing import List


class ConnectedComponents:
    """
    Count number of Connected Components in an Undirected Graph
    Time complexity: O(E+V)
    Space complexity: O(E+V)
    Where E = Number of edges, V = Number of vertices
    """
    def dfs(self, node: int, graph: List[List[int]], visited: List[bool]):
        for adjacency in graph[node]:
            if not visited[adjacency]:
                visited[adjacency] = True
                self.dfs(adjacency, graph, visited)

    def count(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if not visited[i]:
                count += 1
                visited[i] = True
                self.dfs(i, graph, visited)
        return count


class NeighboursGraph:
    """
    Find maximum number for each connected component in an undirected graph
    """
    # row and column numbers of 4 neighbours
    ROW_SHIFT = [0, 1, 0, -1]
    COL_SHIFT = [-1, 0, 1, 0]

    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.n_row = len(graph)
        self.n_col = len(graph[0])
        self.count = 0
        self.curr_neighbour = None

    def is_safe(self, i: int, j: int, visited: List[List[bool]]):
        return (0 <= i < self.n_row
                and 0 <= j < self.n_col
                and not visited[i][j]
                and self.graph[i][j] == self.curr_neighbour)

    def dfs(self, i: int, j: int, visited: List[List[bool]]):
        self.count += 1
        visited[i][j] = True
        # recur for all connected neighbours
        for k in range(4):
            if self.is_safe(i + self.ROW_SHIFT[k], j + self.COL_SHIFT[k], visited):
                self.dfs(i + self.ROW_SHIFT[k], j + self.COL_SHIFT[k], visited)

    def count_neighbours(self):
        result = {}
        neighbours = [self.graph[0][0]]
        for self.curr_neighbour in neighbours:
            visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
            for i in range(self.n_row):
                for j in range(self.n_col):
                    # add new neighbours if exist
                    if self.graph[i][j] not in neighbours:
                        neighbours.append(self.graph[i][j])
                    if visited[i][j] is False and self.graph[i][j] == self.curr_neighbour:
                        self.dfs(i, j, visited)
                        # save only biggest number of neighbours
                        if result.get(self.curr_neighbour, 0) < self.count:
                            result[self.curr_neighbour] = self.count
                        self.count = 0
        return result


if __name__ == "__main__":
    # connected components
    # 0 - 1   3
    #     |   |
    #     2   4
    assert 2 == ConnectedComponents().count(5, [[0, 1], [1, 2], [3, 4]])
    # neighbours graph
    matrix = [
        [0, 0, 1, 2],
        [0, 1, 2, 1],
        [2, 1, 1, 1],
    ]
    graph = NeighboursGraph(matrix)
    assert {0: 3, 1: 5, 2: 1} == graph.count_neighbours()

    # Example of DFS and BFS
    graph = {
        'A': ['B','C'],
        'B': ['D', 'E'],
        'C': [],
        'D': [],
        'E': []
    }

    def dfs(visited: set, graph: dict, node: str):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(visited, graph, neighbor)
    visited = set()
    dfs(visited, graph, "A")
    assert visited == {'E', 'B', 'A', 'C', 'D'}

    def bfs(visited: set, graph: dict, node: str):
        visited.add(node)
        queue.append(node)
        while queue:
            s = queue.pop(0)
            for neighbor in graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    visited = set()
    queue = []
    dfs(visited, graph, "A")
    assert visited == {'E', 'C', 'D', 'B', 'A'}
