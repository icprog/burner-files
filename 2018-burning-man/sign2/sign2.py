#!/usr/bin/env python3

import effects
import opc
import sys
import time


COLS = 20
ROWS = 12


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


def run_sign(client, fps):
    start_time = time.time()
    switch_time = 0
#    effect = effects.GreenT(COLS, ROWS, "img/green-t-1.png")
    effect = effects.SpriteJitter(COLS, ROWS, "img/oa-main.png")
    while True:
        t = time.time() - start_time
#        if t >= switch_time:
#            effect = random.choice(effects)
#            effect.switch_on()
#            switch_time = t + random.uniform(3, 3)
        effect.tick(t)
        pixels = effect.get_pixels()
        client.put_pixels(pixels, channel=0)
        time.sleep(1 / fps)


if __name__ == '__main__':
    main()
