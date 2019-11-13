from Queue import PriorityQueue

# Romania Map with the path cost.
Romania_Map = {\
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},\
            'Zerind': {'Arad': 75, 'Oradea': 71},\
            'Oradea': {'Zerind': 71, 'Sibiu': 151},\
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},\
            'Timisoara': {'Arad': 118, 'Lugoj': 111},\
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},\
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},\
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},\
            'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},\
            'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},\
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},\
            'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},\
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
            'Giurgiu': {'Bucharest': 90},\
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},\
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},\
            'Eforie': {'Hirsova': 86},\
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},\
            'Iasi': {'Vaslui': 92, 'Neamt': 87},\
            'Neamt': {'Iasi': 87}\
        }

# This function does the A* search.
def a_star(start_city, end_city):
    # Heuristc values as straight line distances.
    heuristics = {\
                        'Arad': 366,\
                        'Zerind': 374,\
                        'Oradea': 380,\
                        'Sibiu': 253,\
                        'Timisoara': 329,\
                        'Lugoj': 244,\
                        'Mehadia': 241,\
                        'Drobeta': 242,\
                        'Craiova': 160,\
                        'Rimnicu': 193,\
                        'Fagaras': 176,\
                        'Pitesti': 100,\
                        'Bucharest': 0,\
                        'Giurgiu': 77,\
                        'Urziceni': 80,\
                        'Hirsova': 151,\
                        'Eforie': 161,\
                        'Vaslui': 199,\
                        'Iasi': 226,\
                        'Neamt': 234\
                    }

    # Create instances of PriorityQueue
    frontier, marked = PriorityQueue(), {}

    # Store the straight line distance values inside the priority queue
    frontier.put((heuristics[start_city], 0, start_city, [start_city]))

    # Set marked city's straight line distances
    marked[start_city] = heuristics[start_city]
    while not frontier.empty():

        # Get the heuristic , initial cost , straight line distance , path cost values from priority queue.
        (h, cost, v, path) = frontier.get()

        # If reached return cost.
        if v == end_city:
            return h, cost, path

        # Expand a city's neighbors
        for neighbor in Romania_Map[v].keys():

            #Calculate cost of current city so far.
            cost_from_start = cost + Romania_Map[v][neighbor]

            # updates the h value
            h = cost_from_start + heuristics[neighbor]

            # include unmarked neighbors.
            if not neighbor in marked or marked[neighbor] >= h:
                marked[neighbor] = h

                # Store the new neighbor values in the queue.
                frontier.put((h, cost_from_start, neighbor, path + [neighbor]))

def main():
    print('start_city : Lugoj')

    # start city = Lugoj
    start_city = 'Lugoj'
    print('end_city : BUCHAREST')

    # end city = Bucharest
    end_city = 'Bucharest'

    # If the city does not exist return error.
    if start_city not in Romania_Map or end_city not in Romania_Map:
        print('ERROR: CITY DOES NOT EXIST.')
    else:

        # Calculate the path cost from Lugoj to Bucharest.
        h, cost, short_path = a_star(start_city, end_city)

        # Prints the path cost.
        print('PATH COST = ', cost)

        # Prints the shortest path from Lugoj to Bucharest
        print(' -> '.join(city for city in short_path))

if __name__ == '__main__':
    main()