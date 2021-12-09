from math import exp
from math import sqrt
from math import sin
from math import tan
from math import cos
from math import pi
import matplotlib.pyplot as plt

#givens
Xb = 0.8 * 9.81
wb = 100*pi*2

labda = 1

#calculating the amplitude
def a(wn):
    a = (Xb) / ((wn ** 2) - (wb ** 2))
    return a


#particular, general and total solution

def total_solution(t,wb,a,wn):
    xh = -(Xb) / (((wn ** 2) - (wb ** 2))*wn) *sin(wn*t)*wb
    xp = a * sin(wb * t)
    xt = xp + xh
    return xt

def wn(k,m):
    wn = sqrt(k/m)
    print("This is omega n",wn)
    return wn

def forloop(a,wn):
    t = 0
    results = []
    time = []

    for i in range(0, 100):
        solution = total_solution(t, wb, a, wn)
        results.append(solution)
        time.append(t)
        t = t + 0.001

    plt.plot(time, results)
    plt.show()




#changing base frequency, needs to go between 0 and 100 Hz

def A(wn, wc):
    A = (Xb) / (wn ** 2 - wc ** 2)
    return A


def forloop2(wn):
    wc = 0
    results2 = []
    wc_list = []
    calc = int(100*pi*2)
    for i in range(0, calc):
        solution2 = A(wn, wc)
        results2.append(solution2)
        wc_list.append(wc)
        wc = wc + 0.1

    plt.plot(wc_list, results2)
    plt.show()



