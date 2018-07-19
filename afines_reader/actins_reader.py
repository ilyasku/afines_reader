import numpy as np
from .base_reader import BaseReader
from .model.actins import Actins

class ActinsReader(BaseReader):

    def __init__(self, fname):
        BaseReader.__init__(self, fname)
        self.actins = {}        

    def parse_content_following_step_line(self, t, lines):
        N = len(lines)
        x = np.empty(N)
        y = np.empty(N)
        r = np.empty(N)
        fidx = np.empty(N, dtype=np.int16)
        for i, l in enumerate(lines):
            split = l.split("\t")
            x[i] = float(split[0])
            y[i] = float(split[1])
            r[i] = float(split[2])
            fidx[i] = int(split[3])
        a = Actins(x, y, r, fidx)
        self.actins[t] = a
