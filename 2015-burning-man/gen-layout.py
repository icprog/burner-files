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

GL_SCALE = 0.2
GL_X     = -2
GL_Y     = 0
GL_Z     = -1

def print_out(pixels):
    for y in range(ROWS):
        for p in pixels[y * COLS:y * COLS + COLS]:
            print "%d:%03d" % (p[0], p[1]),
        print

def pos(x, y):
    return x + y * COLS

# Build an array:
#
# led_idx: [strand_idx, fc_led_idx, (lx, ly, lz)]
#
# - led_idx is the OPC index of a led (in natural order: row_idx * COLS + col_idx)
# - fc_led_idx is the fadecandy address of that led
# - lx, ly, lz is the position of that LED in space
def gen_pixels():
    ret = [[0, 0] for i in range(LED_CNT)]

    def set_pixel(x, y, strand, idx_on_strand):
        # Fadecandy constant: the first led on strand n has index 64*n
        STRAND_START = 64 * strand
        ret[pos(x, y)] = [strand, STRAND_START + idx_on_strand, (GL_X + GL_SCALE * x, GL_Y, GL_Z + GL_SCALE * y)]

    for s in range(STRANDS):
        for x in range(COLS):
            # top half
            set_pixel(x, 2 * s, s, x)
            # bottom half
            set_pixel(x, 2 * s + 1, s, 2 * COLS - x - 1)

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
    map_str = ",\n".join('[ %d, %d, %d, %d, "%s"]'
                         % (0, i, p[1], 1, COLOR_LAYOUT)
                 for (i, p) in enumerate(pixels))
    f = open(fname, 'w')
    f.write(FCSERVER_CONFIG_TEMPLATE % locals())

def write_glserver_layout(fname, pixels):
    points = ",\n".join('{"point": [%f, %f, %f]}' % p[2]
                        for p in pixels)
    open(fname, 'w').write("[\n" + points + "]\n")

pixels = gen_pixels()
write_fcserver_config("fcserver.json", "127.0.0.1", pixels)
write_fcserver_config("fcserver-dev.json", "0.0.0.0", pixels)
write_glserver_layout("glserver-layout.json", pixels)

print_out(pixels)
