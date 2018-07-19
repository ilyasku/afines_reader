import numpy as np

class Motors(object):

    def __init__(self, x: np.ndarray, y: np.ndarray,
                 dx: np.ndarray, dy: np.ndarray,
                 fidx0: np.ndarray, fidx1: np.ndarray,
                 lidx0: np.ndarray, lidx1: np.ndarray):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.fidx0 = fidx0
        self.fidx1 = fidx1
        self.lidx0 = lidx0
        self.lidx1 = lidx1

    def __str__(self):
        s = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}"
        return s.format(self.x, self.y,
                        self.dx, self.dy,
                        self.fidx0, self.fidx1,
                        self.lidx0, self.lidx1)

    def __repr__(self):
        return self.__str__()
