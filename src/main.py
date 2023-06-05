import map_file
import dijkstra
from math import inf

def main():
    import time
    m = map_file.Map("map_1.map")
    m.create_map()
    m.generate_graph()
    m.print_map()
    d = dijkstra.Dijkstra(m.get_graph(), m.map_width)
    t1 = time.time()
    result = d.dijkstra()
    t2 = time.time()
    time = t2- t1 
    if result != inf:
        print("shortest route: ", result, "\nTime spent: ", time)
    else:
        print("no route \nTime spent: ", time)

if __name__ == "__main__":
    main()