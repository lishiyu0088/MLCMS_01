import numpy as np
import math
import matplotlib.pyplot as plt

##This file defines Dijkstra algorithm.##

def find_target(map_grid):
    ## This function returns target coordinates##
    target = np.where(map_grid == 4)
    return target

def dijstra_field(map_grid):
    ## This function returns costs of each grid point according to Dijkstra algorithm##
    target = find_target(map_grid)
    m_y = len(map_grid)
    m_x = len(map_grid[0])
    cost_max = m_x*m_y
    cost = 0
    cost_field = np.full((len(map_grid), len(map_grid[0])), int(cost_max), dtype=np.int8)
    cost_field[target[0], target[1]] = cost
    list =[]
    start_list = []
    start_list.append(target)
    list.append(target)
    while len(start_list)!=0:
        for element in start_list:
            for j in range(-1, 2, 1):
                for q in range(-1, 2, 1):
                    m = [element[0] + j, element[1] + q]
                    if m[0] < 0 or m[0] > (len(map_grid)-1) or m[1] < 0 or m[1] > (len(map_grid[0])-1):  # If the position is out of boundary, delete it.
                        continue
                    if map_grid[m[0], m[1]] == 3:  # If obstacles are found, delete it.
                        cost_field[m[0], m[1]] = cost_max
                        continue
                    if j==0 and q==0:
                        continue
                    if list.count(m)==0:
                        start_list.append(m)
                        list.append(m)
                    cost = abs(j)+abs(q)+cost_field[element[0],element[1]]
                    if cost<cost_field[m[0],m[1]]:
                        cost_field[m[0],m[1]] =cost
            start_list.remove(element) # delete father node
    return cost_field, cost

'''
map_grid = np.loadtxt("./data/bottleneck.txt")
m_y = len(map_grid)
m_x = len(map_grid[0])
cost_max = m_x*m_y
field, cost=dijstra_field(map_grid)
plt.imshow(field, cmap=plt.cm.hot, interpolation='nearest', vmin=0, vmax=cost)
plt.show()
'''