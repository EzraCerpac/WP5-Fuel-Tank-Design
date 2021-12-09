from math import exp
from math import sqrt
from math import sin
from math import tan
import matplotlib.pyplot as plt

#givens
Xb = 0.8 * 9.81
wb = 100 #got to convert from hz still

labda = 1

#calculating the amplitude
def a(wn):
    a = (Xb * wn ** 2) / (wn ** 2 - wb ** 2)
    return a


#particular, general and total solution

def total_solution(t,wb,a,labda,wn):
    xh = (wn*Xb)/(wn**2 - wb**2) * sin(wb*t)*tan(wn*t)
    xp = a * sin(wb * t)
    xt = xp + xh
    return xt

def wn(k,m):
    wn = sqrt(k/m)
    return wn

def forloop(a):
    t = 0
    results = []
    time = []

    for i in range(0, 100):
        solution = total_solution(t, wb, a, labda, wn)
        results.append(solution)
        time.append(t)
        t = t + 0.1

    plt.plot(time, results)
    plt.show()




#changing base frequency, needs to go between 0 and 100 Hz
# A = ( wn**2 * Xb ) / ( wn**2 - wc**2 )

