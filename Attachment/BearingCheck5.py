from Attachment.Constants import edge_distance_min
import numpy as np
import os


def main(width, D2, stif_num, w):
    # print(f"running {os.path.basename(__file__)}")
    right_x = width / 2 - edge_distance_min * D2
    left_x = -right_x
    mid = (stif_num / 2 - 1) / 2
    if stif_num // 2 > 1:
        vertical_spacing = (w - 2 * edge_distance_min) / (stif_num / 2 - 1)
    else:
        vertical_spacing = 0

    fastener_positions = []
    fastener_x = []
    fastener_z = []

    for i in range(stif_num // 2):
        z = (i - mid) * vertical_spacing
        fastener_positions.append([left_x, z])
        fastener_x.append(left_x)
        fastener_z.append(z)
    for i in range(stif_num // 2):
        z = (i - mid) * vertical_spacing
        fastener_positions.append([right_x, z])
        fastener_x.append(right_x)
        fastener_z.append(z)

    fastener_positions = np.array(fastener_positions)
    fastener_x = np.array(fastener_x)
    fastener_z = np.array(fastener_z)


    A = np.pi * (D2 / 2)**2

    x_cg = sum(fastener_x)
    z_cg = sum(fastener_z)

    return fastener_positions, fastener_x, fastener_z, A, x_cg, z_cg