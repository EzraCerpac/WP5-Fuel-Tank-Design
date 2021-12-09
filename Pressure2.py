"""Calculates thickness related to the pressure"""
import MaterialProperties as mp




def t1(R, material, ts, P):
    t_1 = (P * R) / (mp.Yield_stress(material) * 1e6)
    t_2 = ts * (1 / (1 - mp.Poisson_ratio(material)) + 1)
    t = max(t_1, t_2)
    return t


def t2(R, material, P):
    t2 = (P * R) / (2 * mp.Yield_stress(material) * 1e6)
    return t2


def Failuret1(t1, t2, R, material, P):
    # Given certain parameters, it says if t is enough or not. True means failure
    sigma1 = (P * R) / t1
    m_yield = mp.Yield_stress(material) * 1e6
    tmin = t2 * (1 / (1 - mp.Poisson_ratio(material)) + 1)
    if sigma1 > m_yield or t1 < tmin:
        return True
    else:
        return False


def Failuret2(t, R, material, P):
    # Given certain parameters, it says if t is enough or not. True means failure
    sigma2 = (P * R) / (2 * t)
    m_yield = mp.Yield_stress(material) * 1e6
    if sigma2 > m_yield:
        return True
    else:
        return False

# r = np.arange(0.1, 0.52, 0.01)
#    x_ = []
#    for radius in r:
#        tank_v1 = FuelTank(radius, "Ti-6AL")
#        tank_v1.p2()
#        x_.append([radius, tank_v1.massTank])
#    x_ = sorted(x_, key=lambda x:x[1])
#    print(x_)

#t2=t2(0.5,"Al-2014")
#print(t2)
#t1=t1(0.5,"Al-2014",t2)
#print(t1)
#ft1=Failuret1(t1,t2+0.001,0.5,"Al-2014")
#print(ft1)
#ft2=Failuret2(t2,0.5,"Al-2014")
#print(ft2)