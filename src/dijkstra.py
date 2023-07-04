from heapq import heappush, heappop
from math import inf

class Dijkstra:
    """ Class for implementing Dijkstra's algorithm.
    Finds the shortest route between two points in a weighted graph.

    See more at https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    """
    def __init__(self, g, n, start_node, goal_node):
        self.n = n
        self.g = g
        self.start_node = start_node
        self.goal_node = goal_node
        self.prev = [-1] * (self.n*self.n)
    
    def dijkstra(self):
        distances = [inf] * (self.n * self.n)  
        distances[self.start_node] = 0
        heap = []
        heappush(heap, (0, self.start_node))
        done = []

        while len(heap) > 0:
            dist, node = heappop(heap)
            if node in done:
                continue
            done.append(node)
            for child in self.g[node]:
                current = distances[child[0]]
                new = distances[node] + child[1]
                if new < current:
                    distances[child[0]] = distances[node] + child[1]
                    heappush(heap, (distances[child[0]], child[0]))
                    self.prev[child[0]] = node

        return distances[self.goal_node]

    def get_path(self):
        s = []
        u = self.goal_node
        while self.prev[u] != -1:
            s.append(u)
            u = self.prev[u]
        s.append(self.start_node)
        s.reverse()
        return s
