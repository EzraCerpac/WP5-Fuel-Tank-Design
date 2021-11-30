import numpy as np

import LaunchLoads3a, LaunchLoads3b


class FuelTank:
    def __init__(self, R):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 246.52
        self.m2 = 532.47
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m = self.m1 + self.m2
        # Definition for dimentions
        self.R = R
        self.L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2)

        # Random Values
        self.material = "Al-2014"
        self.t1 = 3e-3
        self.t2 = 4e-3

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
    tank = FuelTank(0.5)
    pass


if __name__ == '__main__':
    main()
