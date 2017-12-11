#!/usr/bin/env python
from scipy import optimize
import numpy as np
from pylab import *
from scipy import *
from scipy import optimize

# x2data=[30, 50, 80, 120, 200]
# ydata=[30, 50, 80, 120, 200]
x2data = [-25, -40, -50, -50, -25, -100, 75, -50, 75, 15, 30]
ydata = [0, 15, 25, 50,75,75,100,125,250,20,0]


x_diff = 75
n = 11
x0data = [x_diff]*n
B10 = [-78.07]*n
B20 = [-54.76]*n
# print x0data

x1data=np.add(x2data,x0data)

# d1data=np.sqrt((np.square(x1data) + np.square(ydata)))
# print 'd1',d1data
# d2data=np.sqrt((np.square(x2data) + np.square(ydata)))
# print 'd2',d2data

# B10 = [-89.91, -89.91, -89.91, -89.91, -89.91]
# B20 = [-61.42, -61.42, -61.42, -61.42, -61.42]

# BZ1 = [-78.07, -84.73, -87.32, -88.80, -89.54]
# BZ2 = [153.55, -9.62, -48.84, -58.09, -61.05]

BZ1 = [61.79, 227.55,328.56, 21.83, -54.02, -42.55, -74.74, -69.56,-77.70, -55.87, -62.90]
BZ2 = [1072.55, 172.79, 48.1, -4.07, -18.5, -46.42, -46.25, -47.73, -53.65, 1114.07, 661.93]

BZ1data = BZ1
print 'BZ1data', BZ1data
BZ2data = BZ2

# logx1 = log10(d1data)
# logy1 = log10(BZ1data)

# define our (line) fitting function
# fitfunc = lambda p, x, y: (p[0]) * (((x-p[1])**2) + ((y-p[2])**2))**(-3/2)
fitfunc = lambda p, x, y: p[2] / ((x-p[1])**2 + (y-p[0])**2)**(1/2)**(3) + p[3]
errfunc = lambda p, x, y, B: B - fitfunc(p, x, y)

# pinit1 = [1000000, 0.001, 0.001, -1]
pinit1 = [0.000001, 0.001, 100000, 1]
out1 = optimize.leastsq(errfunc, pinit1, args=(x1data, ydata, BZ1data), full_output=1)
print 'out1', out1

pfinal1 = out1[0]
# print 'pfinal1', pfinal1

# # covar = out[1]
# # print 'covar', covar
raw_input('Press ENTER to get the relation between distance from sensor and magnetic strength with least square method')


b1 = 18336066.3418
x10 = -2.78449875435
y10 = -4.1282395466
C1 = -79.4384354297


print 'b1', b1
print 'x10', x10
print 'y10', y10
print 'C1', C1



fitfunc = lambda p, x, y: p[0] / (((x-p[1])**2 + (y-p[2])**2)**(1/2))**(3)
errfunc = lambda p, x, y, B: (B - fitfunc(p, x, y))

# pinit1 = [1000000, 0.001, 0.001, -1]
pinit1 = [10000000, -0.1, -0.1]
out1 = optimize.leastsq(errfunc, pinit1,
                       args=(x2data, ydata, BZ2data), full_output=1)
# # print 'out1', out1

pfinal1 = out1[0]
# # print 'pfinal1', pfinal1

# # # covar = out[1]
# # # print 'covar', covar


b2 = 24767501.5711
x20 = -1.53861147238
y20 = -0.50534024789
C2 = -57.8547336877


print 'b2', b2
print 'x20', x20
print 'y20', y20
print'C2', C2



BZ1n = [1753.05]
# BZ1datan = BZ1n
# print 'BZ1datan', BZ1datan
# logy3 = log10(BZ1datan)
# print 'logy3', logy3

      # define our (line) fitting function
fitfunc = lambda p, x: b1 / ((p[0])**x) + C1
errfunc = lambda p, x, y: (y - fitfunc(p, x))

p0 = [1.0]
out = optimize.leastsq(errfunc, p0,
                       args=(3, BZ1n), full_output=1)

xyfinal1 = out[0]
      # covar = out[1]

      # power = pfinal[1]
d1 = xyfinal1[0]

print 'd1',d1


BZ2n = [53.28]
BZ2datan = BZ2n
# logy4 = log10(BZ2datan)

      # define our (line) fitting function
fitfunc = lambda p, x: b2 / ((p[0])**x) + C2
errfunc = lambda p, x, y: (y - fitfunc(p, x))

p0 = [0.1]
out = optimize.leastsq(errfunc, p0,
                       args=(3, BZ2n), full_output=1)

dfinal2 = out[0]
      # covar = out[1]

      # power = pfinal[1]
d2 = dfinal2[0]

print 'd2',d2


# # x0=x0data[0]
# d1sq = d1**2
# d2sq = d2**2
# fitfunc = lambda p, x: x + 2*x_diff*(p[0]-x20) + (x_diff)**2
# errfunc = lambda p, x, y: (y - fitfunc(p, x))

# # x2 = (np.square(d1)-np.square(d2)-np.square(x_diff))/(2*x_diff)
# # x1 = x2-78

# p0 = [0.1]
# out = optimize.leastsq(errfunc, p0,
#                        args=(d2sq,d1sq), full_output=1)

# final2 = out[0]
#       # covar = out[1]

#       # power = pfinal[1]
# x2 = final2[0]

# y = np.sqrt((d2**2 - x2**2))+y20

# print 'The coordinate of the magnet is (%g, %g)'%(x2, y)

x0=75

x2 = (np.square(d1)-np.square(d2)-np.square(x0))/(2*x0)
y = np.sqrt((d2**2 - x2**2))
x1 = x2-75

print 'The coordinate of the magnet is (%g, %g)'%(x2, y)

