from math import pi, exp
import MaterialProperties as mp

def column(material: str, R, L, t1):
    E = mp.E_mod(material)
    I = pi * R**3 * t1
    A = pi * R**2

    sigma_cr = (pi**2 * E * I) / (A * L**2)
    return sigma_cr


def shell(material: str, p, R, L, t1, h):
    E = mp.E_mod(material)
    v = mp.Poisson_ratio(material)
    Q = p/E * (R/t1)**2
    k = h + 12/pi**4 * L**4/(R**2*t1**2) * (1-v**2)/h

    crit_stress = (1.983-0.983*exp(-23.14*Q)) * k * pi**2*E/(12*(1-v**2)) * (t1/L)**2

    return crit_stress