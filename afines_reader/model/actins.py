import numpy as np

class Actins(object):

    def __init__(self, x: np.ndarray, y: np.ndarray,
                 r: np.ndarray, fidx: np.ndarray):
        self.x = x
        self.y = y
        self.r = r
        self.fidx = fidx

    def __str__(self):
        s = "Actins data of {} filaments, consisting of {} beads."
        return s.format(len(np.unique(self.fidx)), len(self.x))

    def __repr__(self):
        return self.__str__()
