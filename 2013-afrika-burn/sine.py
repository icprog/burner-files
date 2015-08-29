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

class Sine(object):
    def __init__(self, n_pixels):
        self.n_pixels = n_pixels

    def get_pixels(self, t):
        pixels = []
        for y in range(10):
            for x in range(20):
                period = color_utils.cos(t, period=4, minn=10, maxx=40)
                shift = color_utils.cos(x + t * 10, period=period, minn=-2, maxx=2)
                lvl = color_utils.cos(y + shift, period=10, minn=1, maxx=0.4)
                ii = y * 20 + x
                f = flow[ii]
                if f:
                    pixels.append((0, 0, 0))
                else:
                    pixels.append((lvl * 255, 0, 0))
        return pixels
