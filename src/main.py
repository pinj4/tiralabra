
#import time
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
        print(result, "Time spent: ", time)
    else:
        print("no route \nTime spent: ", time)

        #return d.dijkstra()

#m = Main()
main(4)
main(8)
#print(k)

#print("NEW")
#k2 = main(20)
#print(k2)

