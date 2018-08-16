import random

from math import cos, pi
from PIL import Image, ImageFilter


COLS = 20
ROWS = 12


def squash(v, low, high):
    return min(max(low, v), high)


class FlatImage:
    def __init__(self, file_name):
        self.image = Image.open(file_name)
        self.arr = self.image.load()

    def tick(self, ts):
        pass

    def get_pixels(self):
        return [self.arr[c, r][:3]
                for r in range(0, ROWS)
                for c in range(0, COLS)]


def randfloat(lo, hi):
    return lo + random.random() * hi


def sprite_off(sprite, target_img):
    pass


def sprite_move(sprite, target_img):
    target_img.paste(sprite,
                     (random.choice([-1, 1]), random.choice([-1, 1])),
                     mask=sprite)

    
def sprite_smooth(sprite, target_img):
    blurred = sprite.copy()
    blurred.paste(sprite, (0, -1), sprite)
    blurred.paste(sprite, (0, 1), sprite)
    blurred = Image.blend(blurred, sprite, 0.3)
    blurred.paste(sprite, (0, 0), mask=sprite)
    target_img.paste(blurred, None, mask=blurred)


def normal(sprite, target_img):
    target_img.paste(sprite, None, mask=sprite)


class SpriteJitter:
    EMPTY_COLOR = (0, 0, 0)
    OPS = [sprite_smooth, sprite_off, sprite_move]

    EFFECT_DURATION = [0.2, 1.5]
    BREAK_DURATION = [0.5, 1]
    SPRITE_IDX_DURATION = [3, 10]

    def __init__(self, file_name):
        self.image = Image.open(file_name)
        self.sprites = self.find_sprites()
        self.start_ts = None
        self.effect_end = None
        self.effect = None

    def tick(self, ts):
        if self.start_ts is None:
            self.start_ts = ts
            self.effect_end = ts
            self.effect = '--start--'
            self.sprite_idx_end = ts

        if ts >= self.sprite_idx_end:
            self.sprite_idx_end = ts + randfloat(*self.SPRITE_IDX_DURATION)
            self.sprite_idx = random.randrange(0, len(self.sprites))
        elif ts < self.effect_end:
            return

        if self.effect == normal:
            self.effect = random.choice(self.OPS)
            self.effect_end = ts + randfloat(*self.EFFECT_DURATION)
        else:
            self.effect = normal
            self.effect_end = ts + randfloat(*self.BREAK_DURATION)

        img = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
        for idx, s in enumerate(self.sprites):
            if idx != self.sprite_idx:
                img.paste(s, (0, 0), mask=s)
        if self.sprite_idx is not None:
            self.effect(self.sprites[self.sprite_idx], img)
        self.arr = img.load()

    def source_p(self, c, r):
        if (c < 0) or (c >= self.image.width) or (r < 0) or (r >= self.image.height):
            return (0, 0, 0, 0)
        return self.image.load()[c, r]

    def get_pixels(self):
        return [self.arr[c, r][:3]
                for r in range(0, ROWS)
                for c in range(0, COLS)]

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
                    if self.source_p(x + dx, y + dy) == sprite_color:
                        mark_seen(x, y)
                        spr.putpixel((x, y), sprite_color)
                        if (dx != 0) or (dy != 0):
                            flood_copy(sprite_color, spr, x+dx, y+dy)

        def get_sprite(sx, sy):
            spr = Image.new('RGBA', self.image.size, (0, 0, 0, 0))
            flood_copy(self.source_p(sx, sy), spr, sx, sy)
            return spr

        for x in range(0, self.image.width):
            for y in range(0, self.image.height):
                if seen(x, y):
                    continue
                if self.source_p(x, y)[:3] == (0, 0, 0):
                    continue
                sprites.append(get_sprite(x, y))

        return sprites


class GreenT:
    LOOP_LEN = 10

    def __init__(self, file_name):
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
        return self.arr[
            squash(c, 0, self.image_width-1),
            squash(r, 0, self.image_height-1),
        ]

    def get_pixels(self):
        return [self.p(c, r + self.dy)[:3]
                for r in range(0, ROWS)
                for c in range(0, COLS)]


class MultiEffect:
    def __init__(self, effects, duration):
        self.effects = effects
        self.duration = duration
        self.effect_idx = 0
        self.end_ts = None

    def tick(self, ts):
        if self.end_ts is None:
            self.end_ts = ts + self.duration

        if ts >= self.end_ts:
            self.effect_idx = (self.effect_idx + 1) % len(self.effects)
            self.end_ts = ts + self.duration

        self.effects[self.effect_idx].tick(ts)

    def get_pixels(self):
        return self.effects[self.effect_idx].get_pixels()


class Bunny:
    # In memory of Bull Bunny aka Michael R Oddo
    FILE_NAME = 'img/bunny4.png'

    def __init__(self):
        self.image = Image.open(self.FILE_NAME)
        self.arr = self.image.load()

    def tick(self, ts):
        pass

    def get_pixels(self):
        return [self.arr[c, r][:3]
                for r in range(0, ROWS)
                for c in range(0, COLS)]
