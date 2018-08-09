from __future__ import division
import color_utils
import math

from effect import Effect

class Sine(Effect):
    def get_pixels(self, t):
        pixels = []
        for y in range(self.rows):
            for x in range(self.cols):
                period = 1 + color_utils.cos(t, period=4, minn=10, maxx=40)
                shift = color_utils.cos(x + t * 10, period=period, minn=-2, maxx=2)
                lvl = color_utils.cos(y + shift, period=10, minn=1, maxx=0.4)
                if self.pattern.get(x, y):
                    pixels.append((255, 255, 255))
                else:
                    pixels.append((lvl * 255, 0, 0))
        return pixels
