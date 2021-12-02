from math import pi
import math

def NatFreq(E,L,t,m,r):
    A = pi * 2*r * t
    k = 2*(E * A) / L # 2 because mass is at center of mass
    Fn = math.sqrt(k / m) * (1 / (2 * pi))
    return Fn




