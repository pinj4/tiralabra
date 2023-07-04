from math import inf
import map_file
import dijkstra
import ida_star


def main():
    import time
    while True:
        choose_map = input("Choose map 1-5 or type q to quit: ")
        if choose_map =="q":
            print("goodbye")
            break
        elif choose_map not in ["1", "2", "3", "4", "5"]:
            print("choose a number between 1-5")
            continue
        m = map_file.Map(f"map_{choose_map}.map")

        graph = m.get_graph()
        m.print_map()
        map_width = m.map_width

        start_y = input(f"Choose a row for the starting point from 1-{map_width}: ")
        if start_y == "q":
            print("goodbye")
            break

        if int(start_y) not in range(1, map_width+1):
            print("row is out of range")
            continue

        nodes = m.get_available_nodes_from_row(int(start_y))
        if nodes == []:
            print("no available nodes")
            continue

        start_node = input(f"Choose an available node from row {start_y}: {nodes}: ")
        if start_node == "q":
            print("goodbye")
            break

        if int(start_node) not in nodes:
            print("node is unavailable")
            continue

        goal_y = input(f"Choose a row for the goal point from 1-{map_width}: ")
        if goal_y == "q":
            print("goodbye")
            break
        if int(goal_y) not in range(1, map_width+1):
            print("row is out of range")
            continue
        nodes = m.get_available_nodes_from_row(int(goal_y))
        if nodes == []:
            print("no available nodes")
            continue

        goal_node = input(f"Choose available node from row {goal_y}: {nodes}: ")
        if goal_node == "q":
            print("goodbye")
            break
        if int(goal_node) not in nodes:
            print("node is unavailable")
            continue

        if start_node == goal_node and start_y == goal_y:
            print("Choose different points")
            continue
        print(f"\nstart node: [row {start_y}, node {start_node}] end node: [row {goal_y}, node {goal_node}]\n")

        start_node = ((int(start_y)-1) * m.map_width) + (int(start_node)-1)
        goal_node = ((int(goal_y)-1) * m.map_width) + (int(goal_node)-1)


        d = dijkstra.Dijkstra(graph, m.map_width, int(start_node), int(goal_node))
        d_t1 = time.time()
        d_result = d.dijkstra()
        d_t2 = time.time()
        d_time = d_t2 - d_t1
        d_path = d.get_path()


        IDA = ida_star.IdaStar(graph, int(start_node), int(goal_node), m.map_width)
        i_t1 = time.time()
        i_result, i_path = IDA.ida_star()
        i_t2 = time.time()
        i_time = i_t2- i_t1

        if i_result != inf or d_result != inf:

            d_updated_map = m.update_map(d_path)
            d_map = m.get_updated(d_updated_map)

            i_updated_map = m.update_map(i_path)
            i_map = m.get_updated(i_updated_map)

            m.print_labels()
            m.print_maps(d_map, i_map)

            print("\nDijkstra \nshortest route: ", round(float(d_result), 3), "\nTime spent: ", round(d_time, 10), "seconds")

            print("\nIDA* \nshortest route ", round(i_result, 3), "\nTime spent: ", round(i_time, 10),"seconds\n")


        else:
            print("\nDijkstra \nno route \nTime spent: ", round(d_time, 10), "seconds")
            print("\nIDA* \nno route \nTime spent: ", round(i_time, 10), "seconds\n")

        if d_time < i_time:
            print("\nDijkstra took ", round((i_time-d_time), 10), "seconds less than IDA*-algorithm")
        elif i_time < d_time:
            print("\nIDA* took ", round((d_time - i_time), 10), "seconds less than Dijsktra's algorithm")
        elif i_time == d_time:
            print("\nDijkstra and IDA* algorithms spent the same amount of time")

        if round(i_result, 3) == round(float(d_result), 3) and i_result != inf:
            print("Both algorithms found equally short routes\n")
        elif round(float(d_result), 3) < round(i_result, 3) and d_result != inf:
            print("Dijkstra found a shorter route than IDA*\n")
        elif round(i_result, 3) < round(float(d_result), 3) and i_result != inf:
            print("IDA* found a shorter route than Dijsktra\n")
        else:
            print("\n")



if __name__ == "__main__":
    main()
