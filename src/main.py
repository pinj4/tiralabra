from math import inf
import map_file
import dijkstra
import ida_star


def main():
    import time
    while True:
        choose_map = input("Choose map 1-4 or type q to quit: ")
        if choose_map == "q":
            print("goodbye")
            break
        elif choose_map not in ["1", "2", "3", "4"]:
            print("choose a number between 1-4")
            break
        m = map_file.Map(f"map_{choose_map}.map")

        graph = m.get_graph()
        m.print_map()
        map_width = m.map_width

        start_y = input(f"Choose a row for the starting point from 1-{map_width}: ")
        if int(start_y) not in range(1, map_width+1):
            print("that row is out of range")
            break 
        nodes = m.get_available_nodes_from_row(int(start_y))

        start_node = input(f"Choose an available node from row {start_y}: {nodes}: ")
        if int(start_node) not in nodes:
            print("that node is unavailable")
            break
        
        goal_y = input(f"Choose a row for the goal point from 1-{map_width}: ")
        if int(goal_y) not in range(1, map_width+1):
            print("that row is out of range")
            break 
        nodes = m.get_available_nodes_from_row(int(goal_y))

        goal_node = input(f"Choose available node from row {goal_y}: {nodes}: ")
        if int(goal_node) not in nodes:
            print("that node is unavailable")
            break

        if start_node == goal_node:
            print("Choose different points")
            break
        
        
        print("start node: ", start_node, " end node: ", goal_node)


        d = dijkstra.Dijkstra(graph, m.map_width, int(start_node), int(goal_node))
        d_t1 = time.time()
        d_result = d.dijkstra()
        d_t2 = time.time()
        d_time = d_t2 - d_t1

        if d_result != inf:
            print("\nDijkstra \nshortest route: ", d_result, "\nTime spent: ", d_time)
            d_path = d.get_path()
        else:
            print("\nDijkstra \nno route \nTime spent: ", d_time)

        IDA = ida_star.IdaStar(graph, int(start_node), int(goal_node), m.map_width)
        i_t1 = time.time()
        i_result, i_path = IDA.ida_star()
        i_t2 = time.time()
        i_time = i_t2- i_t1 

        if i_result != inf:
            print("\nIDA* \nshortest route ", i_result, "\nTime spent: ", i_time, "\n")
            d_updated_map = m.update_map(d_path)
            print("\nDijsktra map: ") 
            m.print_updated(d_updated_map)

            i_updated_map = m.update_map(i_path)
            print("\nIDA* map: ") 
            m.print_updated(i_updated_map)
            #print("\n IDA* path ", i_path)
            #print("\n Dijkstra path ", d_path)

        else:
            print("\nIDA* \nno route \nTime spent: ", i_time, "\n")


if __name__ == "__main__":
    main()
