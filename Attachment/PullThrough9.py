from math import pi, sqrt
import MaterialProperties as mp
import os


#mm and MPa here
def main(Fy, Dfo, Dfi, t2, t3, material_lug, material_wall):
    # print(f"running {os.path.basename(__file__)}")
    Dfo = Dfo/1000
    Dfi = Dfi/1000
    t2 = t2/1000
    t3 = t3/1000

    Ay2 = pi * Dfi * t2
    Ay3 = pi * Dfi * t3

    tauxy2 = Fy / Ay2
    tauxy3 = Fy / Ay3

    Ax2 = pi / 4 * (Dfo ** 2 - Dfi ** 2)
    Ax3 = pi / 4 * (Dfo ** 2 - Dfi ** 2)

    sigmay2 = Fy / Ax2
    sigmay3 = Fy / Ax3

    t2test = True
    t3test = True

    Y2 = 1000000*mp.Yield_stress(material_lug)
    Y3 = 1000000*mp.Yield_stress(material_wall)

    if Y2<sqrt(sigmay2**2+3*tauxy2**2) or Y3<sqrt(sigmay3**2+3*tauxy3**2):
        test = False
        if Y2<sqrt(sigmay2**2+3*tauxy2**2):
            t2test = False
        if Y3 < sqrt(sigmay3 ** 2 + 3 * tauxy3 ** 2):
            t3test = False
    else:
        test = True

    stress2 = sqrt(sigmay2**2+3*tauxy2**2)/1000000
    stress3 = sqrt(sigmay3**2+3*tauxy3**2)/1000000

    return test, stress2, stress3