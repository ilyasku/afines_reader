import numpy as np

class BaseReader(object):

    def __init__(self, fname):
        self.fname = fname
        self.t = None

    def read(self):
        f = open(self.fname, "rt")
        lines = f.readlines()

        t = []
        N = []

        i = 0
        while i < len(lines):
            t_i, N_i = self.parse_step_line(lines[i])
            t.append(t_i)
            N.append(N_i)
            self.parse_content_following_step_line(t_i, lines[i+1: i+N_i+1])
            i += N_i + 1
        self.t = np.array(t)

    def parse_content_following_step_line(self, t, content_lines):
        raise NotImplementedError("Abstract Base Class")

    @staticmethod
    def parse_step_line(step_line):
        split = step_line.split("\t")
        t = float(split[0].split("=")[1])
        N = int(split[1].split("=")[1])
        return t, N
