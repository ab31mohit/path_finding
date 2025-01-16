from collections import deque  # Implement stack using deque
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
Implementing Depth First Search (DFS) algorithm.
Here 'draw' is the function that we are passing as an argument to the algorithm function
"""
def DfsAlgorithm(draw, start, end):
    stack = deque([start])  # Initialize deque with the start node
    came_from = {}          # To reconstruct path
    visited = set()         # To track visited nodes
    found_goal = False      # Flag to indicate if goal is found

    while stack:  # Keep running while the stack is not empty
        # Allow user to stop the algo in between
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current_node = stack.pop()  # Get the last node added from the stack (LIFO)

        if current_node in visited:
            continue  # Skip if already visited

        visited.add(current_node)  # Mark current node as visited

        if current_node == end:  # Path is found
            reconstruct_path(came_from, end, draw)
            end.put_end()
            found_goal = True  # Set flag indicating goal has been found
            break  # Exit loop since we found the goal

        # Consider neighbors for next nodes in search
        for neighbor in current_node.neighbors:
            if neighbor not in visited and neighbor not in stack:  # Avoid revisiting
                came_from[neighbor] = current_node
                stack.append(neighbor)  # Add neighbor to stack
                neighbor.set_open()  # Visualize open set of nodes (neighbors of current node)

        draw()  # Update visualization

        if current_node != start:
            current_node.set_closed()  # Visualize closed set of nodes (already visited nodes)

    return found_goal  # Return whether the goal was found

