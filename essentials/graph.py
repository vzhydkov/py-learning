class Graph:
    def __init__(self, graph):
        self.n_row = len(graph)
        self.n_col = len(graph[0])
        self.graph = graph
        self.curr_key = None
        self.count = 0

    def is_safe(self, i, j, visited):
        return (0 <= i < self.n_row
                and 0 <= j < self.n_col
                and not visited[i][j]
                and self.graph[i][j] == self.curr_key)

    def dfs(self, i, j, visited):
        self.count += 1
        # These arrays are used to get row and column numbers of 4 neighbours
        row_nbr = [0, 1, 0, -1]
        col_nbr = [-1, 0, 1, 0]

        visited[i][j] = True
        # Recur for all connected neighbours
        for k in range(4):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.dfs(i + row_nbr[k], j + col_nbr[k], visited)

    def count_neighbours(self):
        """
        >>> graph.count_neighbours()
        {0: 3, 1: 5, 2: 1}
        """
        result = {}
        check = [self.graph[0][0]]
        for key in check:
            self.curr_key = key
            visited = [[False for _ in range(self.n_col)] for _ in range(self.n_row)]
            for i in range(self.n_row):
                for j in range(self.n_col):
                    if self.graph[i][j] not in check:
                        check.append(self.graph[i][j])
                    if visited[i][j] is False and self.graph[i][j] == self.curr_key:
                        self.dfs(i, j, visited)
                        if result.get(self.curr_key, 0) < self.count:
                            result[self.curr_key] = self.count
                        self.count = 0
        return result


if __name__ == "__main__":
    graph = [
        [0, 0, 1, 2],
        [0, 1, 2, 1],
        [2, 1, 1, 1],
    ]
    import doctest
    doctest.testmod(extraglobs={'graph': Graph(graph)})
