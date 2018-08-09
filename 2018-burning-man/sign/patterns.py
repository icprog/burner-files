
DEFAULT_C = (255, 255, 255)
PALETTE = {
    '.': (0, 0, 0),
    'R': (255, 0, 0),
    'G': (0, 255, 0),
    'B': (0, 0, 255),
}

PATTERNS = {}

class Pattern:

    def __init__(self, name, pat):
        self.name = name
        self.pat = pat

    def get(self, c, r):
        return ((0 <= r < len(self.pat))
                and (0 <= c < len(self.pat[r]))
                and (self.pat[r][c] != '.'))

    def cget(self, c, r):
        if not ((0 <= r < len(self.pat))
                and (0 <= c < len(self.pat[r]))):
            return DEFAULT_C
        return PALETTE.get(self.pat[r][c], DEFAULT_C)

def p(name, data):
    PATTERNS[name] = Pattern(name, data)
    return PATTERNS[name]

p("dear-big", [
    #01234567890123456789
    "....................", #0
    "....................", #1
    ".@@@..@@@..@@..@@@..", #2
    ".@..@.@...@..@.@..@.", #3
    ".@..@.@...@..@.@..@.", #4
    ".@..@.@@..@@@@.@@@..", #5
    ".@..@.@...@..@.@@...", #6
    ".@..@.@...@..@.@.@..", #7
    ".@..@.@...@..@.@..@.", #8
    ".@@@..@@@.@..@.@..@.", #9
    "....................", #A
    "....................", #B
])

p("dear-bold", [
    #01234567890123456789
    "....................", #0
    "GGG..BBBB.GGG..BBB..", #1
    "GGGG.BBBBGGGGG.BBBB.", #2
    "GG.GGBB..GG.GG.BB.BB", #3
    "GG.GGBB..GG..G.BB.BB", #4
    "GG.GGBBBBGGGGG.BBBB.", #5
    "GG.GGBBBBGGGGG.BBB..", #6
    "GG.GGBB..GG.GG.BBBB.", #7
    "GG.GGBB..GG.GG.BB.BB", #8
    "GGGG.BBBBGG.GG.BB.BB", #9
    "GGG..BBBBGG.GG.BB.BB", #A
    "....................", #B
])

p("camp dear", [
    #01234567890123456789
    "....................", #0
    "..@@..@@..@...@.@@@.", #1
    ".@...@..@.@@.@@.@..@", #2
    ".@...@@@@.@.@.@.@@@.", #3
    ".@...@..@.@...@.@...", #4
    "..@@.@..@.@...@.@...", #5
    "....................", #6
    ".@@@..@@@..@@..@@@..", #7
    ".@..@.@...@..@.@..@.", #8
    ".@..@.@@..@@@@.@@@..", #9
    ".@..@.@...@..@.@.@..", #A
    ".@@@..@@@.@..@.@..@.", #B
])

p("test", [
    #01234567890123456789
    "R@@@............@@@R", #0
    "@..................@", #1
    "@..................@", #2
    "@.RRR....GG...BBB..@", #3
    "..R..R..G..G..B..B..", #4
    "..RRR...G.....BBB...", #5
    "..R..R..G.GG..B..B..", #6
    "..R..R..G..G..B..B..", #7
    "@.R..R...GG...BBB..@", #8
    "@..................@", #9
    "@..................@", #A
    "R@@@............@@@R", #B
])

p("orphan-asylum-1", [
    #01234567890123456789
    "RRRR...WW...........", #0
    "R..RWW.WWW.W.W.R.WW.", #1
    "R..RW..WW..WWWR.RW.W", #2
    "R..RW..W...W.WRRRW.W", #3
    "RRRRW..W...W.WR.RW.W", #4
    "....................", #5
    "RRRR................", #6
    "R..R..R.RW..R.RW...W", #7
    "RRRR.WWR.W..R.RWW.WW", #8
    "R..R.W.R.W..R.RW.W.W", #9
    "R..R.W.R.W..R.RW...W", #A
    "R..RWW.R.WWWRRRW...W", #B
])

p("orphan-asylum-2", [
    #01234567890123456789
    "RRR....WWw..........", #0
    "R.RwWW.W.W.W.W.R.WW.", #1
    "R.RwWw.WWw.WWWR.RW.W", #2
    "R.RwW..Ww..W.WRRRW.W", #3
    "RRRwW..Ww..W.WR.RW.W", #4
    "....................", #5
    "RRR..RR.RR..........", #6
    "R.R.wwRRRWW.R.RW...W", #7
    "RRR.wWWRRWW.R.RWW.WW", #8
    "R.R.wW.RRWW.R.RWWWWW", #9
    "R.RwwW.RRWWWR.RWW.WW", #A
    "R.RwWW.RRWWWRRRWW.WW", #B
])

p("orphan-asylum-3", [
    #01234567890123456789
    "RRRR................", #0
    "R..RWW.WW.W...R.W..W", #1
    "R..RW..WW.W..R.RWW.W", #2
    "R..RW..W..WWWRRRW.WW", #3
    "RRRRW..W..W.WR.RW..W", #4
    "....................", #5
    "RRRR................", #6
    "R..R..R.R...R.R.....", #7
    "RRRR.WWR..W.R.RW...W", #8
    "R..R.W.R..W.R.RWW.WW", #9
    "R..R.W.R..W.RRRW.W.W", #A
    "R..RWW....WWW..W...W", #B
])
