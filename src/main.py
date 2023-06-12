from math import inf
import map_file
import dijkstra
import ida_star


def main():
    import time
    while True:
        choose_map = input("Choose map 1-7 or type q to quit: ")
        if choose_map == "q":
            print("goodbye")
            break
        elif choose_map not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("choose a number between 1-7")
            break
        ## ida*-algortimti toimii tällä hetkellä vasta kartoille 4 ja 6
        m = map_file.Map(f"map_{choose_map}.map")

        graph = m.get_graph()
        m.print_map()

        d = dijkstra.Dijkstra(graph, m.map_width)
        d_t1 = time.time()
        d_result = d.dijkstra()
        d_t2 = time.time()
        d_time = d_t2 - d_t1

        if d_result != inf:
            print("Dijkstra \nshortest route: ", d_result, "\nTime spent: ", d_time)
        else:
            print("Dijkstra \nno route \nTime spent: ", d_time)

        IDA = ida_star.IdaStar(graph)
        i_t1 = time.time()
        i_result = IDA.ida_star(m.map_width+1)
        i_t2 = time.time()
        i_time = i_t2- i_t1 

        if i_result != inf:
            print("IDA* \nsortest route ", i_result, "\nTime spent: ", i_time)
        else:
            print("IDA* \nno route \nTime spent: ", i_time)

if __name__ == "__main__":
    main()