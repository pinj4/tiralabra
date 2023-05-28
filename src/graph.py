import random

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [['x'] * (self.n) for _ in range(self.n)]
        self.graph = [[] for _ in range(self.n*self.n+1)]
        self.weights = {}
        for i in range(self.n*self.n+3):
            self.weights[i] = 10**9
    
    def get_graph(self):
        return self.graph
    
    def add_edge(self, a, b, node1, node2):
        if a >= 0 and b >= 0: 
            if node1 != "x" and node2 != "x":   
                self.graph[a].append((b, self.weights[b]))   
                self.graph[b].append((a, self.weights[a]))  
    
    def generate_matrix(self):
        seq = [1,2,3,4,5,6,7,8,9,0,0,0,0]
        node = 1
        for row in range(len(self.matrix)):
            for x in range(len(self.matrix[row])):
                if (row, x) == (0,0):
                    self.matrix[0][0] = "s"
                elif (row, x) == (self.n-1,self.n-1):
                    self.matrix[self.n-1][self.n-1] = "e"
                    self.weights[node] = 0
                else:
                    rand = random.choice(seq)
                    if rand != 0:
                        self.matrix[row][x] = rand
                        self.weights[node] = rand
                self.add_edge(node, node-1, self.matrix[row][x],self.matrix[row][x-1])
                self.add_edge(node, node-self.n, self.matrix[row][x], self.matrix[row-1][x])
                node += 1

    def print_graph(self):
        for row in self.matrix:
            print(*row, sep="|")
