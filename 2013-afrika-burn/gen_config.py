#!/usr/bin/python

pixels = [[i, 0, 0] for i in range(200)]

def print_out(pixels):
    for y in range(10):
        for p in pixels[y * 20:y * 20 + 20]:
            print "%d:%03d" % tuple(p[1:]),
        print 

def pos(x, y):
    return x + y * 20

for i in range(5):
    for x in range(20):
        p = pixels[pos(19 - x, 8 - 2 * i)]
        p[1] = i
        p[2] = x + i * 64

        p = pixels[pos(x, 9 - 2 * i)]
        p[1] = i
        p[2] = x + 20 + i * 64

print ",\n".join("[ %d, %d, %d, %d]" % (0, p[0], p[2], 1)
                 for (i, p) in enumerate(pixels))

print_out(pixels)
