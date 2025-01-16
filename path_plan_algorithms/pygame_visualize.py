import pygame  # 2D Graphics module for visualization

# Size of pygame 2D window
WIDTH = 800
HEIGHT = 800

# Defining variable for 2D pygame window
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Setting caption for the pygame window
pygame.display.set_caption("Path Finding Algorithm")

# Defining different color variables in RGB format
RED = (255, 0, 0)           # Visited nodes
GREEN = (0, 255, 0)         # nodes in the open set (neighbors of current node) or possible next nodes to visit
BLUE = (0, 0, 255)          # Optional: could be used for other purposes
WHITE = (255, 255, 255)     # Default color for unexplored/unvisited nodes
BLACK = (0, 0, 0)           # Barrier nodes
ORANGE = (255, 165, 0)      # Start node
PURPLE = (128, 0, 128)      # Path from start to end node
GREY = (128, 128, 128)      # Grid lines color
TURQUOISE = (64, 224, 208)  # End node

class SpotNode:
    """Class representing each node in the grid as a spot(a box)."""
    
    def __init__(self, row, col, width, height, total_rows, total_cols):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * height
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.height = height
        self.total_rows = total_rows
        self.total_cols = total_cols

    def get_pos(self):
        """Return the position of the node."""
        return self.row, self.col

    def is_closed(self):
        """Check if the node has been visited."""
        return self.color == RED
    
    def is_open(self):
        """Check if the node is in the open set."""
        return self.color == GREEN
    
    def is_path(self):
        """Check if the node is part of previously calculated path(using some other algo)"""
        return self.color == PURPLE

    def is_barrier(self):
        """Check if the node is a barrier."""
        return self.color == BLACK
    
    def is_start(self):
        """Check if the node is a start node."""
        return self.color == ORANGE
    
    def is_end(self):
        """Check if the node is an end node."""
        return self.color == TURQUOISE
    
    def reset(self):
        """Reset the color of the node to white."""
        self.color = WHITE

    def set_closed(self):
        """Set the node as closed (visited)."""
        self.color = RED

    def set_open(self):
        """Set the node as open (part of current exploration)."""
        self.color = GREEN

    def put_barrier(self):
        """Set the node as a barrier."""
        self.color = BLACK

    def put_start(self):
        """Set the node as the start point."""
        self.color = ORANGE

    def put_end(self):
        """Set the node as the end point."""
        self.color = TURQUOISE

    def set_path(self):
        """Set the node as part of the path from start to end."""
        self.color = PURPLE

    def draw(self):
        """Draw the node on the screen."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_neighbors(self, grid):
        """Update neighbors of this node. Neighbors are added only if they are not barriers and within grid boundaries."""
        
        # Checking right neighbor
        if self.col < (self.total_cols - 1) and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Checking left neighbor 
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

        # Checking up neighbor 
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Checking down neighbor 
        if self.row < (self.total_rows - 1) and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

    def __lt__(self, other):
        return False

def make_grid(rows, cols, width, height):
    """Create a grid of SpotNodes."""
    grid = []
    row_size = height // rows
    col_size = width // cols

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            node = SpotNode(i, j, col_size, row_size, rows, cols)
            grid[i].append(node)

    return grid

def draw_grid(win, rows, cols, width, height):
    """Draws a grid on top of nodes to visualize structure."""
    row_size = height // rows
    col_size = width // cols

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * row_size), (width, i * row_size))
    
    for j in range(cols):
        pygame.draw.line(win, GREY, (j * col_size, 0), (j * col_size, height))

def draw(win, grid, rows, cols, width, height):
    """Draw everything related to grid on pygame window."""
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw()
    
    draw_grid(win, rows, cols, width, height)
    pygame.display.update()

def get_clicked_pos(mouse_pos, rows, cols, width, height):
    """Get position of mouse click in terms of row/col index."""
    row_size = height // rows
    col_size = width // cols
    y_pos, x_pos = mouse_pos

    row_index = y_pos // row_size
    col_index = x_pos // col_size
    return row_index, col_index
