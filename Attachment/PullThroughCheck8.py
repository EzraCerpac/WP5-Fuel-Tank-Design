import numpy as np
from ForcesAndMoments import Mz, Fy
import os
import ForcesAndMoments
import pandas as pd


# def out_of_plain_load(F_y, M_z, A_i, n_f, r_i,s):
#     # Calculation out of plane force
#     F_pi = F_y / n_f
#     F_pMz = M_z * A_i * r_i / s
#     Total_force = float(F_pi + F_pMz)
#     return (Total_force)
#
#
# def main(r, A, n_f):
#     print(f"running {os.path.basename(__file__)}")
#     # initial values
#     numbering = []
#     Results = []
#
#     # sum of areas times r^2
#     r_2 = r ** 2
#     product = r_2 * A
#     summation = np.sum(product)
#
#     # calculating and listing all the forces for the fastners
#     for i in range(len(r)):
#         force = out_of_plain_load(Fy, Mz, A, n_f, r[i], summation)
#         Results.append(force)
#
#     # Sorting array based on force
#     for i in range(len(Results)):
#         numbering.append(i)
#
#     empty_array = np.empty((len(Results), 0), int)
#     empty_array = np.append(empty_array, np.array([Results]).transpose(), axis=1)
#     final_array = np.append(empty_array, np.array([numbering]).transpose(), axis=1)
#     sorted_fastner_forces = np.array(sorted(final_array, key=lambda x: x[0]))
#
#     return sorted_fastner_forces

def main(w, t2, e1, wp):
    l = 3 / 2 * w + t2
    d = w - 2 + e1
    h = wp - 2 * e1
    l1_t1 = (ForcesAndMoments.lug1.Fz * l + ForcesAndMoments.lug1.Fy * d / 2 + (
            ForcesAndMoments.lug1.Fx * l + ForcesAndMoments.lug1.Mz) / h) / (2 * d)
    l1_t2 = (ForcesAndMoments.lug1.Fz * l + ForcesAndMoments.lug1.Fy * d / 2 + (
            -ForcesAndMoments.lug1.Fx * l + ForcesAndMoments.lug1.Mz) / h) / (2 * d)
    l1_b1 = (ForcesAndMoments.lug1.Fz * l - ForcesAndMoments.lug1.Fy * d / 2 + (
            ForcesAndMoments.lug1.Fx * l + ForcesAndMoments.lug1.Mz) / h) / (2 * d)
    l1_b2 = (ForcesAndMoments.lug1.Fz * l - ForcesAndMoments.lug1.Fy * d / 2 + (
            -ForcesAndMoments.lug1.Fx * l + ForcesAndMoments.lug1.Mz) / h) / (2 * d)
    l2_t1 = (ForcesAndMoments.lug2.Fz * l + ForcesAndMoments.lug2.Fy * d / 2 + (
            ForcesAndMoments.lug2.Fx * l + ForcesAndMoments.lug2.Mz) / h) / (2 * d)
    l2_t2 = (ForcesAndMoments.lug2.Fz * l + ForcesAndMoments.lug2.Fy * d / 2 + (
            -ForcesAndMoments.lug2.Fx * l + ForcesAndMoments.lug2.Mz) / h) / (2 * d)
    l2_b1 = (ForcesAndMoments.lug2.Fz * l - ForcesAndMoments.lug2.Fy * d / 2 + (
            ForcesAndMoments.lug2.Fx * l + ForcesAndMoments.lug2.Mz) / h) / (2 * d)
    l2_b2 = (ForcesAndMoments.lug2.Fz * l - ForcesAndMoments.lug2.Fy * d / 2 + (
            -ForcesAndMoments.lug2.Fx * l + ForcesAndMoments.lug2.Mz) / h) / (2 * d)
    lugs = [l1_t1, l1_t2, l1_b1, l1_b2, l2_t1, l2_t2, l2_b1, l2_b2]
    name = ["l1_t1", "l1_t2", "l1_b1", "l1_b2", "l2_t1", "l2_t2", "l2_b1", "l2_b2"]

    lugs_df = pd.DataFrame(data=lugs, columns=["Lugs"])
    names_df = pd.DataFrame(data=name, columns=["Name"])
    lugs_df = lugs_df.join(names_df)
    lugs_df = lugs_df.sort_values(by=["Lugs"])
    lugs_df = lugs_df.reset_index()

    max = lugs_df.Lugs[7]

    return lugs_df, max