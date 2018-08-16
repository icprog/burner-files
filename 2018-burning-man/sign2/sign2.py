#!/usr/bin/env python3

import effects
import opc
import sys
import time


def main():
    if len(sys.argv) == 1:
        IP_PORT = '127.0.0.1:7890'
    elif len(sys.argv) == 2 and ':' in sys.argv[1] and not sys.argv[1].startswith('-'):
        IP_PORT = sys.argv[1]
    else:
        print()
        print('    Usage: sign2.py [ip:port]')
        print()
        print('    If not set, ip:port defauls to 127.0.0.1:7890')
        print()
        sys.exit(0)
    client = opc.Client(IP_PORT)
    if client.can_connect():
        print('    connected to %s' % IP_PORT)
    else:
        # can't connect, but keep running in case the server appears later
        print('    WARNING: could not connect to %s' % IP_PORT)

    run_sign(client, 20)


class FrameTimer:
    def __init__(self, fps):
        self.ts = None
        self.delay = 1 / fps

    def sleep(self):
        now = time.time()
        if self.ts is not None:
            time.sleep(max(0, (self.ts + self.delay) - now))
        self.ts = now


def run_sign(client, fps):
    effect = effects.MultiEffect([
        effects.SpriteJitter("img/oa-main.png"),
        effects.Bunny(),
        effects.GreenT("img/green-t-1.png"),
    ], 10)
    ft = FrameTimer(fps)
    while True:
        ft.sleep()
        effect.tick(time.time())
        pixels = effect.get_pixels()
        client.put_pixels(pixels, channel=0)


if __name__ == '__main__':
    main()
