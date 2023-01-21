import pygame
from node import Node
from colors import *
from algorithm import BFS


WIDTH = 400
BLOCK_SIZE = 20
TOTAL_ROWS_COLS = WIDTH // BLOCK_SIZE
SCREEN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption  ("Uninformed Pathfinding Algorithms")
pygame.init()


def make_grid():
    """
    Creates a 2D grid of Node objects

    returns: list of Node objects
    """
    return [[Node(row, col, WHITE, BLOCK_SIZE, TOTAL_ROWS_COLS) for col in range(TOTAL_ROWS_COLS)] for row in range(TOTAL_ROWS_COLS)]


def draw(grid):
    """
    Draws node onto screen
    """
    for row in grid:
        for node in row:
            node.draw(SCREEN, pygame)

    draw_grid_lines()
    pygame.display.update()


def draw_grid_lines():
    """
    Draws horizontal and vertical grid lines.
    """
    for i in range(TOTAL_ROWS_COLS):
        pygame.draw.line(SCREEN, BLACK, (0, i * BLOCK_SIZE), (WIDTH, i * BLOCK_SIZE))   # HORIZONTAL LINE
        pygame.draw.line(SCREEN, BLACK, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, WIDTH))   # VERTICAL LINE


def mouse_clicked_position(position):
    """
    Gets the positon of the mouse event clicked

    position: is a tuple of (x,y) coordinates related to pygame
    """
    mouse_x, mouse_y = position

    row = mouse_x // BLOCK_SIZE
    col = mouse_y // BLOCK_SIZE

    return row, col


def main():
    grid = make_grid()
    start = None
    end = None

    running = True
    while running:
        draw(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:
                row, col = mouse_clicked_position(pygame.mouse.get_pos())
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.change_color(PINK)

                elif not end and node != start:
                    end = node
                    end.change_color(RED)

                elif node != start and node != end:
                    node.change_color(BLACK)

            # RIGHT CLICK
            if pygame.mouse.get_pressed()[1]:
                print('right mouse clicked')
                row, col = mouse_clicked_position(pygame.mouse.get_pos())
                node = grid[row][col]
                node.change_color(WHITE)
                            
                if node == start:
                    start = None

                elif node == end:
                    end = None
                    
            # KEYBOARD EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    print('Executing BFS algo')
                    algo = BFS()
                    algo.find_path(grid, start, end, lambda: draw(grid))

                if event.key == pygame.K_c:
                    start = None
                    end = None 
                    grid = make_grid()
    pygame.quit()


main()