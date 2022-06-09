INF = 99999999


class dij:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [
            [0 for column in range(self.vertices)] for row in range(self.vertices)
        ]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])

    def minDistance(self, cost, visited):
        minDist = INF
        for i in range(self.vertices):
            if cost[i] < minDist and visited[i] == False:
                minDist = cost[i]
                self.min_dex = i

        return self.min_dex

    def dijkstra(self, src):
        cost = [INF for i in range(self.vertices)]
        visited = [False for i in range(self.vertices)]
        cost[src] = 0

        for count in range(self.vertices):
            u = self.minDistance(cost, visited)
            visited[u] = True
            print(cost)
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and visited[v] == False
                    and cost[v] > cost[u] + self.graph[u][v]
                ):
                    cost[v] = cost[u] + self.graph[u][v]
            # print(cost)
        self.printSolution(cost)


if __name__ == "__main__":
    g = dij(5)
    g.graph = [
        [0, 4, 0, 30, 100],
        [4, 0, 50, 0, 0],
        [0, 50, 0, 20, 10],
        [30, 0, 20, 0, 60],
        [100, 0, 10, 60, 0],
    ]
    g.dijkstra(0)
