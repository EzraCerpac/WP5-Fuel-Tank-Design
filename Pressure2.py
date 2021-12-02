"""Calculates thickness related to the pressure"""
import MaterialProperties as mp

P = 18.5e5



def t2(R, material):
    t2 = (P * R) / (2 * mp.Yield_stress(material) * 10 ** 6)
    return t2

def t1(t2, material):
    #t1 = (P * R) / (mp.Yield_stress(material) * 10 ** 6)
    t1 = t2 * (1/(1-mp.Poisson_ratio(material)) + 1)
    return t1


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

#r = np.arange(0.1, 0.52, 0.01)
#    x_ = []
#    for radius in r:
#        tank_v1 = FuelTank(radius, "Ti-6AL")
#        tank_v1.p2()
#        x_.append([radius, tank_v1.massTank])
#    x_ = sorted(x_, key=lambda x:x[1])
#    print(x_)