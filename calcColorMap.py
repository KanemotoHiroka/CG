def calcColorMap(x):
    r = 1.0
    g = 0.0
    b = 0.0
    if x <= 1:
        r = 1.0
        g = 0.0
        b = 1.0 - (x - 5.0/6.0)*6.0
    if x <= 5.0/6.0:
        r = 6.0*(x - 4.0/6.0)
        g = 0.0
        b = 1.0
    if x <= 4.0/6.0:
        r = 0.0
        g = 1.0 - (x - 3.0/6.0)*6.0
        b = 1.0
    if x <= 3.0/6.0:
        r = 0.0
        g = 1.0
        b = 6.0*(x - 2.0/6.0)
    if x <= 2.0/6.0:
        r = 1.0 - (x - 1.0/6.0)*6.0
        g = 1.0
        b = 0.0
    if x <= 1.0/6.0:
        r = 1.0
        g = 6.0*x
        b = 0.0
    return [r, g, b]