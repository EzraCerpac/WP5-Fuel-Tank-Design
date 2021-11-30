import numpy as np
import MaterialProperties as mp
import LaunchLoads3, MassOfAttachments4, TotalMassCalc

class Spacecraft:
    def __init__(self):
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC

        self.a = 5  # Acceleration random value

class FuelTank(Spacecraft):
    def __init__(self, R, material):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 393.7
        self.m2 = 850.5
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m = self.m1 + self.m2

        # Definition for dimensions
        self.R = R
        self.L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2)+2*self.R

        # Material
        self.material = material

    def p2(self):
        # t1 for cylinder, t2 for sphere in meters
        self.P = 18.5e5
        self.t1 = (self.P*self.R)/(mp.Yield_stress(self.material)*10**6)
        self.t2 = (self.P*self.R)/(2*mp.Yield_stress(self.material)*10**6)


    def p3(self):
        self.column_ratio, self.shell_ratio = LaunchLoads3.main(self.material, self.R, self.L, self.t1, self.P, h, self.mass, self.a)
        self.compressive_load = self.mass * self.a

    def p4_find_n(self):
        self.n_attachments, self.attachments_mass = MassOfAttachments4.main(self.compressive_load)

    def p4(self):
        self.attachments_mass = MassOfAttachments4.calc_mass(self.compressive_load, self.n_attachments)

    def massCalc(self):
        self.m_tank = (2 * np.pi * self.R * (
                    self.L - 2 * self.R) * self.t1 + 4 * np.pi * self.R ** 2 * self.t2) * mp.density(self.material)
        self.m_total = TotalMassCalc.main(self.m_tank, self.attachments_mass)



def main():
    SAPPHIRE = Spacecraft()
    # R must be smaller than 0.536 or L=0
    tank = FuelTank(0.4, "Al-2014")
    iteration(tank)


def iteration(tank: FuelTank):
    tank.p2()
    tank.p3()
    tank.p4_find_n()
    tank.massCalc()


if __name__ == '__main__':
    main()
