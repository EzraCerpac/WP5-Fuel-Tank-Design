from math import pi
import MaterialProperties as mp

def main(material: str, R, L, t1):
    E = mp.E_mod(material)
    I = pi * R**3 * t1
    A = pi * R**2

    sigma_cr = (pi**2 * E * I) / (A * L**2)
    return sigma_cr