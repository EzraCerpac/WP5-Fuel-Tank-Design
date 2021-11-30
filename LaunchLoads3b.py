from math import pi

def main(E, v, p, R, L, t1, h):
    Q = p/E * (R/t1)**2
    k = h + 12/pi**4 * L**4/(R**2*t1**2) * (1-v**2)/h
    