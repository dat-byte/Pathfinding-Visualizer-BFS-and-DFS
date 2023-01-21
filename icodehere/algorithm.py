import abc
from time import sleep
from colors import YELLOW, BLUE, GREEN

class PathFindingAlgorithm(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_path(self, grid, start, end, draw):
        """
        Find a path from the start node to the end node in a graph.

        Parameters:
            grid: 2D array of Node objects
            start_node (Node): Starting node.
            end_node (Node): Ending node.
            draw (lamda): draws ui updates to the screen
        """
        pass

    def update_node_neighbors(self, grid):
        """
        Updating the neighbors for each node because there may be some UI changes
        before starting the alogorithm

        Parameters:
            grid: 2D array of Node objects
        """
        for row in grid:
            for node in row:
                node.update_neighbors(grid)

    def show_path(self, path_mapper, current, start, draw):
        """
        Reconstructing path 

        Parameters:
            path_mapper (dict): dictionary of parent for each node
            current (Node): the end node, if found
            draw (lamda): draws ui updates to the screen
        """
        path = []
        while current != start:
            path.append(current)
            current = path_mapper[current]
        path.append(start)
        
        for node in path:
            node.change_color(YELLOW)
            draw()
            sleep(1)

class BFS(PathFindingAlgorithm):
    def find_path(self, grid, start, end, draw):
        super().update_node_neighbors(grid)

        path = {}
        queue = [start]

        while len(queue) > 0:
            current = queue.pop(0)

            if current != start: current.change_color(BLUE)
            if current == end: super().show_path(path, current, start, draw)
            
            neighbors = current.get_neighbors()
            for node in neighbors:
                if node.get_color() != BLUE:
                    path[node] = current
                    queue.append(node)
                    if node != start: node.change_color(GREEN)
        print('Done with BFS')

