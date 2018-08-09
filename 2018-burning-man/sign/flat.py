from __future__ import division
import color_utils
import math

from effect import Effect

class Flat(Effect):
    def get_pixels(self, t):
        pixels = []
        for y in range(self.rows):
            for x in range(self.cols):
                pixels.append(self.pattern.cget(x, y))
        return pixels
