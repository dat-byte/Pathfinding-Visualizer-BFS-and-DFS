from node import Node
from colors import *


class Grid:
    def __init__(self,TOTAL_ROWS, TOTAL_COLS, BLOCK_SIZE, WINDOW_SIZE):
        self.grid = []
        self._start_node = None
        self._end_node = None
        self._TOTAL_ROWS = TOTAL_ROWS
        self._TOTAL_COLS = TOTAL_COLS
        self._BLOCK_SIZE = BLOCK_SIZE
        self._WINDOW_SIZE = WINDOW_SIZE
    

    def get_grid(self):
        return self.grid
    

    def get_node(self, row, col):
        return self.grid[row][col]

    
    def create_grid(self):
        """
        Creates a 2D array of Node objects with WHITE as its color for all blocks
        """
        self.start_node = None
        self.end_node = None
        self.grid = [[Node(row, col, WHITE, self._BLOCK_SIZE) for col in range(self._TOTAL_COLS)] for row in range(self._TOTAL_ROWS)]

    
    def draw_grid(self, pygame, SCREEN):
        """
        Draws a grid that the user sees within the window

        pygame: pygame instance
        SCREEN: pygame screen that the user sees
        """
        for row in range(self._TOTAL_ROWS):
            for col in range(self._TOTAL_COLS):
                node = self.grid[row][col]
                pygame.draw.rect(SCREEN, node.get_color(), node.draw_block(pygame), 0)

        self.draw_grid_lines(pygame, SCREEN)

        # Update the display
        pygame.display.update()


    def draw_grid_lines(self, pygame, SCREEN):
        """
        Draws the grid lines of the grid 

        pygame: pygame instance
        SCREEN: pygame screen that the user sees
        """
        for i in range(self._TOTAL_ROWS):
            pygame.draw.line(SCREEN, BLACK, (0, i * self._BLOCK_SIZE), (self._WINDOW_SIZE, i * self._BLOCK_SIZE))
            for j in range(self._TOTAL_COLS):
                pygame.draw.line(SCREEN, BLACK, (j * self._BLOCK_SIZE, 0), (j * self._BLOCK_SIZE, self._WINDOW_SIZE))


    def set_block_color(self, row, col):
        """
        Update the node color of the block at ("row", "col") =  "color"

        row: row to update (int)
        col: col to update (int)s
        """
        node = self.grid[row][col]

        if not self._start_node and node != self._end_node:
            self._start_node = node
            self._start_node.make_start_node()
                
        elif not self._end_node and node != self._start_node:
            self._end_node = node
            self._end_node.make_end_node()
                
        elif node != self._start_node and node != self._end_node:
            node.make_barrier_node()

    
    def node_reset(self, row, col):
        """
        Resetting a node to an empty/free space

        row: row to update (int)
        col: col to update (int)
        """
        node = self.grid[row][col]

        node.reset_node()
        if node == self._start_node:
            self._start_node = None
        elif node == self._end_node:
            self._end_node = None