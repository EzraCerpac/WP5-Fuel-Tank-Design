import pandas as pd
import numpy as np


def Analysis1(path):
    df = pd.read_csv(path)

    df = df[df.d_out > 2.2]
    df = df[df.ms1 >= 0]
    df = df[df.ms2 >= 0]
    df = df[df.ms3 >= 0]
    df = df[df.ms4 >= 0]
    df = df[df.ms5 >= 0]
    df = df.sort_values(by=['weight'])
    df = df.reset_index()

    t_opt = df.t[0]
    w_opt = df.w[0]
    D1_opt = df.D1[0]
    t2_opt = df.t2[0]
    d_out_opt = df.d_out[0]
    return t_opt, w_opt, D1_opt, t2_opt, d_out_opt


def Analysis2(path):
    df = pd.read_csv(path)

    df = df[df.d_out > 3.2]
    df = df[df.ms1 >= 0]
    df = df[df.ms2 >= 0]
    df = df[df.ms3 >= 0]
    df = df[df.ms4 >= 0]
    df = df[df.ms5 >= 0]
    df = df.sort_values(by=['weight'])
    df = df.reset_index()

    t_opt = df.t[0]
    w_opt = df.w[0]
    D1_opt = df.D1[0]
    t2_opt = df.t2[0]
    d_out_opt = df.d_out[0]
    return t_opt, w_opt, D1_opt, t2_opt, d_out_opt
