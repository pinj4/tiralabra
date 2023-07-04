from math import sqrt, inf

class IdaStar:
    """ Class for implementing IDA*-algorithm.
    It uses iterative deepening depth-first function with heurestic evaluation function
    to find the shortest path between two points.

    See more at https://en.wikipedia.org/wiki/Iterative_deepening_A*
    """
    def __init__(self, graph, start_node, goal_node, n):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.n = n
        self.estimate = {}
        self.distance = {}

    def ida_star(self): 
        threshold = self._heuristics(self.start_node)
        path = [(self.start_node,0)]

        while True:
            temp = self._search(path, 0, threshold)
            if temp == "FOUND":
                dist = sum(float(weight) for _, weight in path)
                shortest_path = [node for node,_ in path]
                return dist, shortest_path
            if temp == inf:
                return inf, []
            threshold = temp

    def _sort_neighbours(self, node):
        """Function for sorting node's neighbours by (distance + heurestics) from lowest to highest
        """ 

        neighbours = []
        for neighbour, weight in self.graph[node]:
            if neighbour not in self.estimate:
                self.estimate[neighbour] = self.distance[node] + self._heuristics(neighbour) + weight
            neighbours.append([neighbour, weight, self.estimate[neighbour]])
        neighbours.sort(key = lambda x: x[2])
        sorted_neighbours = []
        for j in neighbours:
            sorted_neighbours.append((j[0], j[1]))
        return sorted_neighbours
        
    def _search(self, path, distance, threshold):
        """iterative function that finds the shortest path between two points.

        Args:
            path (list): current search path
            distance (int): current distance from starting node
            threshold (int): estimated cost of the cheapest path

        Returns:
            str "FOUND" if there is a path between selected points
            int "inf" if there isn't one
        """
        current_node = path[-1][0]
        self.estimate[current_node] = distance + self._heuristics(current_node)
        self.distance[current_node] = distance

        if self.estimate[current_node] > threshold:
            return self.estimate[current_node]

        if self.goal_node == current_node:
            return "FOUND"

        minim_weight = inf

        neighbours = self._sort_neighbours(current_node)

        for child, weight in neighbours:
            if (child, weight) not in path:
                path.append((child, weight))
                temp = self._search(path, distance + weight, threshold)
                if temp == inf:
                    return inf
                if temp == "FOUND":
                    return "FOUND"
                if temp < minim_weight:
                    minim_weight = temp
                path.pop()

        return minim_weight

    def _heuristics(self, current_node):
        ## solmujen x ja y koordinaatit
        node_y = current_node / self.n
        node_y = int(node_y)
        node_x = current_node - (self.n * node_y) + 1

        goal_y = self.goal_node / self.n
        goal_y = int(goal_y)
        goal_x = self.goal_node - (self.n * goal_y) + 1

        ## solmujen x- ja y-koordinaattien etäisyys
        dx = abs(node_x - goal_x)
        dy = abs(node_y - goal_y)

        heurestic = min(dx, dy) * sqrt(2) + (max(dx, dy) - min(dx, dy))
        return heurestic
