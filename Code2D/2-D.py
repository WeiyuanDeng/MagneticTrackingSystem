#!/usr/bin/env python
import sys
import serial
import numpy as np
import time
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
from numpy import pi, r_
from scipy import optimize
from pylab import *
from scipy import *

def Sensor():
  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor")
  print "Your choice: sensor", sensor
  print "Please wait..."
  return sensor

def getAverage(S):
  p = len(S) - 1
  q = len(S) - 11
  return sum(S[q:p])/10

# main() function
def main():
  # expects 1 arg - serial port string
  if(len(sys.argv) != 2):
    print 'Example usage: python 2-D.py "/dev/ttyACM0"'
    exit(1)

 #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = sys.argv[1];

  # open serial port
  ser = serial.Serial(strPort, 9600)
  sleep(1)

  print 'Please put the magnet away'
# Read value from sensor 1
  ser.write(Sensor())

 # Get initial magnetic strength
  initial_sum1 = []

  while True:
    if len(initial_sum1) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      initial_sum1.append(data_int)
    else:
      B10 = getAverage(initial_sum1)
      print 'Initial magnetic strength:', B10
      break

# Read value from sensor 2
  ser.write(Sensor())

  initial_sum2 = []

  while True:
    if len(initial_sum2) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      initial_sum2.append(data_int)
    else:
      B20 = getAverage(initial_sum2)
      print 'Initial magnetic strength:', B20
      break

  # Magnet at 30 mm from the sensor
  raw_input("Put the magnet at 30mm from the sensor and press ENTER")

  print "Read from sensor 1"
  ser.write(Sensor())

  measure1_sum = []

  while True:
    if len(measure1_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure1_sum.append(data_int)
    else:
      B1_measure1 = getAverage(measure1_sum)
      print 'Real time magnetic strength at 30mm from sensor1:', B1_measure1
      break

  print "Read from sensor 2"
  ser.write(Sensor())

  measure1_sum = []

  while True:
    if len(measure1_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure1_sum.append(data_int)
    else:
      B2_measure1 = getAverage(measure1_sum)
      print 'Real time magnetic strength at 30mm from sensor2:', B2_measure1
      break

  # Magnet at 50 mm from the sensor
  raw_input("Put the magnet at 50mm from the sensor and press ENTER")

  print "Read from sensor 1"
  ser.write(Sensor())

  measure2_sum = []

  while True:
    if len(measure2_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure2_sum.append(data_int)
    else:
      B1_measure2 = getAverage(measure2_sum)
      print 'Real time magnetic strength at 50mm from sensor1:', B1_measure2
      break

  print "Read from sensor 2"
  ser.write(Sensor())

  measure2_sum = []

  while True:
    if len(measure2_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure2_sum.append(data_int)
    else:
      B2_measure2 = getAverage(measure2_sum)
      print 'Real time magnetic strength at 50mm from sensor2:', B2_measure2
      break

  # Magnet at 80 mm from the sensor
  raw_input("Put the magnet at 80mm from the sensor and press ENTER")

  print "Read from sensor 1"
  ser.write(Sensor())

  measure3_sum = []

  while True:
    # try:
    if len(measure3_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure3_sum.append(data_int)
    else:
      B1_measure3 = getAverage(measure3_sum)
      print 'Real time magnetic strength at 80mm from sensor1:', B1_measure3
      break

  print "Read from sensor 2"
  ser.write(Sensor())

  measure3_sum = []

  while True:
    if len(measure3_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure3_sum.append(data_int)
    else:
      B2_measure3 = getAverage(measure3_sum)
      print 'Real time magnetic strength at 80mm from sensor2:', B2_measure3
      break

  # Magnet at 120 mm from the sensor
  raw_input("Put the magnet at 120mm from the sensor and press ENTER")

  print "Read from sensor 1"
  ser.write(Sensor())

  measure4_sum = []

  while True:
    if len(measure4_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure4_sum.append(data_int)
    else:
      B1_measure4 = getAverage(measure4_sum)
      print 'Real time magnetic strength at 120mm from sensor1:', B1_measure4
      break

  print "Read from sensor 2"
  ser.write(Sensor())

  measure4_sum = []

  while True:
    if len(measure4_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure4_sum.append(data_int)
    else:
      B2_measure4 = getAverage(measure4_sum)
      print 'Real time magnetic strength at 120mm from sensor2:', B2_measure4
      break

  # Magnet at 200 mm from the sensor
  raw_input("Put the magnet at 200mm from the sensor and press ENTER")

  print "Read from sensor 1"
  ser.write(Sensor())

  measure5_sum = []

  while True:
    # try:
    if len(measure5_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure5_sum.append(data_int)
    else:
      B1_measure5 = getAverage(measure5_sum)
      print 'Real time magnetic strength at 200mm from sensor1:', B1_measure5
      break

  print "Read from sensor 2"
  ser.write(Sensor())

  measure5_sum = []

  while True:
    if len(measure5_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      measure5_sum.append(data_int)
    else:
      B2_measure5 = getAverage(measure5_sum)
      print 'Real time magnetic strength at 200mm from sensor2:', B2_measure5
      break

  x2data = [-25, -40, -50, -50, -25, -100, 75, -50, 75, 15, 30]
  ydata = [0, 15, 25, 50,75,75,100,125,250,20,0]

  x_diff = 75
  n = 11
  x0data = [x_diff]*n
  x1data=np.add(x2data,x0data)
  BZ1data = [B1_measure1, B1_measure2, B1_measure3, B1_measure4, B1_measure5]
  BZ2data = [B2_measure1, B2_measure2, B2_measure3, B2_measure4, B2_measure5]


  raw_input('Press ENTER to get the relation between distance from sensor and magnetic strength with least square method')
  # define our (line) fitting function
  # fitfunc = lambda p, x, y: (p[0]) * (((x-p[1])**2) + ((y-p[2])**2))**(-3/2)
  fitfunc = lambda p, x, y: p[2] / ((x-p[1])**2 + (y-p[0])**2)**(1/2)**(3) + p[3]
  errfunc = lambda p, x, y, B: B - fitfunc(p, x, y)

  # pinit1 = [1000000, 0.001, 0.001, -1]
  pinit1 = [0.01, 0.01, 100000, 1]
  out1 = optimize.leastsq(errfunc, pinit1, args=(x1data, ydata, BZ1data), full_output=1)
  print 'out1', out1

  pfinal1 = out1[0]
  # print 'pfinal1', pfinal1


  pfinal1 = out1[0]

  b1 =pfinal1[2]
  x10 = pfinal2[1]
  y10 = pfinal2[0]
  C1 = pfinal1[3]

  print 'b1', b1
  print 'x10', x10
  print 'y10', y10
  print 'C1', C1


  fitfunc = lambda p, x, y: p[0] / (((x-p[1])**2 + (y-p[2])**2)**(1/2))**(3) +p[3]
  errfunc = lambda p, x, y, B: (B - fitfunc(p, x, y))

  # pinit1 = [1000000, 0.001, 0.001, -1]
  pinit1 = [10000000, 0.1, 0.1,1]
  out1 = optimize.leastsq(errfunc, pinit1,
                         args=(x2data, ydata, BZ2data), full_output=1)
  # # print 'out1', out1

  pfinal1 = out1[0]
  # # print 'pfinal1', pfinal1

  b2 =pfinal1[0]
  x20 = pfinal2[1]
  y20 = pfinal2[2]
  C2 = pfinal1[3]

  print 'b1', b1
  print 'x10', x10
  print 'y10', y10
  print 'C1', C1


  raw_input("Put the magnet wherever you like within the range 300mm and press ENTER")
  Bx_sum = []

  ser.write(Sensor())

  while True:
    if len(Bx_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx_sum.append(data_int)
    else:
      BZ1n = getAverage(Bx_sum)
      print 'Real time magnetic strength from Sensor 1:', BZ1n

  ser.write(Sensor())

  while True:
    if len(Bx_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx_sum.append(data_int)
    else:
      BZ2n = getAverage(Bx_sum)
      print 'Real time magnetic strength from Sensor 2:', BZ2n

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

  x0=75

  x2 = (np.square(d1)-np.square(d2)-np.square(x0))/(2*x0)
  y = np.sqrt((d2**2 - x2**2))
  x1 = x2-75

  print 'The coordinate of the magnet is (%g, %g)'%(x2, y)

    # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
