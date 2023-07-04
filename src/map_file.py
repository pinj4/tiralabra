from math import inf, sqrt
import copy

class Map():
    def __init__(self, file):
        self.file = file
        self.map = None
        self.map_width = 0
        self._map_graph = []
        self.graph = []
    
    def print_map(self):
        print(self.map)
    
    def update_map(self, path:list):
        """function for "drawing on" the path the algorithm chose

        Args:
            path (list): nodes in the chosen path

        Returns:
            list: graph with Xs marking the path
        """
        updated = copy.deepcopy(self._map_graph)
        for node in path:
            node_y = node / self.map_width
            node_y = int(node_y) 
            node_x = node - (self.map_width * node_y) + 1
            for y in range(len(updated)):
                for x in range(len(updated[y])):
                    if y == int(node_y+1) and x+1 == node_x:
                        updated[y][x] = "X"

        return updated

    def get_updated(self, updated):
        """function for formatting the map with the drawn on path

        Args:
            updated (list): graph with Xs marking the path

        Returns:
            list: graph with Xs marking the path formatted for printing
        """
        new = []
        for row in updated:
            r = ''.join(row)
            new.append(r)
        return new

    def print_labels(self):
        print("Dijkstra map:", "{:>{}} {:{}}".format( "IDA*",self.map_width-3 , "map:", self.map_width))

    def print_maps(self, map1, map2):
        for row in range(len(map1)):
            print(map1[row],"     ", map2[row])

    def get_graph(self):
        self.create_map()
        self._generate_graph()
        return self.graph

    def get_available_nodes_from_row(self, row):
        nodes = []
        node_num = 1 
        for node in self._map_graph[row]:
            if node != "@":
                nodes.append(node_num)
            node_num += 1
        return nodes

    def create_map(self):
        try:
            self._map_file_contents()
            return "Done"
        except:
            return "wrong file"

    def _map_file_contents(self):
        """function for reading and formatting the map's file
        """
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


    def _generate_graph(self):
        """function for creating a graph for the algorithms to use
        """
        self.graph = [[] for _ in range(self.map_width*self.map_width)]
        node = 0
        for row in range(len(self._map_graph)):
            for x in range(len(self._map_graph[row])):
                n = self._map_graph[row][x]
                if n != "@":
                    ## aloitussolmuun yhteys
                    if node == 1: ## toka solmu
                        self.add_edge(node, 0, self._map_graph[row][x],self._map_graph[1][0], 1)
                    elif node == self.map_width: ## alotussolmun alempi
                        self.add_edge(node, 0, self._map_graph[row][x], self._map_graph[1][0], 1)
                    elif node == self.map_width + 1: ## alotussolmusta viistoon alas
                        self.add_edge(node, 0, self._map_graph[row][x], self._map_graph[1][0], sqrt(2))
                    ## edellinen solmu ja ylempi solmu
                    if row - 1 > 0 and x - 1 > 0:
                        self.add_edge(node, node-1, self._map_graph[row][x],self._map_graph[row][x-1], 1)
                        self.add_edge(node, node-self.map_width, self._map_graph[row][x], self._map_graph[row-1][x], 1)
                    ## diagonaalit :
                    if row - 1 > 0 and x - 1 > 0:
                        self.add_edge(node, node-self.map_width - 1, self._map_graph[row][x], self._map_graph[row-1][x-1], sqrt(2))
                    if row - 1 > 0 and x + 1 < self.map_width:
                        self.add_edge(node, node-self.map_width + 1 , self._map_graph[row][x], self._map_graph[row-1][x+1], sqrt(2))
                node += 1