import numpy as np

class FuelTank:
    def __init__(self, R):
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
        self.L = (-4*np.pi*self.R**3+3*self.V)/(3*np.pi*self.R**2)

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
