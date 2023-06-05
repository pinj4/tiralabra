import map_file
import dijkstra
import time

def main(n):
    import time
    gr = graph.Graph(n)
    gr.generate_matrix()
    gr.print_graph()
    d = dijkstra.Dijkstra(gr.get_graph(), n)
    t1 = time.time()
    result = d.dijkstra()
    t2 = time.time()
    time = t2- t1 
    if result != 10**9:
        print("shortest route: ", result, "\nTime spent: ", time)
    else:
        print("no route \nTime spent: ", time)

def main2():
    import time
    m = map_file.Map("map_3.map")
    m.create_map()
    m.generate_graph()
    m.print_map()
    d = dijkstra.Dijkstra(m.get_graph(), m.map_width)
    t1 = time.time()
    result = d.dijkstra()
    t2 = time.time()
    time = t2- t1 
    if result != 10**9:
        print("shortest route: ", result, "\nTime spent: ", time, "LEN ", len(result))
    else:
        print("no route \nTime spent: ", time)






if __name__ == "__main__":
    #main(4)
    #main(8)
    main2()