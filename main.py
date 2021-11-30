import numpy as np
import MaterialProperties as mp
import LaunchLoads3a, LaunchLoads3b


class FuelTank:
    def __init__(self, R, material):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 393.7
        self.m2 = 850.5
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m = self.m1 + self.m2

        # Definition for dimentions
        self.R = R
        self.L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2)

        # Material
        self.material = material

    def p2(self):
        # t1 for cylinder, t2 for sphere in meters
        self.P = 18.5e5
        self.t1 = (self.P*self.R)/(mp.Yield_stress(self.material)*10**6)
        self.t2 = (self.P*self.R)/(2*mp.Yield_stress(self.material)*10**6)

    def p3a(self):
        self.column_buckling_stress, fail = LaunchLoads3a.main(self.material, self.R, self.L, self.t1)
        if fail:
            print("fail!")


class Spacecraft:
    def __init__(self):
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC


def main():
    SAPPHIRE = Spacecraft()
    # R must be smaller than 0.536 or L=0
    tank = FuelTank(0.4, "Al-2014")
    pass


if __name__ == '__main__':
    main()
