from queue import PriorityQueue      # module to implement priority queue
from path_plan_algorithms.pygame_visualize import *


"""
Heuristic function to determine approximate distance of current node from the goal node
"""
def h_score(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Approximating the distance as Manhatten distance
    return abs(x1 - x2) + abs(y1 - y2)


"""
Backtracking the came_from set from end to start to construct the path from start to goal
"""
def reconstruct_path(came_from, current, draw):

    while current in came_from:
        current = came_from[current]  
        current.set_path()
        draw()
    current.put_start()


"""
Implementing the A* (A-star) Algorithm.
Here 'draw' is the function that we are passing as an argument to the algorithm function
"""
def AstarAlgorithm(draw, grid, start, end):     
    # for storing the neighbours of current Node based on their cost (f_score)
    open_set = PriorityQueue()
    count = 0   # for storing the order in which a Node is added in the open_set
    
    """Initializing g scores for all the nodes within the grid to 'inf' as we don't know how far every node is from the start node."""
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0   # distance of start node from itself is 0 

    """Initializing f scores for all the nodes within the grid to 'inf' as we don't know what is the cost of going to goal node though all of those nodes."""
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h_score(start.get_pos(), end.get_pos())   # cost of going from start to end (which we want to minimize)

    open_set.put((0, count, start))   # Push the start node with cost (f_score) 0
    came_from = {}    # To reconstruct path

    """This set will be used to check if a node is present in the open_set or not. By default priority queue does not have the functionality to check if a node is present in queue or not, it only retuns node with smallest value of its elements. This open_set has will keep track of all the elements that are in the open set priority queue."""
    open_set_hash = {start}  
    found_goal = False
    
    while not open_set.empty():
        # to allow user to stop the algo in between
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # pops out the node with lowest value of F-score & if Fscore ties, then we look at the count variable
        current_node = open_set.get()[2]

        # similar to priority queue, we remove the current node to check for next nodes in the search
        open_set_hash.remove(current_node)

        if current_node == end:      # path is found
            reconstruct_path(came_from, end, draw)
            end.put_end()
            found_goal = True
            break

        # considering the neighbors for the next node in the search
        for neighbor in current_node.neighbors:
            temp_g_score = g_score[current_node] + 1

            # checking if there is a better node in the neighbours for the search with a smaller g_score
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h_score(neighbor.get_pos(), end.get_pos())    # f_score = g_score + h_score (for a particular node)

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.set_open()

        draw()

        if current_node != start:
            current_node.set_closed()

    return found_goal
