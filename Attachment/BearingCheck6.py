from ForcesAndMoments import Fx, Fy, Fz, Mx, My, Mz
import numpy as np
import os


# creating an array of the distances to cg

def main(fastener_positions, x_cg, z_cg, stif_num, A):
    # print(f"running {os.path.basename(__file__)}")
    fastener_distance = []

    for coordinate in fastener_positions:
        r = np.sqrt((coordinate[0] - x_cg) ** 2 + (coordinate[1] - z_cg) ** 2)
        fastener_distance.append(r)

    fastener_distance = np.array(fastener_distance)

    # sum of distances to cg:

    sum_r = 0

    for i in range(0, len(fastener_distance)):
        sum_r = sum_r + fastener_distance[i]

    sum_r2 = 0

    for i in range(0, len(fastener_distance)):
        sum_r2 = sum_r2 + (fastener_distance[i]) ** 2

    # Calculations
    F_inplaneX = Fx / stif_num
    F_inplaneZ = Fz / stif_num

    F_inplaneMy = [My * A * r / (A * sum_r2) for r in fastener_distance]

    return F_inplaneX, F_inplaneZ, F_inplaneMy, fastener_distance
