from Attachment import LugDesign3 as ld
from Attachment import MaterialProperties as mp
from Attachment import FastenerPattern4, BearingCheck5, BearingCheck6, BearingCheck7, PullThroughCheck8, PullThrough9
from Attachment import FastenerType10, ThermalStressCheck11
from math import pi
from Attachment.SafetyFactors import calcMS
import pandas as pd
import numpy as np
from Attachment import AnalysisCSV as acsv


class RTGattachment:
    def __init__(self, material: str, t1, w, D1, t2, d_out):
        """Starting values"""
        self.backup_plate_material = "metal"
        self.specific_material = material
        self.fastener_outer_diameter = d_out  # mm
        self.t3 = 1.4  # mm

        # From p3 combinations
        self.t1 = t1
        self.w = w
        self.D1 = D1
        self.h = w
        self.h2 = 0.3

        # Changed immediately in p4
        self.width = 0

        # Arbitrary value for p7
        self.t2 = t2

        # For p11
        self.wall_material = "Al-2014"
        self.fastener_material = "Al-7075"

    def checkMaterialBearingStrength(self, material):
        BearingCheck7.BearingCheck(material, self.sigma_br)

    def calcSigma_br(self):
        BearingCheck7.calcSigma_br(self.P, self.t2, self.D2)

    def p3(self):
        #     self.t1, self.w, self.D1, self.h, self.h2, self.mass_flange, self.bendstress,  self.combinations = ld.ChooseLug(self.specific_material)
        self.mass_flange, self.bendstress = ld.mass_stress(self.specific_material, self.t1, self.w, self.D1)

    def p4(self, new_width):
        self.stif_num, self.D2, self.width = FastenerPattern4.main(new_width, self.backup_plate_material, self.width,
                                                                   self.h, self.t1, self.w)

    def p5(self):
        self.fastener_positions, self.fastener_x, self.fastener_z, self.A, self.x_cg, self.z_cg = BearingCheck5.main(
            self.width, self.D2, self.stif_num, self.w)

    def p6(self):
        self.F_inplaneX, self.F_inplaneZ, self.F_inplaneMy, self.fastener_distance = BearingCheck6.main(
            self.fastener_positions, self.x_cg, self.z_cg, self.stif_num, self.A)

    def p7(self):
        self.P, self.sigma_br = BearingCheck7.main(self.t2, self.F_inplaneX, self.F_inplaneZ, self.F_inplaneMy,
                                                   self.fastener_x, self.fastener_z, self.fastener_distance, self.D2)

    def p7_choose_t2(self):
        self.P, self.sigma_br, self.t2 = BearingCheck7.find_t2(self.F_inplaneX, self.F_inplaneZ, self.F_inplaneMy,
                                                               self.fastener_x, self.fastener_z, self.fastener_distance,
                                                               self.D2,
                                                               self.specific_material)

    def p8(self):
        self.sorted_fastner_force, self.maxFastener = PullThroughCheck8.main(self.w, self.t2, 1.5 * self.D2, self.width)

    def p9(self):
        self.PullThrough_test, self.stress2, self.stress3 = PullThrough9.main(self.maxFastener,
                                                                              self.fastener_outer_diameter, self.D2,
                                                                              self.t2,
                                                                              self.t3,
                                                                              self.specific_material,
                                                                              self.specific_material)

    def p10(self):
        self.phi_lug, self.phi_sc = FastenerType10.main(self.fastener_outer_diameter, self.D2, self.t2, self.t3, 10, 10,
                                                        self.specific_material, self.specific_material,
                                                        self.specific_material)  # Subject to change

    def p11(self):
        self.P = ThermalStressCheck11.main(self.A, self.P, self.phi_lug, self.phi_sc, self.fastener_material,
                                           self.wall_material, self.specific_material)

    def calcWeight(self):
        """Calculate the weight of the entire lug"""
        # print("\nCalculating weight:")
        backup = (self.width * self.w - self.stif_num * self.A) * self.t2 * 1e-9 * mp.density(
            self.specific_material) * 1000
        flanges = 2 * (self.mass_flange + self.w ** 2 * self.t1 * 1e-9 * mp.density(self.specific_material)) * 1000
        fasteners = self.stif_num * 1e-9 * mp.density(self.fastener_material) * 1000 * 2 * self.t2 * pi * (
                self.fastener_outer_diameter / 2) ** 2
        self.total_weight = backup + flanges + fasteners
        # print(f"{backup} + {flanges} + {fasteners} = {self.total_weight} in grams")

    def printAll(self):
        print("\n##########################")
        print("\nThe Parameters:\n")
        attrs = vars(self)
        print('\n'.join("%s: %s" % item for item in attrs.items()))
        print("\n##########################")


def Iteration(attachment):
    # print(
    #     f"\nStarting to run iteration for {attachment.__class__.__name__} made out of {attachment.specific_material}:\n")
    attachment.p3()
    attachment.p4(True)
    attachment.p5()
    attachment.p6()
    attachment.p7()  # Changed
    # attachment.checkMaterialBearingStrength(attachment.specific_material)
    attachment.p8()
    attachment.p9()
    attachment.p10()
    # print(f"attachment.P =\n{attachment.P}")
    attachment.p11()
    # print(f"attachment.P = {attachment.P}\n")
    # attachment.checkMaterialBearingStrength(attachment.specific_material)
    attachment.calcWeight()


