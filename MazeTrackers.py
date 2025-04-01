#Generate maze, what is a wall? where can I go?
#generate image using matplotlib
#2D array
#get through the maze (hug right wall)
#solver
#check surroundings (options, what is empty above, below, left, right), find possible movement locations, if right, go forward
#right is relative to robot
#if can't go right, just turn whatever possible.
#hug the right wall for movement.
#check, if it can't solve it, say "sorry! can't solve it"

#solver, plotter, maze generator
import matplotlib.pyplot as plt
import numpy as np
import random

NORTH = [0,-1]
SOUTH = [0,1]
EAST = [1,0]
WEST = [-1,0]

class Maze:
    #initialize the same maze, 4x4 in init via 2D array
    #Player class
    #check surroundings, store direction
    #let #2 = answer
    #check if you are top right down bot,
    def __init__(self, height, width):
        #create the maze
        #maybe have an AI model do the importing?
        #Looked into something called DFS-based maze generation;
        # honestly don't understand it, hard coded for now;
        # figure out how to auto generate and check if it's possible
        self.maze = self.gen_maze(height, width)
        #instantiate start position

    def get_maze(self):
        return self.maze

    #prints maze. position is player position
    def print_maze(self, position):
        maze_array = np.array(self.maze)
        rows, cols = maze_array.shape
        x, y = position
        #imshow takes in:
            # X: data of image (in form of array)
            # cmap: color map, maps values (0, 1, 2) to colors
        plt.imshow(maze_array, cmap='Greys')
        plt.xticks(np.arange(rows), np.arange(rows))
        plt.yticks(np.arange(cols), np.arange(cols))
        #plot player
        plt.scatter(x, y, color='red')
        plt.show()

    #returns the tile at x (column number) and y (row number)
    def get_tile(self,x,y):
        return self.maze[y][x]

    def gen_maze(self, width = 20, height = 20):
        #generates empty maze with width as row length and height as # of rows
        maze = [[1] * (width + 1) for i in range(height + 1)]

        directions = [(2,0), (0,2), (-2,0), (0,-2)]
        def carve_path(y,x):
            maze[y][x] = 0 #current cell is a path
            random.shuffle(directions)
            #dx, dy refers to direction, nx, ny refers to new point (point that it's trying to go to)
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                #checks if the point it is trying to go to is a valid point in terms of dimensions
                #creates an outside layer that makes sure it's traversable.
                #also checks that the square is not already a path
                if 0 < nx < width and 0 < ny < height and maze[ny][nx] == 1:
                    #carve the space in between with an empty space
                    maze[y + dy//2][x + dx//2] = 0
                    #recursively call itself and keep going from that point
                    carve_path(ny, nx)
        carve_path(1,1)
        return maze

class Player:
    def __init__(self, maze):
        self.maze = maze
        self.position = [1,1]

    def get_position(self):
        return self.position

#direction refers (x,y)
#x col#
#y row#
    def check_direction(self, direction):
        x = self.position[0]
        y = self.position[1]
        if x + direction[0] > len(self.maze.get_maze()[y]) - 1 or x + direction[0] < 0:
            return False
        if y + direction[1] > len(self.maze.get_maze()) - 1 or y + direction[1] < 0:
            return False
        # if the east position is filled
        if self.maze.get_tile(x+direction[0],y+direction[1]) == 1:
            return False
        return True

    #when calling this method, need to make sure location is valid (equal to ==)
    # if so, move there. position is in row (top 0), col (left 0)
    def move(self, direction):
        if self.check_direction(direction):
            self.position[0] += direction[0]
            self.position[1] += direction[1]
            print(f"You moved to {self.position}")
            return True
        else:
            print("Sorry, that is not a valid location to move to.")
            return False



#height and width placeholder values. they don't do anything now
newMaze = Maze(10, 10)
tempMaze = newMaze.gen_maze(50,50)
Knight = Player(newMaze)
while True:
    choice = input("Where do you want to move: ")
    choice = choice.upper()
    match choice:
        case "WEST":
            direction = WEST
        case "EAST":
            direction = EAST
        case "NORTH":
            direction = NORTH
        case "SOUTH":
            direction = SOUTH
        case _:
            print("Sorry, please enter a valid direction")
            continue
    Knight.move(direction)
    newMaze.print_maze(Knight.get_position())