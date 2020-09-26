"""
Find maximum number of each connected neighbours
"""


class NeighboursGraph:
    # row and column numbers of 4 neighbours
    ROW_SHIFT = [0, 1, 0, -1]
    COL_SHIFT = [-1, 0, 1, 0]

    def __init__(self, graph):
        self.graph = graph
        self.n_row = len(graph)
        self.n_col = len(graph[0])
        self.count = 0
        self.curr_neighbour = None

    def is_safe(self, i, j, visited):
        return (0 <= i < self.n_row
                and 0 <= j < self.n_col
                and not visited[i][j]
                and self.graph[i][j] == self.curr_neighbour)

    def dfs(self, i, j, visited):
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
    matrix = [
        [0, 0, 1, 2],
        [0, 1, 2, 1],
        [2, 1, 1, 1],
    ]
    g = NeighboursGraph(matrix)
    print(g.count_neighbours())
    # assert {0: 3, 1: 5, 2: 1} == g.count_neighbours()
