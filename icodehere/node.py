from colors import *

class Node:
    def __init__(self, row, col, color, BLOCK_SIZE):
        self.row = row
        self.col = col
        self.color = color
        self.neighbors = []
        self.x = row * BLOCK_SIZE
        self.y = col * BLOCK_SIZE
        self.BLOCK_SIZE = BLOCK_SIZE

    def is_start_node(self):
        return self.color == PINK
    
    def is_end_node(self):
        return self.color == RED

    def is_barrier_node(self):
        return self.color == BLACK

    def make_start_node(self):
        self.color = PINK
    
    def make_end_node(self):
        self.color = RED
    
    def make_barrier_node(self):
        self.color = BLACK
    
    def reset_node(self):
        self.color = WHITE

    def draw_block(self, pygame):
        return pygame.Rect(self.col * self.BLOCK_SIZE, self.row * self.BLOCK_SIZE, self.BLOCK_SIZE, self.BLOCK_SIZE)

    def get_color(self):
        return self.color
    
    def set_color(self, value):
        self.color = value