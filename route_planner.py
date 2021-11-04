import numpy as np
import math



def obstacle_list(map_grid):
    ### This function is used to find the list of starting point ###
    map_x = len(map_grid)
    map_y = len(map_grid[0])
    list = []
    for i in range(map_x):
        for j in range(map_y):
            if map_grid[i, j] == 3:
                list.append([i, j])
    return list

def utility(distance):
    ### This function defines the cost function of obstacles ###
    rmax = 4
    if distance < rmax:
        cost_obstacle = math.exp(1/(distance**2-rmax**2))
    else:
        cost_obstacle =0
    return cost_obstacle

def distance(start, end):
    dis = math.sqrt((start[0]-end[0])**2+(start[1]-end[1])**2)
    return dis

def cost_function(start, end, map_grid):
    cost_distance = distance(start, end)
    list = obstacle_list(map_grid)
    cost_obstacle = 0
    for obstacle in list:
        cost_obstacle += utility(distance(start, obstacle))
    cost = cost_distance + 0.2*cost_obstacle
    return cost

class Planner(object):
    """
    Creat a route planner
    """

    def __init__(self):
        """
        Initialization
        """
        # self.g = 0
        self.start = np.array([5, 2])  # start point
        self.goal = np.array([15, 15])  # end point
        self.open = np.array([[], [], [], [], [], []])  # start an empty open list
        self.closed = np.array([[], [], [], [], [], []])  # start an empty close list
        self.best_path_array = np.array([[], []])  # list of path
    def open_list(self, map_grid):
    ### This function is used to find the list of starting point###
        map_x = len(map_grid)
        map_y = len(map_grid[0])
        list = []
        for i in range(map_x):
            for j in range(map_y):
                if map_grid[i,j]==2:
                    list.append([i,j])
        return list


    def find_min(self, map_grid, x, target):
    ### This function is used to find the neighbors with the minimum costs###
        min =1000
        min_point = [0,0]
        for j in range(-1, 2, 1):
            for q in range(-1, 2, 1):
                target_list =[]
                #if j == 0 and q == 0:  # delete father node
                #    continue
                if (x[0] + j) < len(map_grid) and (x[1] + q)< len(map_grid[0]):
                    m = [x[0] + j, x[1] + q]
                    # print(m)
                    if m[0] < 0 or m[0] > len(map_grid) or m[1] < 0 or m[1] > len(
                            map_grid[0]):  # If the position is out of boundary, delete it.
                        continue

                    if map_grid[int(m[0]), int(m[1])] == 3:  # If obstacles are found, delete it.
                        continue

                    if map_grid[int(m[0]), int(m[1])] == 2:  # If other pedestrians are found, delete it.
                        continue

                    if cost_function(m, target, map_grid) < min:
                        min = cost_function(m, target, map_grid)
                        min_point = m

    def find_dijkmin(self, map_grid, field, x):
    ### This function is used to find the neighbors with the minimum costs###
        min =1000
        min_point = [0,0]
        for j in range(-1, 2, 1):
            for q in range(-1, 2, 1):
                target_list =[]
                #if j == 0 and q == 0:  # delete father node
                #    continue
                if (x[0] + j) < len(map_grid) and (x[1] + q)< len(map_grid[0]):
                    m = [x[0] + j, x[1] + q]
                    # print(m)
                    if m[0] < 0 or m[0] > len(map_grid) or m[1] < 0 or m[1] > len(
                            map_grid[0]):  # If the position is out of boundary, delete it.
                        continue

                    if map_grid[int(m[0]), int(m[1])] == 3:  # If obstacles are found, delete it.
                        continue

                    if map_grid[int(m[0]), int(m[1])] == 2:  # If other pedestrians are found, delete it.
                        continue

                    if field[m[0],m[1]] < min:
                        min = field[m[0],m[1]]
                        min_point = m
        return min_point

class Planner_circle(object):
    """
    Creat a route planner
    """

    def __init__(self):
        """
        Initialization
        """
        # self.g = 0
        self.start = np.array([5, 2])  # start point
        self.goal = np.array([15, 15])  # end point
        self.open = np.array([[], [], [], [], [], []])  # start an empty open list
        self.closed = np.array([[], [], [], [], [], []])  # start an empty close list
        self.best_path_array = np.array([[], []])  # list of path
    def open_list(self, map_grid):
    ### This function is used to find the list of starting point###
        map_x = len(map_grid)
        map_y = len(map_grid[0])
        list = []
        for i in range(map_x):
            for j in range(map_y):
                if map_grid[i,j]==2:
                    list.append([i,j])
        return list
