from heapq import heappush, heappop
from math import inf

class Dijkstra:
    def __init__(self, g, n):
        self.n = n
        self.g = g
    

    def dijkstra(self):
        distances = [inf] * (self.n * self.n)  
        distances[self.n+1] = 0
        heap = []
        heappush(heap, (0,self.n+1))
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

        return distances[-1]


