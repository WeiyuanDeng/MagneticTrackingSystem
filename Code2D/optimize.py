#!/usr/bin/env python
from scipy import optimize
import numpy as np
from pylab import *
from scipy import *
from scipy import optimize

x2data=[30, 50, 80, 120, 200]
ydata=[30, 50, 80, 120, 200]

x0data=[78,78,78,78,78]

x1data=np.add(x2data,x0data)

d1data=np.sqrt((np.square(x1data) + np.square(ydata)))
print 'd1',d1data
d2data=np.sqrt((np.square(x2data) + np.square(ydata)))
print 'd2',d2data

B10 = [-89.91, -89.91, -89.91, -89.91, -89.91]
B20 = [-61.42, -61.42, -61.42, -61.42, -61.42]

BZ1 = [-78.07, -84.73, -87.32, -88.80, -89.54]
BZ2 = [153.55, -9.62, -48.84, -58.09, -61.05]

BZ1data = np.subtract(BZ1, B10)
# print 'BZ1data', BZ1data
BZ2data = np.subtract(BZ2, B20)

logx1 = log10(d1data)
logy1 = log10(BZ1data)

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + (-3) * (x+p[1])
errfunc = lambda p, x, y: (y - fitfunc(p, x))

pinit1 = [1.0, -1.0]
out1 = optimize.leastsq(errfunc, pinit1,
                       args=(logx1, logy1), full_output=1)
# print 'out1', out1

pfinal1 = out1[0]
# print 'pfinal1', pfinal1

# covar = out[1]
# print 'covar', covar


b1 =pfinal1[0]
A1 = 10.0**pfinal1[0]
dinit1 = pfinal1[1]

print 'A1',A1
print 'dinit1', dinit1


logx2 = log10(d2data)
logy2 = log10(BZ2data)

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + (-3) * (x+p[1])
errfunc = lambda p, x, y: (y - fitfunc(p, x))

pinit2 = [1.0, -1.0]
out2 = optimize.leastsq(errfunc, pinit2,
                       args=(logx2, logy2), full_output=1)
# print 'out2', out2

pfinal2 = out2[0]
# print 'pfinal2', pfinal2

# covar = out[1]
# print 'covar', covar

# power2 = pfinal2[1]
b2 =pfinal2[0]
A2 = 10.0**pfinal2[0]
dinit2 = pfinal2[1]

print 'A2:',A2
print 'dinit2', dinit2



BZ1n = [-80]
BZ1datan = np.subtract(BZ1n, B10[0])
print 'BZ1datan', BZ1datan
logy3 = log10(BZ1datan)
print 'logy3', logy3

      # define our (line) fitting function
fitfunc = lambda p, x: b1 + x * (p[0]+dinit1)
errfunc = lambda p, x, y: (y - fitfunc(p, x))

p0 = [-1.0]
out = optimize.leastsq(errfunc, p0,
                       args=(-3,logy3), full_output=1)

dfinal1 = out[0]
      # covar = out[1]

      # power = pfinal[1]
d1 = 10**dfinal1[0]

print 'd1',d1


BZ2n = [0]
BZ2datan = np.subtract(BZ2n, B20[0])
logy4 = log10(BZ2datan)

      # define our (line) fitting function
fitfunc = lambda p, x: b2 + x * (p[0]+dinit2)
errfunc = lambda p, x, y: (y - fitfunc(p, x))

p0 = [-1.0]
out = optimize.leastsq(errfunc, p0,
                       args=(-3,logy4), full_output=1)

dfinal2 = out[0]
      # covar = out[1]

      # power = pfinal[1]
d2 = 10**dfinal2[0]

print 'd2',d2


x0=x0data[0]

x2 = (np.square(d1)-np.square(d2)-np.square(x0))/(2*x0)
print x2
y = np.sqrt((d2**2 - x2**2))
x1 = x2-78

print 'The coordinate of the magnet is (%g, %g)'%(x2, y)
