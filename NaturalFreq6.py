from math import pi
import math

E = math.pow(9,10) * 73.1
L = 4.25
A = pi * 2.3 * 0.00144
m = 1791.93

k = math.sqrt((E*A)/L)
print(k)
Fn = math.sqrt(k/m) * (1/(2*pi))
print(Fn)

