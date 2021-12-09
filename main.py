import numpy as np
import Pressure2, LaunchLoads3, MassOfAttachments4, TotalMassCalc
import NaturalFreq6 as nf
import MaterialProperties as mp
import displacement565 as dsp

class Spacecraft:
    def __init__(self):
        self.h = 4.25  # Height of SC
        self.d = 2.3  # Inner Diameter of SC

        self.a_axial = 7.5 * 9.81
        self.a_lateral = 2.5 * 9.81

        self.freq = nf.SimplifiedNatFreq(mp.E_mod("Al-2024"), 4.25, 0.00144, 1791, 1.15)


class FuelTank:
    def __init__(self, R, material):
        # 1 refers to fuel, 2 to oxidizer
        self.V1 = 0.28
        self.V2 = 0.367
        self.m1 = 246.52 # new value
        self.m2 = 532.47 #new
        # Assume 1 large tank
        self.V = self.V1 + self.V2
        self.m_fuel = self.m1 + self.m2


        # Definition for dimensions
        self.R = R
        self.L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2) + 2 * self.R

        # Material
        self.material = material

        self.n_attachments = 4  # Random starting value

        # spacecraft values
        self.a_axial = 7.5 * 9.81
        self.a_lateral = 2.5 * 9.81
        self.sc_mass_without_tank = 1791.37 - 246.52 - 532.47 - 7.52 - 19.09

    def p2(self):
        # t1 for cylinder, t2 for sphere in meters
        self.P = 18.5e5
        self.t2 = Pressure2.t2(self.R, self.material)
        self.t1 = Pressure2.t1(self.R, self.material, self.t2)
        # starting mass
        self.mass = TotalMassCalc.tankMass(self.material, self.R, self.L, self.t1, self.t2) + self.sc_mass_without_tank + self.m_fuel


    def p2_pressure_check(self):
        t1_fail = Pressure2.Failuret1(self.t1, self.t2, self.R, self.material)
        t2_fail = Pressure2.Failuret2(self.t2, self.R, self.material)
        fail = t1_fail or t2_fail
        if fail:
            self.t2 = Pressure2.t2(self.R, self.material)
            self.t1 = Pressure2.t1(self.R, self.material, self.t2)
        return fail

    def p3(self):
        self.n_attachments = LaunchLoads3.check_h(self.material, self.R, self.L, self.t1, self.P)
        change, self.sigma_cr = LaunchLoads3.stress_failure_check(self.material, self.R, self.L, self.t1, self.P,
                                                                  self.n_attachments, self.mass, self.a_axial)
        if True:
            ratio = 0
            while abs(ratio - 1) > 0.01:
                column_ratio, shell_ratio = LaunchLoads3.main(self.material, self.R, self.L, self.t1, self.P,
                                                              self.n_attachments, self.mass, self.a_axial)
                ratio = max(column_ratio, shell_ratio)
                # self.t1 *= max(column_ratio, shell_ratio)
                R = self.R * ratio**(1/10)
                L = (-4 * np.pi * self.R ** 3 + 3 * self.V) / (3 * np.pi * self.R ** 2) + 2 * self.R
                mass = TotalMassCalc.tankMass(self.material, R, L, self.t1,
                                                   self.t2) + self.sc_mass_without_tank + self.m_fuel
                if mass < self.mass:
                    self.R = R
                    self.L = L
                    self.mass = mass
                    print(self.R, self.mass)
                else:
                    break
        self.compressive_load = self.mass * self.a_axial

    # def p4_find_n(self):
    #     self.n_attachments, self.attachments_mass = MassOfAttachments4.main(self.compressive_load)

    def p4(self):
        self.attachments_mass = MassOfAttachments4.calc_mass(self.compressive_load, self.n_attachments)

    def p6(self):
        self.freq, self.k = nf.DistNatFreq(mp.E_mod(self.material), self.L, self.t1, self.mass, self.R)

    def massCalc(self):
        self.massTank = TotalMassCalc.tankMass(self.material, self.R, self.L, self.t1, self.t2)
        self.mass = TotalMassCalc.totalMass(self.material, self.R, self.L, self.t1, self.t2, self.attachments_mass,
                                            self.m_fuel, self.sc_mass_without_tank)
        self.mass_tank_fueled = self.m_fuel + self.massTank

    def Displacement(self):
        wn = dsp.wn(self.k, self.mass)
        a = dsp.a(wn)
        dsp.forloop(a,wn)
        dsp.forloop2(wn)



    def printAll(self):
        print("\n##########################")
        print("\nThe Parameters:\n")
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items()))
        print("\n##########################")



def main():
    SAPPHIRE = Spacecraft()
    # R must be smaller than 0.536 or L=0 (0.5 is the best)
    tank_v1 = FuelTank(0.5, "Ti-6AL")
    firstIteration(tank_v1)
    tank_v1.printAll()
    print(SAPPHIRE.freq)


def firstIteration(tank: FuelTank):
    print(f"Running Iterations for {tank.__class__.__name__}:")
    tank.p2()
    tank.p3()
    tank.p4()
    thicknessIteration(tank)
    tank.p6()
    tank.Displacement()


def thicknessIteration(tank: FuelTank):
    number_of_iterations = 0
    fail = True
    while fail:
        number_of_iterations += 1
        tank.massCalc()
        starting_mass = tank.mass
        tank.p3()
        tank.p4()
        tank.massCalc()
        new_mass = tank.mass
        massIteration(tank, starting_mass, new_mass)
        fail = tank.p2_pressure_check()
    print(f"\nRan the thickness iteration {number_of_iterations} times")


def massIteration(tank: FuelTank, old_mass, new_mass):
    number_of_iterations = 1
    while (abs(new_mass - old_mass)) / old_mass > 0.0001:
        print(f"Mass iteration {number_of_iterations}: mass = {tank.mass}")
        number_of_iterations += 1
        old_mass = new_mass
        tank.p3()
        tank.p4()
        tank.massCalc()
        new_mass = tank.mass
    print(f"\n  Ran the mass iteration {number_of_iterations} times")
    tank.p2()


if __name__ == '__main__':
    main()
