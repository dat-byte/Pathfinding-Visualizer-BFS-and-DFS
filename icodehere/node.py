from colors import *

class Node:
    def __init__(self, row, col, color, BLOCK_SIZE, TOTAL):
        self.row = row                  # row in grid
        self.col = col                  # col in grid
        self.color = color              # color of node
        self.TOTAL = TOTAL              # total rows and cols
        self.neighbors = []             # neighbors of this node
        self.x = row * BLOCK_SIZE       # x coordinate in pygame    
        self.y = col * BLOCK_SIZE       # y coordinate in pygame
        self.BLOCK_SIZE = BLOCK_SIZE    # size of block on pygame

    def get_color(self):
        return self.color
    
    def get_position(self):
        return self.row, self.col

    def get_neighbors(self):
        return self.neighbors

    def change_color(self, color):
        """
        Changes the color of the node

        color: RGB tuple
        """
        self.color = color
    
    def draw(self, screen, pygame):
        """
        Draws rectangle/block on window screen at position (x,y) with a 
        width of BLOCK_SIZE

        screen: window screen
        pygame: instance of pygame
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.BLOCK_SIZE, self.BLOCK_SIZE) )

    def update_neighbors(self, grid):
        """
        Gets the neighbors for the "this" node class
        """
        self.neighbors = []
        vectors = [(-1, 0), (1, 0), (0, 1), (0, -1)]    # north, south, east, west of this node
        
        for x in range(4):
            rr = self.row + vectors[x][0]
            cc = self.col + vectors[x][1]

            if rr < 0 or cc < 0: continue
            if rr >= self.TOTAL or cc >= self.TOTAL: continue
            if grid[rr][cc].get_color() != BLACK: self.neighbors.append(grid[rr][cc])