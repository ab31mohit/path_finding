from queue import PriorityQueue  # for implementing priority queue
from path_plan_algorithms.pygame_visualize import *

"""
Backtracking the came_from set from end to start to construct the path from start to goal.
"""
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]  
        current.set_path()
        draw()
    current.put_start()


"""
Implementing Dijkstra's Algorithm.
Here 'draw' is the function that we are passing as an argument to the algorithm function.
"""
def DijkstraAlgorithm(draw, grid, start, end):
    # storing the neighbors of current node based on their distance from start
    open_set = PriorityQueue()

    """initializing g scores for all the nodes within the grid to 'inf' as we don't know how far every node is from the start node."""
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0  # Distance of start node from itself is 0

    open_set.put((0, start))  # Push the start node with distance(g_score) 0
    came_from = {}   # To reconstruct path
    visited = set()  # To track visited nodes
    found_goal = False

    while not open_set.empty():
        # Allow user to stop the algo in between
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_node = open_set.get()[1]  # Get the node with the lowest distance (or g_score)

        if current_node == end:  # Path is found
            reconstruct_path(came_from, end, draw)
            end.put_end()
            found_goal = True
            break

        visited.add(current_node)  # Mark current node as visited

        # Consider neighbors for next nodes in search
        for neighbor in current_node.neighbors:
            if neighbor in visited:
                continue  # Skip if already visited

            tentative_g_score = g_score[current_node] + 1  # Cost is assumed to be 1

            if tentative_g_score < g_score[neighbor]:  # Found a better path
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                open_set.put((g_score[neighbor], neighbor))  # Add neighbor with updated cost
                neighbor.set_open()  # Visualize open set of nodes (neighbors of current node)

        draw()  # Update visualization

        if current_node != start:
            current_node.set_closed()  # Visualize closed set of nodes (already visited nodes)

    return found_goal

