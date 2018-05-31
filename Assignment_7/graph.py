"""
graph.py: Contains classes for representing a graph.
"""


class Grid(object):
    """
    A class representing a grid graph object.
    """

    def __init__(self, height, width, oob):
        """
        Create an object of the Grid type.

        @height: The height of the grid.
        @width: The width of the grid.
        @oob: A list in which each contains coordinates of two points,
              each of which specify a rectangular area which is blocked
              /out-of-bounds and cannot be traversed.
        """

        self.height = height
        self.width = width
        self.oob = []

        for ((x1, y1), (x2, y2)) in oob:
            if 0 <= x1 < width and \
               0 <= x2 < width and \
               0 <= y1 < height and \
               0 <= y2 < height:
                # Convert the bounds to bottom-left and top-right
                (x1, x2) = sorted((x1, x2))
                (y1, y2) = sorted((y1, y2))

                self.oob.append(((x1, y1), (x2, y2)))

        self.oob.sort()

    def isOOB(self, coords):
        """
        Returns whether a point is out-of-bounds, i.e not inside valid grid region.
        """

        (x, y) = coords

        if x < 0 or x >= self.width or y < 0 or y >= self.height:
           return True

        for ((x1, y1), (x2, y2)) in self.oob:
           if x1 <= x <= x2 and y1 <= y <= y2:
               return True

        return False

    def neighboursOf(self, coords):
        """
        Get the available neighbours of a point.

        @coords: Coordinate of the point.

        Returns: The list of available neightbours.
        """

        (x, y) = coords

        neighbours = list(map(lambda v: (x + v[0], y + v[1]),
                              [(0, 1), (0, -1), (1, 0), (-1, 0)]))

        return list(filter(lambda a: not self.isOOB(a), neighbours))

    def __str__(self):
        """
        Pretty print a grid.
        """

        grid = [['. ' for _ in range(self.width)] + ['\n'] for _ in range(self.height)]

        for ((x1, y1), (x2, y2)) in self.oob:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[self.height - j - 1][i] = '# '

        return ''.join(map(lambda x: ''.join(x), grid))

    def __repr__(self):
        """
        Return a representation.
        """

        return "Grid(%d, %d, %s)" % (self.width, self.height, self.oob.__repr__())
