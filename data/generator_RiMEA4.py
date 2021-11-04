import numpy
from random import randint

# Initialization
# 1 stands for empty state
# 2 stands for pedestrain
# 3 stands for obstacle
# 4 stands for target
map_x = 52
map_y = 27
map_grid = numpy.full((map_x, map_y), int(1), dtype=numpy.int8)
w=20
h=10
width = int(w * 2.5)
height = int(h * 2.5)

coordinates = set()
density = 0.2

while len(coordinates) <= w * h * density:
    x, y = randint(1, width), randint(1, height)
    if (x != 50) and (y != 25):
        coordinates.add((x, y))

for i in range(width + 2):
    map_grid[i,0]= 3

for i in range(height):
    map_grid[0, i+1] = 3

for i in range(width + 2):
    map_grid[i, height + 1] = 3

for i in range(height):
    map_grid[width+1, i + 1] = 3

for c in coordinates:
    map_grid[c[0], c[1]] = 2


map_grid[width,int(height / 2)]=4

numpy.savetxt("../data/rimea4.txt", map_grid, fmt=' '.join(['%i'] *map_y))