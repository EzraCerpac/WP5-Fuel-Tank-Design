import numpy as np
import os
import MaterialProperties as mp


def calcSigma_br(P, t2, D2):
    return P / (D2 * t2)


def BearingCheck(material, sigma_br):
    print(f"running BearingCheck in {os.path.basename(__file__)}")
    F_bry = mp.F_bry(material)

    if sigma_br > F_bry:
        print(f"\nBearing Failure!!! Bearing allowable of {material} = {F_bry} MPa, but the "
              f"bearing stress is {sigma_br} MPa.\n")
    elif sigma_br < 0.8 * F_bry:
        print(f"\nFurther optimization possible! Bearing allowable of {material} = {F_bry} MPa, but the "
              f"bearing stress is just {sigma_br} MPa.\n")
    else:
        print(f"\nPerfect bearing stress. Bearing allowable of {material} = {F_bry} MPa, and the "
              f"bearing stress is {sigma_br} MPa.\n")


def main(t2, F_inplaneX, F_inplaneZ, F_inplaneMy, fastener_x, fastener_z, fastener_distance, D2):
    # print(f"running {os.path.basename(__file__)}")
    Fx = F_inplaneX + F_inplaneMy * fastener_x / fastener_distance
    Fz = F_inplaneZ + F_inplaneMy * fastener_z / fastener_distance

    P = np.sqrt(Fx ** 2 + Fz ** 2)

    sigma_br = P / (D2 * t2)

    return max(P), max(sigma_br)


def find_t2(F_inplaneX, F_inplaneZ, F_inplaneMy, fastener_x, fastener_z, fastener_distance, D2, material):
    print(f"running {os.path.basename(__file__)}")
    Fx = F_inplaneX + F_inplaneMy * fastener_x / fastener_distance
    Fz = F_inplaneZ + F_inplaneMy * fastener_z / fastener_distance

    P = np.sqrt(Fx ** 2 + Fz ** 2)

    margin = 0.8

    sigma_br = mp.F_bry(material) * margin

    t2 = P / (D2 * sigma_br)

    return max(P), sigma_br, max(t2)
