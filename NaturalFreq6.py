import numpy as np


def NatFreq(E, L, t, m, r):
    A = np.pi * 2 * r * t
    k =2*(E * A) / L  # 2 because mass is at center of mass
    Fn = np.sqrt(k / m) * (1 / (2 * np.pi))
    return Fn
