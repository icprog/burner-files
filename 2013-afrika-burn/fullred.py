from __future__ import division
import color_utils
import math

# how many sine wave cycles are squeezed into our n_pixels
# 24 happens to create nice diagonal stripes on the wall layout
freq_r = 1
freq_g = 0.1
freq_b = 0.1

# how many seconds the color sine waves take to shift through a complete cycle
speed_r = 7
speed_g = -13
speed_b = 19

flow_str = """
. . . . . . . . . . . . . . . . . . . . 
. @ @ @ . @ . . . . @ @ . . @ . . . @ . 
. @ . . . @ . . . @ . . @ . @ . . . @ . 
. @ . . . @ . . . @ . . @ . @ . . . @ . 
. @ @ . . @ . . . @ . . @ . @ . . . @ . 
. @ . . . @ . . . @ . . @ . @ . . . @ . 
. @ . . . @ . . . @ . . @ . @ . @ . @ . 
. @ . . . @ . . . @ . . @ . @ @ . @ @ . 
. @ . . . @ @ @ . . @ @ . . @ . . . @ . 
. . . . . . . . . . . . . . . . . . . . 
""".replace(" ", "").replace("\n", "")

flow = [(c == "@") for c in flow_str]   

class FullRed(object):
    def __init__(self, n_pixels):
        self.n_pixels = n_pixels

    def get_pixels(self, t):
        pixels = []
        lvl = color_utils.cos(math.pi * t * 0.8, minn=-1, maxx=1)
        for y in range(10):
            for x in range(20):
                ii = y * 20 + x
                f = flow[ii]
                if f == (lvl > 0):
                    pixels.append((abs(lvl) * 256, 0, 0))
                else:
                    pixels.append((0, 0, 0))
        return pixels
