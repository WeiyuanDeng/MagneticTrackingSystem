#!/usr/bin/env python
from scipy import optimize
import numpy as np

# xdata = [30, 50, 80, 120, 160, 200]

# ydata = [1214.09-14, 270.29-14, 79.22-14, 33.43-14, 22.69-14, 18.64-14]

# print ydata

# fitfunc = lambda p, x: p[0] * (x+p[1]) ** (-3)
# errfunc = lambda p, x, y: (y - fitfunc(p, x))

# out,success = optimize.leastsq(errfunc, [1,-1,-0.5],args=(xdata, ydata),maxfev=3000)

# print "%g * (x+%g)"%(out[0],out[1])


from pylab import *
from scipy import *
from scipy import optimize

xdata=[30, 50, 80, 120, 160, 200]
ydata=[1214.09-14, 270.29-14, 79.22-14, 33.43-14, 22.69-14, 18.64-14]

# xdata=[30, 50, 80, 120, 160, 200]
# ydata=[399, 85, 22, 8, 4.5, 3.2]
# logx = log10(xdata)
# logy = log10(ydata)

# b1 = 10**4
# C = 2
# x0 = [0.7, 0.7, 0.7,0.7, 0.7]

# ydata[i] = b1*(xdata[i]-x0[i])**(-3)+C


# define our (line) fitting function
fitfunc = lambda p, x: (p[0] * (x-p[1])**(-3))+p[2]
errfunc = lambda p, x, y: (y - fitfunc(p, x))

pinit = [1000000, 0.1, 1.0]
out = optimize.leastsq(errfunc, pinit,
                       args=(xdata, ydata), full_output=1)
# print 'out', out

pfinal = out[0]
# print 'pfinal', pfinal

# covar = out[1]
# print 'covar', covar

b = pfinal[0]
xinit = pfinal[1]
C = pfinal[2]

print 'b', b
print 'C', C
print 'x0', xinit

# b1 = 10**7
# C = 2
# xinit = 0.7


Bx = 20.43

      # define our (line) fitting function
fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
errfunc = lambda p, x, y: (y - fitfunc(p, x))

p0 = [1]
out = optimize.leastsq(errfunc, p0,
                       args=(-3,Bx), full_output=1)

dfinal = out[0]
      # covar = out[1]

      # power = pfinal[1]
d = dfinal[0]

print 'd = ', d


# powerlaw = lambda x, amp, index: amp * (x**index)
# ##########
# Plotting data
##########
# clf()
# subplot(2, 1, 1)
# plot(xdata, powerlaw(xdata, amp, index))     # Fit
# plot(xdata, ydata)#, yerr=yerr, fmt='k.')  # Data
# text(0.0020, 30, 'Ampli = %5.2f' % amp)
# text(0.0020, 25, 'Index = %5.2f' % index)
# xlabel('X')
# ylabel('Y')

# subplot(2, 1, 2)
# loglog(xdata, powerlaw(xdata, amp, index))
# plot(xdata, ydata)#, yerr=yerr, fmt='k.')  # Data
# xlabel('X (log scale)')
# ylabel('Y (log scale)')

# savefig('power_law_fit.png')
# show()


# def fitfunc(p, x):
#     return p[0] + p[1] * (x ** p[2])
# def errfunc(p, x, y):
#     return y - fitfunc(p, x)

# xdata=np.array([30, 50, 80, 120, 160, 200])
# ydata=np.array([1214.09-14, 270.29-14, 79.22-14, 33.43-14, 22.69-14, 18.64-14])

# N = 5000
# xprime = xdata * N

# qout,success = optimize.leastsq(errfunc, [max(ydata),-1,-0.5],
#                                args=(xprime, ydata),maxfev=3000)

# out = qout[:]
# out[0] = qout[0]
# out[1] = qout[1] * (N**qout[2])
# # out[2] = qout[2]
# print "%g + %g*x^%g"%(out[0],out[1],out[2])


