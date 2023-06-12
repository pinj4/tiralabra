from math import inf, sqrt

class Map():
    def __init__(self, file):
        self.file = file
        self.map = None
        self.map_width = 0
        self._map_graph = []
        self.graph = []
    
    def print_map(self):
        print(self.map)
    
    def get_graph(self):
        self.create_map()
        self.generate_graph()
        return self.graph
          
    def create_map(self):
        try:
            self.map_file_contents()
            return "Done"
        except:
            return "wrong file"

    def map_file_contents(self):
        map_contents = []
        with open(f"src/maps/{self.file}") as map_file:
            contents = map_file.read()
            self.map = contents

            row = []
            width = []
            for line in contents:
                if line in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    width.append(line)
                elif line != "\n":
                    row.append(line)
                else:
                    map_contents.append(row)
                    row = []
        self.map_width = int("".join(map(str, width)))
        self._map_graph = map_contents
    
    def add_edge(self, a, b, node_a, node_b, weight):
        if a >= 0 and b >= 0:
            if node_a != "@" and node_b != "@":   
                self.graph[a].append((b, weight))   
                self.graph[b].append((a, weight))

    
    def generate_graph(self):
        self.graph = [[] for _ in range(self.map_width*self.map_width)]
        node = 0
        for row in range(len(self._map_graph)):
            for x in range(len(self._map_graph[row])):
                n = self._map_graph[row][x]
                if n != "@":
                    if row - 1 > 0 and x - 1 > 0:
                        self.add_edge(node, node-1, self._map_graph[row][x],self._map_graph[row][x-1], 1)
                        self.add_edge(node, node-self.map_width, self._map_graph[row][x], self._map_graph[row-1][x], 1)
                    ## diagonaalit :
                    if row - 1 > 0 and x - 1 > 0:
                        self.add_edge(node, node-self.map_width - 1, self._map_graph[row][x], self._map_graph[row-1][x-1], sqrt(2))
                    if row - 1 > 0 and x + 1 < self.map_width:
                        self.add_edge(node, node-self.map_width + 1 , self._map_graph[row][x], self._map_graph[row-1][x+1], sqrt(2))
                node += 1
    