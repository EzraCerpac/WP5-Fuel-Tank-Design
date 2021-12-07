from math import exp
from math import sqrt
from math import sin
Xb = 0.8 * 9.81
wb = 100 #got to convert from hz still
wn = sqrt(k/m)
a = ( Xb * wn**2 ) /( wn**2 - wb**2 )
xh = a * exp(labda * t)

xp = a * sin(wb * t)

xt = xp + xh

