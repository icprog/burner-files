from __future__ import division
import color_utils
import math

from effect import Effect
from random import randint

def color_average(colors):
    s = [0, 0, 0]
    for c in colors:
        for i in range(3):
            s[i] += c[i]
    for i in range(3):
        s[i] /= len(colors)
    return tuple(s)

def color_max(colors):
    s = [0, 0, 0]
    for c in colors:
        for i in range(3):
            s[i] = max([s[i], c[i]])
    return tuple(s)

class Wheel(Effect):
    def get_pixels(self, t):
        pixels = []
        for y in range(self.rows):
            for x in range(self.cols):
                c = self.pattern.cget(x, y)
                if c != (0, 0, 0):
                    pixels.append(c)
                else:
                    pixels.append(self.get_smoothed_color(x, y, t))
        return pixels

    def get_smoothed_color(self, x, y, t):
        colors = []
        for dx in [-0.1, 0, 0.1]:
            for dy in [-0.1, 0, 0.1]:
                colors.append(self.get_color(x + dx, y + dy, t))
        return color_average(colors)

    def get_color(self, x, y, t):
        dx = x - self.cx
        dy = y - self.cy
        if dx == dy == 0:
            r = 1
        else:
            a = math.atan2(dx, dy)
            r = color_utils.cos(a + t, period=0.3 * math.pi, minn=-0.5, maxx=1.5)
        return (color_utils.clamp(r, 0, 1) * 255, 0, 0)

    def switch_on(self):
        self.cx = randint(0, self.cols - 1)
        self.cy = randint(0, self.rows - 1)
