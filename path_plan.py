
from path_plan_algorithms.pygame_visualize import *
from path_plan_algorithms.astar import *
from path_plan_algorithms.dijkstra import *
from path_plan_algorithms.bfs import *
from path_plan_algorithms.dfs import *

def main():

    # Set up the grid dimensions and window size
    rows = 50
    cols = 50
    width = WIDTH
    height = HEIGHT

    # Create a grid for visualization
    grid = make_grid(rows, cols, width, height)

    start = None
    end = None

    run = True

    msg = """
[Instructions!]
-----------------------------------------------------------------------
[Generating obstacles with start & end goal]:  (from Mouse)
    First left click --> start location.
    Second left click --> end goal.
    Subsequent left clicks at different positions on map --> onbtacles.

[Implementing path_planning]:   (from Keyboard)
    Press 'a' to solve using A* algorithm.
    Press 'b' to solve using BFS algorithm.
    Press 'd' to solve using DFS algorithm.
    Press 'j' to solve using Dijkstra's algorithm.

[Cleaning the grid]:    (from Keyboard)
    Press 'space' to clean path and solve using different algorithm.
    Press 'c' to clear everything from the grid.
    Press 'q' to quit the window and exit the program.
------------------------------------------------------------------------
    
"""
    print(msg)   # Print instructions for keybindings

    while run:
        draw(win, grid, rows, cols, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]:  # Left mouse click
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(mouse_pos, rows, cols, width, height)
                spot = grid[row][col]
                
                if not start and spot != end:
                    start = spot
                    start.put_start()
                
                elif not end and spot != start:
                    end = spot
                    end.put_end()

                elif spot != end and spot != start:
                    spot.put_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right mouse click
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(mouse_pos, rows, cols, width, height)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            """Check keybinding to do corresponding actions on the pygame window"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit the program
                    print("\n[key 'q' is pressed by the user]:\nQuiting the program!")
                    run = False
                
                elif event.key == pygame.K_a and start and end:  # A* Algorithm
                    print("\n[key 'a' is pressed by the user]:\nPlanning path using A* Algorithm!")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    AstarAlgorithm(lambda: draw(win, grid, rows, cols, width, height), grid, start, end)
                    

                elif event.key == pygame.K_b and start and end:  # BFS Algorithm
                    print("\n[key 'b' is pressed by the user]:\nPlanning path using BFS Algorithm!")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    BfsAlgorithm(lambda: draw(win, grid, rows, cols, width, height), start, end)

                elif event.key == pygame.K_d and start and end:  # DFS Algorithm
                    print("\n[key 'd' is pressed by the user]:\nPlanning path using DFS Algorithm!")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    DfsAlgorithm(lambda: draw(win, grid, rows, cols, width, height), start, end)

                elif event.key == pygame.K_j and start and end:  # Dijkstra's Algorithm
                    print("\n[key 'j' is pressed by the user]:\nPlanning path using Dijkstra Algorithm!")
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    DijkstraAlgorithm(lambda: draw(win, grid, rows, cols, width, height), grid, start, end)

                elif event.key == pygame.K_c:  # Clear all nodes
                    print("\n[key 'c' is pressed by the user]:\nResetting the entire pygame window!")
                    for row in grid:
                        for spot in row:
                            spot.reset()
                    start = None
                    end = None

                elif event.key == pygame.K_SPACE:  # Clean only red/green/path nodes
                    print("\n[key 'space' is pressed by the user]:\nClearing path to use other algorithm!")
                    for row in grid:
                        for spot in row:
                            if spot.is_closed() or spot.is_open() or spot.is_path():
                                spot.reset()  # Reset red/green/path nodes but keep barriers/start/end

    pygame.quit()

if __name__ == "__main__":
    main()
