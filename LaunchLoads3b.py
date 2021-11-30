from math import pi, exp

def main(E, v, p, R, L, t1, h):
    Q = p/E * (R/t1)**2
    k = h + 12/pi**4 * L**4/(R**2*t1**2) * (1-v**2)/h

    crit_stress = (1.983-0.983*exp(-23.14*Q)) * k * pi**2*E/(12*(1-v**2)) * (t1/L)**2

    return crit_stress