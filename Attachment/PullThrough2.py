from math import pi, sqrt



def main(Fy, Dfo2, Dfi2, Dfo3, Dfi3, t2, t3, Y2, Y3):
    Ay2 = pi * Dfi2 * t2
    Ay3 = pi * Dfi3 * t3

    tauxy2 = Fy / Ay2
    tauxy3 = Fy / Ay3

    Ax2 = pi / 4 * (Dfo2 ** 2 - Dfi2 ** 2)
    Ax3 = pi / 4 * (Dfo3 ** 2 - Dfi3 ** 2)

    sigmay2 = Fy / Ax2
    sigmay3 = Fy / Ax3



    if Y2<sqrt(sigmay2**2+3*tauxy2**2) or Y3<sqrt(sigmay3**2+3*tauxy3**2):
        test = False
        #if Y2<sqrt(sigmay2**2+3*tauxy2**2):
            #print('In t2')
        #if Y3 < sqrt(sigmay3 ** 2 + 3 * tauxy3 ** 2):
            #print('In t3')
    else:
        test = True

    return test

