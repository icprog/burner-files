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


class SpriteJitter:
    EMPTY_COLOR = (0, 0, 0)

    def __init__(self, cols, rows, file_name):
        self.cols = cols
        self.rows = rows
        self.image = Image.open(file_name)
        self.sprites = self.find_sprites()
        self.start_ts = None

    def tick(self, ts):
        if self.start_ts is None:
            self.start_ts = ts
        self.sprite_idx = int((ts - self.start_ts) / 2) % len(self.sprites)

    def p(self, c, r):
        if (c < 0) or (c >= self.image.width) or (r < 0) or (r >= self.image.height):
            return (0, 0, 0, 0)
        return self.image.load()[c, r]

    def get_pixels(self):
        return [self.sprites[self.sprite_idx].load()[c, r][:3]
                for r in range(0, self.rows)
                for c in range(0, self.cols)]

    def find_sprites(self):
        seen_img = Image.new('1', self.image.size, 0)
        sprites = []

        def seen(x, y): return seen_img.load()[x, y]
        def mark_seen(x, y): seen_img.putpixel((x, y), 1)

        def flood_copy(sprite_color, spr, x, y):
            if seen(x, y):
                return
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if self.p(x + dx, y + dy) == sprite_color:
                        mark_seen(x, y)
                        spr.putpixel((x, y), sprite_color)
                        if (dx != 0) or (dy != 0):
                            flood_copy(sprite_color, spr, x+dx, y+dy)

        def get_sprite(sx, sy):
            spr = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
            flood_copy(self.p(sx, sy), spr, sx, sy)
            return spr

        for x in range(0, self.image.width):
            for y in range(0, self.image.height):
                if seen(x, y):
                    continue
                if self.p(x, y)[:3] == (0, 0, 0):
                    continue
                sprites.append(get_sprite(x, y))

        return sprites


class GreenT:
    LOOP_LEN = 10

    def __init__(self, cols, rows, file_name):
        self.cols = cols
        self.rows = rows
        self.image = Image.open(file_name)
        (self.image_width, self.image_height) = self.image.size
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
        return self.arr[squash(c, 0, self.image_width-1), squash(r, 0, self.image_height-1)]

    def get_pixels(self):
        return [self.p(c, r + self.dy)[:3]
                for r in range(0, self.rows)
                for c in range(0, self.cols)]
