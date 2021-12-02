from math import pi
import math

def NatFreq(E,L,t,m):
    A = pi * 2.3 * t
    k = (E * A) / L
    Fn = math.sqrt(k / m) * (1 / (2 * pi))
    return Fn




