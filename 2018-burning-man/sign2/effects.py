from math import cos, pi
from PIL import Image


def squash(v, low, high):
    return min(max(low, v), high)


class FlatImage:
    def __init__(self, cols, rows, file_name):
        self.cols = cols
        self.rows = rows
        self.image = Image.open(file_name)
        self.arr = self.image.load()

    def tick(self, ts):
        pass

    def get_pixels(self):
        return [self.arr[c, r][:3]
                for r in range(0, self.rows)
                for c in range(0, self.cols)]


class GreenT:
    LOOP_LEN = 10

    def __init__(self, cols, rows, file_name):
        self.cols = cols
        self.rows = rows
        self.image = Image.open(file_name)
        self.arr = self.image.load()
        self.start_ts = None

    def tick(self, ts):
        if self.start_ts is None:
            self.start_ts = ts
        self.dy = squash(
            14*(0.5-cos((ts - self.start_ts) * 2 * pi / self.LOOP_LEN)),
            0, 6,
        )

    def p(self, c, r):
        return self.arr[squash(c, 0, self.cols-1), squash(r, 0, self.rows-1)]

    def get_pixels(self):
        return [self.p(c, r + self.dy)[:3]
                for r in range(0, self.rows)
                for c in range(0, self.cols)]
