from math import inf

class IdaStar:
    def __init__(self, graph):
        self.graph = graph
        self.goal_node = len(self.graph) - 1

    def ida_star(self, start):
        threshold = self.heuristics(start, self.goal_node) 
        path = [start]
        while True:
            temp = self.search(path, 0, threshold)
            if temp == "FOUND": 
                return len(path)
            if temp == inf: 
                return inf
            threshold = temp

    def search(self, path, distance, threshold):
        current_node = path[-1] 
        estimate = distance + self.heuristics(current_node, self.goal_node) 
        if estimate > threshold:
            return estimate
        if self.goal_node == current_node:
            return "FOUND"
        minim_weight = inf
        for child, weight in self.graph[current_node]:
            if child not in path:
                path.append(child)
                temp = self.search(path, distance + weight, threshold)
                if temp == "FOUND":
                    return "FOUND"
                elif temp < minim_weight:
                    minim_weight = temp
                path.pop()
        return minim_weight if minim_weight != inf else inf

    def heuristics(self, current_node, goal_node):
        return abs(current_node - goal_node)

