class BoundingBox(object):
    """
    A 2D bounding box
    """

    def __init__(self, points):
        if len(points) == 0:
            raise ValueError("Can't compute bounding box of empty list")
        self.minx, self.miny = float("inf"), float("inf")
        self.maxx, self.maxy = float("-inf"), float("-inf")
        for point in points:
            # Set min coords
            if point['x'] < self.minx:
                self.minx = point['x']
            if point['y'] < self.miny:
                self.miny = point['y']
            # Set max coords
            if point['x'] > self.maxx:
                self.maxx = point['x']
            if point['y'] > self.maxy:
                self.maxy = point['y']

    @property
    def width(self):
        return self.maxx - self.minx

    @property
    def height(self):
        return self.maxy - self.miny

    def __repr__(self):
        return "BoundingBox({}, {}, {}, {})".format(
            self.minx, self.maxx, self.miny, self.maxy)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, BoundingBox):
            return self.minx == other.minx and self.miny == other.miny and self.maxy == other.maxy and self.maxx == other.maxx
        return False

    #
    # def hash(self):
    #     """Overrides the default implementation"""
    #     return hash(tuple(sorted(self.dict.items())))
