import numpy as np


def SimplifiedNatFreq(E, L, t, m, r):
    A = np.pi * 2 * r * t
    k = 2 * (E * A) / L  # 2 because mass is at center of mass
    Fn = np.sqrt(k / m) * (1 / (2 * np.pi))
    print(k)
    return Fn


def DistNatFreq(E, L, t, m, r):
    A = np.pi * 2 * r * t
    k = (A * E) / L
    Fn = 1 / 4 * np.sqrt(k / m)
    return Fn, k
