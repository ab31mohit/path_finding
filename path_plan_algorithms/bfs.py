from collections import deque  # Implement queue using deque
from path_plan_algorithms.pygame_visualize import *

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
Implementing Breadth-First Search (BFS) algorithm.
Here 'draw' is the function that we are passing as an argument to the algorithm function
"""
def BfsAlgorithm(draw, start, end):
    queue = deque([start])  # Initialize deque with the start node
    came_from = {}          # To reconstruct path
    visited = set([start])  # To track visited nodes

    found_goal = False
    while queue:  # Keep running while the queue is not empty
        # Allow user to stop the algo in between
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_node = queue.popleft()  # Get the first node added from the queue (FIFO)

        if current_node == end:  # Path is found
            reconstruct_path(came_from, end, draw)
            end.put_end()
            found_goal = True
            break

        # Consider neighbors for next nodes in search
        for neighbor in current_node.neighbors:
            if neighbor not in visited:  # Avoid revisiting
                visited.add(neighbor)  # Mark neighbor as visited
                came_from[neighbor] = current_node  # Track how we got to this neighbor
                queue.append(neighbor)  # Add neighbor to queue
                neighbor.set_open()  # Visualize open set of nodes (neighbors of current node)

        draw()  # Update visualization

        if current_node != start:
            current_node.set_closed()  # Visualize closed set of nodes (already visited nodes)

    return found_goal

