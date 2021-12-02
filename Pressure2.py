"""Calculates thickness related to the pressure"""
import MaterialProperties as mp

P = 18.5e5


def t1(R, material):
    t1 = (P * R) / (mp.Yield_stress(material) * 10 ** 6)
    return t1


def t2(R, material):
    t2 = (P * R) / (2 * mp.Yield_stress(material) * 10 ** 6)
    return t2


def Failuret1(t, R, material):
    # Given certain parameters, it says if t is enough or not. True means failure
    sigma1 = (P * R) / t
    m_yield = mp.Yield_stress(material) * 10 ** 6
    if sigma1 > m_yield:
        return True
    else:
        return False


def Failuret2(t, R, material):
    # Given certain parameters, it says if t is enough or not. True means failure
    sigma2 = (P * R) / (2 * t)
    m_yield = mp.Yield_stress(material) * 10 ** 6
    if sigma2 > m_yield:
        return True
    else:
        return False
