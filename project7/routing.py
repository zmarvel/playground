import os, string, sys

import copy
from Queue import Queue
from collections import deque, defaultdict
from math import sqrt
from random import shuffle

# appends padding spaces if the number is smaller than the largest value
# e.g. if the largest val=1245, 1 will be represented as '1   '
def format_num(n, maxSpaces):
    strNum = str(n)
    return strNum + ' ' * (maxSpaces - len(strNum))

# Just a wrapper over python dict to preserve things
# like height, width; also a pretty printing function provided
class Grid:
    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.d = d
    
    # pretty print the grid using the number formatter
    def pretty_print_grid(self):
        nSpaces = len(str(max(self.d.values())))
        strDelim = '|' + ('-' + (nSpaces * ' ')) * self.width + '|'
        print strDelim
        for y in range(self.height):
            print '|' + ' '.join([format_num(self.d[(x, y)], nSpaces) for x in range(self.width)]) + '|'
        print strDelim


# The grid is basically a dictionary. We can treat this as a graph where each node has 4 neighbors.
# Each neighbor contributes an in-edge as well as an out-edge.
# You might want to use this to construct you solution
class Graph:
    def __init__(self, grid):
        self.grid = grid
    
    def vertices(self):
        return self.grid.d.keys()

    def num_vertices(self):
        return len(self.vertices())

    def adj(self, (x, y)):
        return [u for u in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if u in self.grid.d.keys()]

    def check_path(self, path, s, t):
        for point in path:
            val = self.getVal(point)
            if val == -2 or val == -1:
                return False
            elif val != 0:
                if point != s and point != t:
                    return False
        return True

    def put_path(self, path, source, target):
        for point in path:
            if point != source and point != target:
                self.putVal(point, -2)
    
    def remove_path(self, path):
        for point in path:
            if self.getVal(point) == -2:
                self.putVal(point, 0)

    def remove_paths(self):
        for v in self.vertices():
            if self.getVal(v) == -2:
                self.putVal(v, 0)

    # put the value val for vertex u
    def putVal(self, u, val):
        self.grid.d[u] = val
    
    def getVal(self, u):
        return self.grid.d[u]

def eucl_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def bfs(g, source, target):
    queue = deque([source])
    parents = {v: None for v in g.vertices()}
    parents[source] = source
    if source == target:
        return parents
    while len(queue) != 0:
        u = queue.popleft()
        for t in sorted(g.adj(u), key=lambda p: eucl_dist(p, target)):
            if not parents[t]:
                if g.getVal(t) == 0:
                    parents[t] = u
                    queue.append(t)
                if target == t:
                    parents[t] = u
                    return parents
    if not parents[target]:
        print('Unable to find the target.')
        return None
    #raise Exception("No path found.")

def traceback(g, t, parents):
    path = []
    path.append(t)
    t = parents[t]
    while parents[t] != t:
        path.append(t)
        t = parents[t]
    return path

# Takes the grid and the points as arguments and returns a list of paths
# The grid represents the entire chip
# Each path represents the wire used to connect components represented by points
# Each path connects a pair of points in the points array; avoiding obstacles and other paths
# while minimizing the total path length required to connect all points
# If the points cannot be connected the function returns None
def find_paths(grid, points):
    graph = Graph(grid)
    paths = []
    queue = deque(points)
    passed = []
    failed = defaultdict(lambda: 0)
    #removed = [] # removed stack
    removed = Queue() # queue

    while queue:
        p = queue.popleft()
        s, t = p
        print(p)
    
        replaced = []
        while not removed.empty():
            r_p = removed.get()
            r_s, r_t = r_p
            r_parents = bfs(graph, r_s, r_t)
            if r_parents:
                r_path = traceback(graph, r_t, r_parents)
                replaced.append((r_p, r_path))
                graph.put_path(r_path, r_s, r_t)
            else:
                removed.put(r_p)
                for p, path in replaced:
                    graph.remove_path(path)
                    removed.put(p)
                last_path = paths.pop()
                last_p = passed.pop()
                graph.remove_path(last_path)
                removed.put(last_p)
                print(u'Backing up... removed {} paths.'.format(removed.qsize()))
                continue
        if not removed.empty(): continue
                
        parents = bfs(graph, s, t)
        
        if not parents:
            last_path = paths.pop()
            last_pair = passed.pop()
            graph.remove_path(last_path)

            # store the paths we've removed so we can try to avoid computing
            # them again, if they work still
            #removed.append((last_pair, last_path)) # stack
            removed.put(p)
            removed.put(last_pair) # queue

            print(u'Backing up... removed {} paths.'.format(removed.qsize()))

            failed[p] += 1

            # put the point back to its first in line place so we can try again
            #queue.appendleft(p)

            # if we've removed every other path and it still isn't working
            if failed[p] > graph.num_vertices():
                return None
            continue
                    
        # if we failed to find a path previously but we've found one now, reset
        # the counter for how many times it has failed.

        #print(path)
        path = traceback(graph, t, parents)
        graph.put_path(path, s, t)
        passed.append(p)
        paths.append(path)
    return paths

# check that the paths do not cross each other, or the obstacles; returns False if any path does so
def check_correctness(paths, obstacles):
    s = set()
    for path in paths:
        for (x, y) in path:
            if (x, y) in s: return False
            for o in obstacles:
                if (o[0] <= x <= o[2]) and (o[1] <= y <= o[3]):
                    return False
            s.add((x, y))
    return True

def main():
    filename = sys.argv[1]
    print(filename)
    # read all the chip related info from the input file
    with open(filename) as f:
        # first two lines are grid width and height
        h = int(f.readline()); w = int(f.readline())
        
        # third line is the number of obstacles; following numObst lines are the obstacle co-ordinates
        numObst = int(f.readline())
        obstacles = []
        for n in range(numObst):
            line = f.readline()
            obstacles.append([int(x) for x in line.split()])
        
        # read the number of points and their co-ordinates
        numPoints = int(f.readline())
        points = []
        for n in range(numPoints):
            line = f.readline()
            pts = [int(x) for x in line.split()]
            points.append(((pts[0], pts[1]), (pts[2], pts[3])))
    grid = dict(((x, y), 0) for x in range(w) for y in range(h))
    # lay out the obstacles
    for o in obstacles:
        for x in range(o[0], o[2] + 1):
            for y in range(o[1], o[3] + 1):
                grid[(x, y)] = -1
    
    cnt = 1 # route count
    for (s, d) in points:
        grid[s] = cnt; grid[d] = cnt
        cnt += 1
    

    numPaths = cnt - 1
    g = Grid(w, h, grid)
        
    #g.pretty_print_grid()

    paths = find_paths(g, points)
    if paths is None:
        print "Cannot connect all the points!"
    else:
        # check the correctness
        if not check_correctness(paths, obstacles):
            raise Exception("Incorrect solution, some path cross each other or the obstacles!")
        print "Paths:"
        totLength = 0
        for p in paths:
            print p
            totLength += len(p)
        print "Total Length: " + str(totLength)
    
if __name__ == "__main__":
    main()