def margins(attachment):
    # print(f"\nSafety factors of attachment mad from {attachment.specific_material}:")
    #
    # print(f"Bendstress: {calcMS(mp.Yield_stress(attachment.specific_material) * 1e6, attachment.bendstress)}")
    # attachment.calcSigma_br()
    # print(f"Bearing Strength Backup Plate: {calcMS(mp.F_bry(attachment.specific_material), attachment.sigma_br)}")
    # print(f"Bearing Strength Wall: {calcMS(mp.F_bry(attachment.wall_material), attachment.sigma_br)}")
    # print(f"Pull Through Wall: {calcMS(mp.Yield_stress(attachment.wall_material), attachment.stress3)}")
    # print(f"Pull Through Backup Plate: {calcMS(mp.Yield_stress(attachment.specific_material), attachment.stress2)}")

    ms1 = calcMS(mp.Yield_stress(attachment.specific_material) * 1e6, attachment.bendstress)
    ms2 = calcMS(mp.F_bry(attachment.specific_material), attachment.sigma_br)
    ms3 = calcMS(mp.F_bry(attachment.wall_material), attachment.sigma_br)
    ms4 = calcMS(mp.Yield_stress(attachment.wall_material), attachment.stress3)
    ms5 = calcMS(mp.Yield_stress(attachment.specific_material), attachment.stress2)
    return ms1, ms2, ms3, ms4, ms5


def combCSV(material):
    combinations = ld.LugComb(material)
    t = np.arange(0.7, 0.8, 0.05)
    d_options = np.arange(0.1, 10, 0.2)
    df = pd.DataFrame(columns=["t", "w", "D1", "t2", "d_out", "ms1", "ms2", "ms3", "ms4", "ms5", 'weight'])
    for t2 in t:
        print("Wait...")
        for d_out in d_options:
            for index, row in combinations.iterrows():
                attachment_v1 = RTGattachment(material, row["t"], row["w"], row["diameter"], t2, d_out)
                Iteration(attachment_v1)
                ms1, ms2, ms3, ms4, ms5 = margins(attachment_v1)
                _ = {'t': row["t"], 'w': row["w"], 'D1': row["diameter"], 't2': t2, 'd_out': d_out, 'ms1': ms1,
                     'ms2': ms2, 'ms3': ms3, 'ms4': ms4, 'ms5': ms5, 'weight': attachment_v1.total_weight}
                df = df.append(_, ignore_index=True)

    df.to_csv(r'C:\Users\ricke\Desktop\Iterations3.csv')
    print("Done")


def main():
    material = "steel-4130"
    # First case, used the minimum weight from p3
    combinations = ld.LugComb(material)
    attachment_v1_steel = RTGattachment(material, combinations.t[0], combinations.w[0], combinations.diameter[0], 0.8,
                                        10)
    Iteration(attachment_v1_steel)
    print(f"The first case for {material}:")
    attachment_v1_steel.printAll()
    print(margins(attachment_v1_steel))
    print("---------------------------------------------------------")
    # Optimized case
    t_opt, w_opt, D1_opt, t2_opt, d_out_opt = acsv.Analysis1('Steel-4130(Iterations).csv')
    attachment_opt_steel = RTGattachment(material, t_opt, w_opt, D1_opt, t2_opt, d_out_opt)
    Iteration(attachment_opt_steel)
    print(f"The optimum case for {material}:")
    attachment_opt_steel.printAll()
    print(margins(attachment_opt_steel))
    print("---------------------------------------------------------")
    material = "Al-2014"
    # First case, used the minimum weight from p3
    combinations = ld.LugComb(material)
    attachment_v1_al = RTGattachment(material, combinations.t[0], combinations.w[0], combinations.diameter[0], 0.8, 10)
    Iteration(attachment_v1_al)
    print(f"The first case for {material}:")
    attachment_v1_al.printAll()
    print(margins(attachment_v1_al))
    print("---------------------------------------------------------")
    # Optimized case
    t_opt, w_opt, D1_opt, t2_opt, d_out_opt = acsv.Analysis2('Al-2014(Iterations).csv')
    attachment_opt_al = RTGattachment(material, t_opt, w_opt, D1_opt, t2_opt, d_out_opt)
    Iteration(attachment_opt_al)
    print(f"The optimum case for {material}:")
    attachment_opt_al.printAll()
    print(margins(attachment_opt_al))


def findWeightAttachment():
    material = "steel-4130"
    # First case, used the minimum weight from p3
    combinations = ld.LugComb(material)
    attachment_v1_steel = RTGattachment(material, combinations.t[0], combinations.w[0], combinations.diameter[0], 0.8,
                                        10)
    Iteration(attachment_v1_steel)
    print(f"The first case for {material}:")
    attachment_v1_steel.printAll()
    print(margins(attachment_v1_steel))
    print("---------------------------------------------------------")
    # Optimized case
    t_opt, w_opt, D1_opt, t2_opt, d_out_opt = acsv.Analysis1('Attachment/Al-2014(Iterations).csv')
    attachment_opt_steel = RTGattachment(material, t_opt, w_opt, D1_opt, t2_opt, d_out_opt)
    Iteration(attachment_opt_steel)
    print(f"The optimum case for {material}:")
    attachment_opt_steel.printAll()
    print(margins(attachment_opt_steel))
    return attachment_opt_steel.total_weight


if __name__ == '__main__':
    main()

    # print("\nStart of analysis")
    # print(attachment_v1.sigma_br)
