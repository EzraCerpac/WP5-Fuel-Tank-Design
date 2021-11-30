import LaunchLoads3a, LaunchLoads3b

class FuelTank:
    def __init__(self):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 393.7
        self.m2 = 850.5
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m = self.m1 + self.m2

        # Random Values
        self.material = "Al-2014"
        self.R = 2
        self.L = 5
        self.t1 = 3e-3
        self.t2 = 4e-3


    def p3a(self):
        self.column_buckling_stress, fail = LaunchLoads3a.main(self.material, self.R, self.L, self.t1)
        if fail:
            print("fail!")


class Spacecraft:
    def __init__(self, FuelTank):
        self.FuelTank = FuelTank
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC


def main():
    tank = FuelTank()
    SAPPHIRE = Spacecraft(tank)
    pass


if __name__ == '__main__':
    main()
