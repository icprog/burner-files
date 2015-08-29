#!/usr/bin/env python

spacing = 0.11  # m
lines = []
for c in range(-5, 5):
    rs = [range(20), reversed(range(20))][c % 2]
    for r in rs:
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                     (c*spacing, 0, (r - 24.5)*spacing))
print '[\n' + ',\n'.join(lines) + '\n]'
