import numpy as np
import MaterialProperties as mp
import Pressure2, LaunchLoads3, MassOfAttachments4, TotalMassCalc


class Spacecraft:
    def __init__(self):
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC

        self.a_axial = 7.5 * 9.81
        self.a_lateral = 2.5 * 9.81


class FuelTank:
    def __init__(self, R, material):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 393.7
        self.m2 = 850.5
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m = self.m1 + self.m2  # is this the mass of the fuel? -Ezra

        # Definition for dimensions
        self.R = R
        self.L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2) + 2 * self.R

        # Material
        self.material = material

        self.n_attachments = 4 # Random starting value

        self.a_axial = 7.5 * 9.81
        self.a_lateral = 2.5 * 9.81

    def p2(self):
        # t1 for cylinder, t2 for sphere in meters
        self.P = 18.5e5
        self.t1 = Pressure2.t1(self.R, self.material)
        self.t2 = Pressure2.t2(self.R, self.material)
        # starting mass
        self.mass = TotalMassCalc.tankMass(self.material, self.R, self.L, self.t1, self.t2, self.m)

    def p2_pressure_check(self):
        t1_fail = Pressure2.Failuret1(self.t1, self.R, self.material)
        t2_fail = Pressure2.Failuret1(self.t2, self.R, self.material)
        fail = t1_fail or t2_fail
        if fail:
            self.t1 = Pressure2.t1(self.R, self.material)
            self.t2 = Pressure2.t2(self.R, self.material)
            #print(self.t1)
        return fail

    def p3(self):
        fail, self.sigma_cr = LaunchLoads3.stress_failure_check(self.material, self.R, self.L, self.t1, self.P,
                                                           self.n_attachments, self.mass, self.a_axial)
        if fail:
            self.t1 = LaunchLoads3.thickness_from_stress(self.mass, self.a_axial, self.R, self.sigma_cr)
        self.compressive_load = self.mass * self.a_axial



    def p4_find_n(self):
        self.n_attachments, self.attachments_mass = MassOfAttachments4.main(self.compressive_load)

    def p4(self):
        self.attachments_mass = MassOfAttachments4.calc_mass(self.compressive_load, self.n_attachments)

    def massCalc(self):
        self.mass = TotalMassCalc.main(self.material, self.R, self.L, self.t1, self.t2, self.attachments_mass, self.m)

    def printAll(self):
        print("\n##########################")
        print("\nThe Parameters:\n")
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items()))
        print("\n##########################")



def main():
    SAPPHIRE = Spacecraft()
    # R must be smaller than 0.536 or L=0
    tank_v1 = FuelTank(0.4, "Ti-6AL")
    firstIteration(tank_v1)
    tank_v1.printAll()


def firstIteration(tank: FuelTank):
    tank.p2()
    tank.p3()
    tank.p4_find_n()
    thicknessIteration(tank)


def thicknessIteration(tank: FuelTank):
    fail = True
    while fail:
        tank.massCalc()
        starting_mass = tank.mass
        tank.p3()
        tank.p4()
        tank.massCalc()
        new_mass = tank.mass
        massIteration(tank, starting_mass, new_mass)
        fail = tank.p2_pressure_check()




def massIteration(tank: FuelTank, old_mass, new_mass):
    while (abs(new_mass - old_mass)) / old_mass > 0.001:
        old_mass = new_mass
        tank.p3()
        tank.p4()
        tank.massCalc()
        new_mass = tank.mass
        print(tank.mass, tank.sigma_cr)



if __name__ == '__main__':
    main()
