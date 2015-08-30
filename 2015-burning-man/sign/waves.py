from __future__ import division
import color_utils
import math

# how many sine wave cycles are squeezed into our n_pixels
# 24 happens to create nice diagonal stripes on the wall layout
freq_r = 0.1
freq_g = 0.1
freq_b = 0.1

# how many seconds the color sine waves take to shift through a complete cycle
speed_r = -3
speed_g = -2
speed_b = -1

class Waves(object):
    def __init__(self, cols, rows, pattern):
        self.cols = cols
        self.rows = rows
        self.n_pixels = cols * rows
        self.pattern = pattern

    def get_pixels(self, t):
        pixels = []
        flow_color = None

        hc = self.cols / 2
        hr = self.rows / 2

        for y in range(self.rows):
            for x in range(self.cols):
                dist = math.sqrt((x - hc) * (x - hc) + (y - hr) * (y - hr))
                # 3 sine waves for r, g, b which are out of sync with each other
                r = color_utils.remap(math.cos((t/speed_r + 1.0*dist*freq_r)*math.pi*2), -1, 1, 10, 256)
                g = color_utils.remap(math.cos((t/speed_g + 1.0*dist*freq_g)*math.pi*2), -1, 1, 10, 256)
                b = color_utils.remap(math.cos((t/speed_b + 1.0*dist*freq_b)*math.pi*2), -1, 1, 10, 256)
                if self.pattern.get(x, y):
                    if flow_color is None:
                        flow_color = (r, 0, 0)
                    if flow_color[0] > 0.9 * g:
                        pixels.append(flow_color)
                    else:
                        pixels.append((0.9 * g, 0.6 * g, 0))
                else:
                    pixels.append((0.9 * g, 0.6 * g, 0))
        return pixels
