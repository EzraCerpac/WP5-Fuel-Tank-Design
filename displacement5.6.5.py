from math import exp
from math import sqrt
from math import sin

#givens
Xb = 0.8 * 9.81
wb = 100 #got to convert from hz still
wn = sqrt(k/m)

#calculating the amplitude
a = ( Xb * wn**2 ) /( wn**2 - wb**2 )

#particular, general and total solution
xh = a * exp(labda * t)
xp = a * sin(wb * t)

xt = xp + xh


#changing base frequency, needs to go between 0 and 100 Hz
A = ( wn**2 * Xb ) / ( wn**2 - wc**2 )
