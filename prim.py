INF = 99999


class prims:
    def __init__(self, v):
        self.v = v
        self.graph = [[0 for i in range(self.v)] for i in range(self.v)]
        self.visited = [False] * self.v
        self.parent = [-1] * self.v
        self.dist = [INF] * self.v
        self.dist[0] = 0

    def minDis(self):
        mind = INF
        mindex = 0
        for i in range(self.v):
            if self.visited[i] == False and self.dist[i] < mind:
                mind = self.dist[i]
                mindex = i
        return mindex

    def prim(self):
        for _ in range(self.v):
            min_d = self.minDis()
            self.visited[min_d] = True
            for i in range(self.v):
                if (
                    self.visited[i] == False
                    and self.graph[min_d][i] != 0
                    and self.graph[min_d][i] < self.dist[i]
                ):

                    self.dist[i] = self.graph[min_d][i]
                    self.parent[i] = min_d
        print(self.parent)


if __name__ == "__main__":
    g = prims(6)
    g.graph = [
        [0, 4, 6, 0, 0, 0],
        [4, 0, 6, 3, 4, 0],
        [6, 6, 0, 1, 0, 0],
        [0, 3, 1, 0, 2, 3],
        [0, 4, 0, 2, 0, 7],
        [0, 0, 0, 3, 7, 0],
    ]
    g.prim()
