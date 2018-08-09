from __future__ import division
import color_utils
import math

# how many sine wave cycles are squeezed into our n_pixels
# 24 happens to create nice diagonal stripes on the wall layout
freq_r = 24
freq_g = 24
freq_b = 24

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
print flow

class Raver(object):
    def __init__(self, n_pixels):
        self.n_pixels = n_pixels

    def get_pixels(self, t):
        pixels = []
        flow_color = None
        for ii in range(self.n_pixels):
            pct = ii / self.n_pixels
            # diagonal black stripes
            pct_jittered = (pct * 77) % 37
            blackstripes = color_utils.cos(pct_jittered, offset=t*0.05, period=1, minn=0, maxx=1.5)
            blackstripes_offset = color_utils.cos(t, offset=0.9, period=60, minn=-0.5, maxx=3)
            blackstripes = color_utils.clamp(blackstripes + blackstripes_offset, 0, 1)
            # 3 sine waves for r, g, b which are out of sync with each other
            r = blackstripes * color_utils.remap(math.cos((t/speed_r + pct*freq_r)*math.pi*2), -1, 1, 10, 256)
            g = blackstripes * color_utils.remap(math.cos((t/speed_g + pct*freq_g)*math.pi*2), -1, 1, 10, 256)
            b = blackstripes * color_utils.remap(math.cos((t/speed_b + pct*freq_b)*math.pi*2), -1, 1, 10, 256)
            if flow[ii]:
                if flow_color is None:
                    flow_color = (r, 0, 0)
                pixels.append(flow_color)
            else:
                pixels.append((0, g, b))
        return pixels
