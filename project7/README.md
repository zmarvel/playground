# Project 7 — Routing Wires on a Chip #

I added to the `Grid` class a `remove_paths` method, which simply clears all
the paths between points from the grid in order to start fresh. I also added
a method (for convenience) `num_vertices` to the `Graph` class which is
self-explanatory.

I defined `eucl_dist`, which, given two coordinate pairs, returns the Euclidean
distance between them. This was to implement a better BFS search, in which
points that are closer in terms of Euclidean distance to the target point are
prioritized as a sort of best-guess strategy.

The implementation of `find_paths` relies on BFS. Our `bfs` function is very
similar to the one given in class. The primary difference is that it will stop
when it finds the target point. As I mentioned before, another difference is
that nodes closer to the target point are prioritized. This occurs in the 
statement `sorted(g.adj(u), key=lambda p: eucl_dist(p, target))`, which sorts
the adjacent vertices by their distance to the target point.

Our `traceback` function starts at a target point (that is, the end of a path),
and it follows parent pointers all the way to the source of the path. Along
the way, it keeps track of each point it touches and marks it in the grid as
a path (which other paths must avoid).

Finally, `find_paths` keeps track of the paths with a list, the points with a
queue, and the pairs of points that we *were* and *were not* able to connect 
with a wire.

First, we do a BFS to from the given point to find the target. If we aren't able
to find a path to the target... well, I had two solutions. First, I took the
easy road and just started over completely. Obviously this was pretty slow, so 
now it tries to remove the paths it has added in reverse order until it can
finally find a path to the target. If we are able to find a path (using
our traceback function), we store the result with the other paths we have found,
and we return them all when we've connected all the points.
