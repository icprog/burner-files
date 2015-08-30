from __future__ import division
import color_utils
import math

from effect import Effect

class Flat(Effect):
    def get_pixels(self, t):
        pixels = []
        for y in range(self.rows):
            for x in range(self.cols):
                if self.pattern.get(x, y):
                    pixels.append((255, 255, 255))
                else:
                    pixels.append((0, 0, 0))
        return pixels
