import pygame
from grid import Grid
from node import Node
from colors import *

WINDOW_SIZE = 800
BLOCK_SIZE = 20

# set the total number of rows and cols for the grid using integer division
TOTAL_ROWS = WINDOW_SIZE // BLOCK_SIZE
TOTAL_COLS = WINDOW_SIZE // BLOCK_SIZE

# initialize the pygame
pygame.init()

# set the screen dimensions 
SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
SCREEN.fill(WHITE)


def main():
    grid = Grid(TOTAL_ROWS, TOTAL_COLS, BLOCK_SIZE, WINDOW_SIZE)
    grid.create_grid()

    running = True
    while running:
        grid.draw_grid(pygame, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:
                # get the mouse position 
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # calculate the grid cell coordinates 
                row = mouse_y // BLOCK_SIZE
                col = mouse_x // BLOCK_SIZE

                # turn the cell black
                grid.set_block_color(row, col)

            # RIGHT CLICK
            if pygame.mouse.get_pressed()[1]:
                # get the mouse position 
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # calculate the grid cell coordinates 
                row = mouse_y // BLOCK_SIZE
                col = mouse_x // BLOCK_SIZE

                # turn block to WHITE/empty space
                grid.node_reset(row, col)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    grid.create_grid()
                
    # Quit Pygame
    pygame.quit()

main()