#!/usr/bin/python

# Generate fcserver and gl_server layouts for planned sign.
#
# The physical layout is 6 strands of 40 LEDs each, folded in half to
# create two rows:
#
# -o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o.
#  o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o'
# -o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o.
#  o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o-o'
# [...]


STRANDS = 6
ROWS = STRANDS * 2
COLS = 20
LED_CNT = ROWS * COLS

COLOR_LAYOUT = "rgb"

def print_out(pixels):
    for y in range(ROWS):
        for p in pixels[y * COLS:y * COLS + COLS]:
            print "%d:%03d" % tuple(p[1:]),
        print

def pos(x, y):
    return x + y * COLS

def gen_pixels():
    ret = [[i, 0, 0] for i in range(LED_CNT)]

    for l in range(STRANDS):
        for x in range(COLS):
            p = ret[pos(x, 2 * l)]
            p[1] = l
            p[2] = l * 64 + x
    
            p = ret[pos(COLS - x - 1, 2 * l + 1)]
            p[1] = l
            p[2] = l * 64 + x + COLS

    return ret

FCSERVER_CONFIG_TEMPLATE = """
{
    "listen": ["%(listen_addr)s", 7890],
    "verbose": true,

    "color": {
        "gamma": 2.5,
        "whitepoint": [1.0, 1.0, 1.0]
    },

    "devices": [
        {
            "type": "fadecandy",
            "map": [
%(map_str)s
]
        }
    ]
}
"""

def write_fcserver_config(fname, listen_addr, pixels):
    map_str = ",\n".join("[ %d, %d, %d, %d, \"%s\"]"
                         % (0, p[0], p[2], 1, COLOR_LAYOUT)
                 for (i, p) in enumerate(pixels))
    f = open(fname, 'w')
    f.write(FCSERVER_CONFIG_TEMPLATE % locals())

pixels = gen_pixels()
write_fcserver_config("fcserver.json", "127.0.0.1", pixels)
write_fcserver_config("fcserver-dev.json", "0.0.0.0", pixels)

print_out(pixels)
