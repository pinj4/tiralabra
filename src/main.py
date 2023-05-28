import graph
import dijkstra

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

if __name__ == "__main__":
    main(4)
    main(8)


