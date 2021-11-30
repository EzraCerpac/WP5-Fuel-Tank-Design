import MaterialProperties as mp
import os


def main(A, Resultant, phi_lug, phi_fastener, material_fastener, material_wall, material_lug):
    # print(f"running {os.path.basename(__file__)}")
    # Constants: used random values as i do not know the real values
    TworkingMin = 7  # celcius

    Treference = 15  # celcius
    DeltaMax = TworkingMin - Treference

    E_b = mp.E_mod(material_fastener)
    AlfaFastener = mp.Expansion_cof(material_fastener)
    AlfaWall = mp.Expansion_cof(material_wall)
    AlfaLugPlate = mp.Expansion_cof(material_lug)

    # Force calculations
    F_wall_Fastener = (AlfaWall - AlfaFastener) * (10 ** -6) * DeltaMax * E_b * (10 ** 3) * A * (1 - phi_lug)
    F_LugPlate_fastener = (AlfaLugPlate - AlfaFastener) * (10 ** -6) * DeltaMax * (10 ** 3) * E_b * A * (1 - phi_fastener)

    # updating bearing forces
    Resultant = Resultant + F_LugPlate_fastener + F_wall_Fastener

    return Resultant
