from math import pi, exp
import MaterialProperties as mp

def column(material: str, R, L, t1):
    E = mp.E_mod(material)
    I = pi * R**3 * t1
    A = 2*pi*R*t1

    sigma_cr = (pi**2 * E * I) / (A * L**2)
    return sigma_cr


def shell(material: str, p, R, L, t1, h):
    E = mp.E_mod(material)
    v = mp.Poisson_ratio(material)
    Q = p/E * (R/t1)**2
    k = h + 12/pi**4 * L**4/(R**2*t1**2) * (1-v**2)/h

    crit_stress = (1.983-0.983*exp(-23.14*Q)) * k * pi**2*E/(12*(1-v**2)) * (t1/L)**2

    return crit_stress

def launch_loads(m, a, R, t1):
    F = m*a
    A = 2*pi*R*t1

    stress = F/A

    return stress

def main(material: str, R, L, t1, p, h, m, a):
    column_ratio = launch_loads(m, a, R, t1)/column(material, R, L, t1)
    shell_ratio = launch_loads(m, a, R, t1)/shell(material, p, R, L, t1, h)

    return column_ratio, shell_ratio

def thickness_from_stress(m, a, R, stress):
    F = m * a
    A = F / stress
    t1 = A / (2*pi*R)
    return t1

def stress_failure_check(material: str, R, L, t1, p, h, m, a):
    column_cr = column(material, R, L, t1)
    shell_cr = shell(material, p, R, L, t1, h)
    stress = launch_loads(m, a, R, t1)
    fail_column = stress >= column_cr
    fail_shell = stress >= shell_cr
    fail = fail_column or fail_shell
    return fail, min(column_cr, shell_cr)

if __name__ == '__main__':
    for t in range(1, 100):
        print(shell("Ti-6AL", 1, 1, 1, t, 4))
