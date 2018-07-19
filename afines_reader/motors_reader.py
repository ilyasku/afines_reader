import np
from .base_reader import BaseReader
from .model.motors import Motors

class MotorsReader(BaseReader):

    def __init__(self, fname):
        BaseReader.__init__(self, fname)
        self.motors = {}

    def parse_content_following_step_line(self, t, lines):
        N = len(lines)
        x = np.empty(N)
        y = np.empty(N)
        dx = np.empty(N)
        dy = np.empty(N)
        fidx0 = np.empty(N, dtype=np.int16)
        fidx1 = np.empty(N, dtype=np.int16)
        lidx0 = np.empty(N, dtype=np.int16)
        lidx1 = np.empty(N, dtype=np.int16)
        for i, l in enumerate(lines):
            split = l.split("\t")
            x[i] = float(split[0])
            y[i] = float(split[1])
            dx[i] = float(split[2])
            dy[i] = float(split[3])
            fidx0[i] = int(split[4])
            fidx1[i] = int(split[5])
            lidx0[i] = int(split[6])
            lidx1[i] = int(split[7])
        m = Motors(x, y, dx, dy, fidx0, fidx1, lidx0, lidx1)
        self.motors[t] = m
