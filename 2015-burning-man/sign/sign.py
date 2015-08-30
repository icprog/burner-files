#!/usr/bin/env python

from __future__ import division
import time
import math
import sys

import opc
import os
import color_utils
import random

from fake_client import FakeClient

from raver import Raver
from waves import Waves
from fullred import FullRed
from sine import Sine

effects = [Waves(200), FullRed(200), Sine(200)]
effect_idx = 0

#-------------------------------------------------------------------------------
# handle command line

fake = os.environ.get('FAKE')

if len(sys.argv) == 1:
    IP_PORT = '127.0.0.1:7890'
elif len(sys.argv) == 2 and ':' in sys.argv[1] and not sys.argv[1].startswith('-'):
    IP_PORT = sys.argv[1]
else:
    print
    print '    Usage: raver_plaid.py [ip:port]'
    print
    print '    If not set, ip:port defauls to 127.0.0.1:7890'
    print
    sys.exit(0)


#-------------------------------------------------------------------------------
# connect to server

if fake:
	client = FakeClient()
else:
	client = opc.Client(IP_PORT)
if client.can_connect():
    print '    connected to %s' % IP_PORT
else:
    # can't connect, but keep running in case the server appears later
    print '    WARNING: could not connect to %s' % IP_PORT
print


#-------------------------------------------------------------------------------
# send pixels

print '    sending pixels forever (control-c to exit)...'
print

n_pixels = 200
if fake:
    fps = 10
else:
    fps = 20

start_time = time.time()
switch_time = 0
while True:
    t = time.time() - start_time
    if t >= switch_time:
        effect = random.choice(effects)
        switch_time = t + random.uniform(3, 3)
    pixels = effect.get_pixels(t)
    client.put_pixels(pixels, channel=0)
    time.sleep(1 / fps)

