import numpy as np
import pandas as pd
import ForcesAndMoments
import MaterialProperties as mp


def lug(kty, sty, a, t):
    # force inputs
    fz = abs(ForcesAndMoments.lug1.Fz / 2 * 7.233)

    abr = fz / (kty * sty)  # trans yield strength used bc more critical for shear

    diameter = abr / t

    aav = a * abr

    w_ = 1 / 12 * (12 * aav + 6 * diameter + 3 * np.sqrt(2) * diameter + np.sqrt(3) * np.sqrt(
        48 * aav ** 2 - 16 * aav * diameter + 8 * np.sqrt(2) * aav * diameter + 18 * diameter ** 2 - 12 * np.sqrt(
            2) * diameter ** 2))
    return [a, kty, sty, t, w_, diameter]


def LugComb(material):
    s_y = mp.Yield_stress(material)
    rho = mp.density(material) * 1e-9
    t_min = 0.001
    t_max = 0.1
    # Options for lug configuration
    data = []
    a = np.arange(0.01, 1.4, 0.001)
    t = np.arange(t_min, t_max, 0.005) * 39.7

    for i in a:
        for k in t:
            kty = -0.000285541 + 1.36311 * i - 0.327104 * (i ** 2)
            x = lug(kty, s_y * 145, i, k)
            data.append(x)

    data = np.array(data)

    # Data Frame creation
    df = pd.DataFrame(data=data, columns=["a", "kty", "sty", "t", "w", "diameter"])

    # Conversion to imperial units
    df.t = df.t * 25.4
    df.w = df.w * 25.4
    df.diameter = df.diameter * 25.4

    # Arbitrary weight
    weight = (df.t * df.w ** 2 - (np.pi * df.diameter ** 2 / 4 * df.t)) * rho
    df2 = pd.DataFrame(data=weight, columns=["weight"])
    df3 = df.join(df2)

    # Calculation of bending stresses
    Mx = 2208
    Mz = 1.45
    h_z = ForcesAndMoments.h  # Vertical distance between lugs
    ixx = 4 * (df3.t / 1000 * (df3.w / 1000) ** 3 / 12 + df3.w / 1000 * df3.t / 1000 * (h_z / 2) ** 2)
    izz = 4 * (df3.w / 1000 * (df3.t / 1000) ** 3 / 12 + df3.w / 1000 * df3.t / 1000 * (
            df3.w / 1000 / 2 + df3.t / 1000 / 2) ** 2)
    sigma = (Mx * izz * (h_z / 2 + df3.w / 1000/2) + Mz * ixx * (df3.w / 1000 / 2 + df3.t / 1000)) / (ixx * izz)
    dfixx = pd.DataFrame(data=ixx, columns=["ixx"])
    dfizz = pd.DataFrame(data=izz, columns=["izz"])
    dfsigma = pd.DataFrame(data=sigma, columns=["sigma"])
    df3 = df3.join(dfixx)
    df3 = df3.join(dfizz)
    df3 = df3.join(dfsigma)

    # Data processing
    df3 = df3[weight > 0]
    df3 = df3[df3.w >= df3.t]
    df3 = df3[df3.w > df3.diameter]
    df3 = df3[df3.sigma < (df3.sty / 145 * 1e6)]
    df3 = df3[df3.diameter <= 0.7*df3.w]
    w_arrange = df3.sort_values(by=['weight'])
    w_arrange = w_arrange.reset_index()
    comb = w_arrange[["t", "w", "diameter", "weight", "sigma"]]
    return comb

    # # Best option
    # t_ = w_arrange.t[0]
    # w_ = w_arrange.w[0]
    # d_ = w_arrange.diameter[0]
    # h_ = w_
    # h2_ = h_z
    # weight_ = w_arrange.weight[0]
    # sigma = w_arrange.sigma[0]
    #
    # # Combinations
    # comb = w_arrange[["t", "w", "diameter", "sigma"]]
    #
    # return t_, w_, d_, h_, h2_, weight_, sigma, comb


def mass_stress(material, t, w, d):
    rho = mp.density(material) * 1e-9
    # Arbitrary weight
    weight = (t * w ** 2 - (np.pi * d ** 2 / 4 * t)) * rho

    # Calculation of bending stresses
    Mx = 2208
    Mz = 1.45
    h_z = ForcesAndMoments.h  # Vertical distance between lugs
    ixx = 4 * (t / 1000 * (w / 1000) ** 3 / 12 + w / 1000 * t / 1000 * (h_z / 2) ** 2)
    izz = 4 * (w / 1000 * (t / 1000) ** 3 / 12 + w / 1000 * t / 1000 * (
            w / 1000 / 2 + t / 1000 / 2) ** 2)
    sigma = (Mx * izz * (h_z / 2 + w / 1000 / 2) + Mz * ixx * (w / 1000 / 2 + t / 1000)) / (ixx * izz)

    return weight, sigma
# Testing
# print("For average, values are ", ChooseLug())
# print("For 356-T6, values are ", ChooseLug(s_y=165, rho=2.67e-6))
# print("For 4130/8630 steel, values are ", ChooseLug(s_y=435, rho=7.85e-6))
# print("For 2024-T3, values are ", ChooseLug(s_y=345, rho=2.78e-6))
# print("For 2014-T6, values are ", ChooseLug(s_y=414, rho=2.8e-6))
