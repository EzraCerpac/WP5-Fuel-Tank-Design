from Attachment.Constants import edge_distance_min
from math import pi
import os


def minmaxD2(n, w, s_min, s_max, e1=edge_distance_min):
    # vertical distance fitment
    D2_max_v = w / (2 * e1 + s_min * (n - 1))
    D2_min_v = w / (2 * e1 + s_max * (n - 1))
    return D2_max_v

def main(new_width, material, width, h, t1, w):
    # print(f"running {os.path.basename(__file__)}")
    if material == "metal":
        fastener_spacing_min = 2
        fastener_spacing_max = 3
    elif material == "composite":
        fastener_spacing_min = 4
        fastener_spacing_max = 5

    # horizontal distance fitment
    # h_space = (width - h - 2 * t1) / 2
    # D2_max_h = (h_space - edge_distance_min) * 2
    D2_max_h = (width - h - 2*t1) / (2*edge_distance_min + 1)


    options = []
    for i in range(2, 5):
        options.append([i, minmaxD2(i, w, fastener_spacing_min, fastener_spacing_max)])

    if not new_width:
        for option in options:
            if option[1] > D2_max_h:
                option[1] = D2_max_h

    max_area = 0
    for option in options:
        stif_num = option[0] * 2
        area = stif_num * 1/2 * pi * (option[1]/2)**2
        if area >= max_area:
            max_area = area
            best = option

    if new_width:
        width = h + 2 * (t1 + (edge_distance_min + 1/2) * best[1])


    stif_num = best[0] * 2
    D2 = best[1]
    return stif_num, D2, width


# if __name__ == '__main__':
#     attachment.stif_num, attachment.D2 = main()
#     print(attachment.stif_num, attachment.D2)
