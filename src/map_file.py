from math import inf

class Map():
    def __init__(self, file):
        self.file = file
        self.map = None
        self.map_width = 0
        self.map_graph = []
        self.graph = None

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
        self.map_graph =  map_contents
     
    def print_map(self):
        print(self.map)
    
    def create_map(self):
        try:
            self.map_file_contents()
            return "Done"
        except:
            return "wrong file"
    
    def get_graph(self):
        return self.graph

    def add_edge(self, a, b, node1, node2):
        if a >= 0 and b >= 0: 
            if node1 != "@" and node2 != "@":   
                self.graph[a].append((b, 1))   
                self.graph[b].append((a, 1))  
    
    def generate_graph(self):
        self.graph = [[] for _ in range(self.map_width*self.map_width)]
        node = 0
        for row in range(len(self.map_graph)):
            for x in range(len(self.map_graph[row])):
                n = self.map_graph[row][x]
                if n != "@":
                    self.add_edge(node, node-1, self.map_graph[row][x],self.map_graph[row][x-1])
                    self.add_edge(node, node-self.map_width, self.map_graph[row][x], self.map_graph[row-1][x])
                node += 1

#m = Map("map_1.map")
#print(m.create_map())
#print(m.map_graph_weighted())
#m.generate_graph()
#print(m.graph)
#print("Graph ", m.get_map_graph())

#m2 = Map("map_4.map")
#print(m2.create_map())
    