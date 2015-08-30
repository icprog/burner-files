class Effect(object):

    def __init__(self, cols, rows, pattern):
        self.cols = cols
        self.rows = rows
        self.n_pixels = cols * rows
        self.pattern = pattern

