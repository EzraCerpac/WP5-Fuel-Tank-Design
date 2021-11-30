import math
import numpy as np

# Initial Values
rtg_d = 0.422
rtg_h = 1.14
rtg_m = 56

r_sc = 1.15
h_sc = 4.25

d = 0.1     # To be decided
w_max = 3.14 / 90  # in radians per second

# Torques and Thrusters
F_Thrust = 10
T_scz = 10 * 4 * r_sc
Izz = 1836.7
az = T_scz / Izz

T_scy = 40 * h_sc / 2
Iyy = 5311.6
ay = T_scy / Iyy

# Forces and Moments
Fx = az * (r_sc + d + rtg_h / 2) * rtg_m
Fy = rtg_m * w_max ** 2 * (r_sc + d + 1 / 2 * rtg_h)
Fz = rtg_m * -6 * 9.81
Mx = Fz * rtg_h / 2
My = 1 / 2 * ay * rtg_m * (rtg_d / 2) ** 2
Mz = az * (1 / 4 * rtg_m * rtg_d ** 2 + 1 / 12 * rtg_m * rtg_h ** 2) + 1 / 2 * Fx * rtg_h


class Lug:
    def __init__(self, Fx_=0, Fy_=0, Fz_=0, Mz_=0):
        self.Fx = Fx_
        self.Fy = Fy_
        self.Fz = Fz_
        self.Mz = Mz_
        self.p = np.sqrt(Fy**2+Fz**2)


h = 0.3     # To be decided

lug1 = Lug(Fx/2+My/h, Fy/2-Mx/h, Fz/2, Mz)
lug2 = Lug(Fx/2-My/h, Fy/2+Mx/h, Fz/2, Mz)


