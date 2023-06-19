from math import inf

class IdaStar:
    """ Class for implementing IDA*-algorithm.
    It uses iterative deepening depth-first function with heurestic evaluation function
    to find the shortest path between two points.

    See more at https://en.wikipedia.org/wiki/Iterative_deepening_A*
    """
    def __init__(self, graph, start_node, goal_node):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.estimate = {}
        self.distance = {}

    def ida_star(self):
        threshold = self.heuristics(self.start_node)
        path = [self.start_node]
        while True:
            temp = self.search(path, 0, threshold)
            if temp == "FOUND":
                return len(path)
            else:
                return inf
            threshold = temp

    def sort_neighbours(self, node):
        """Function for sorting node's neighbours by (distance + heurestics) from lowest to highest
        """

        neighbours = []
        for neighbour, weight in self.graph[node]:
            if neighbour not in self.estimate:
                self.estimate[neighbour] = self.distance[node] + weight + self.heuristics(neighbour)
            neighbours.append([neighbour, weight, self.estimate[neighbour]])
        neighbours.sort(key = lambda x: x[2])
        sorted_neighbours = []
        for j in neighbours:
            sorted_neighbours.append((j[0], j[1]))
        return sorted_neighbours
        
    def search(self, path, distance, threshold):
        """iterative funtion that finds the shortest path between two points.

        Args:
            path (list): current search path
            distance (int): current distance from starting node
            threshold (int): estimated cost of the cheapest path

        Returns:
            str "FOUND" if there is a path between selected points
            int "inf" if there isn't one
        """
        current_node = path[-1]
        self.distance[current_node] = distance
        self.estimate[current_node] = distance + self.heuristics(current_node) 
        if self.estimate[current_node] > threshold:
            return self.estimate[current_node]
        if self.goal_node == current_node:
            return "FOUND"
        minim_weight = inf
        neighbours = self.sort_neighbours(current_node)
        for child, weight in neighbours:
            if child not in path:
                path.append(child)
                temp = self.search(path, distance + weight, threshold)
                if temp == "FOUND":
                    return "FOUND"
                elif temp < minim_weight:
                    minim_weight = temp
                path.pop()
        return minim_weight if minim_weight != inf else inf

    def heuristics(self, current_node):
        return abs(current_node - self.goal_node)
