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

# main() function
def main():
  # expects 1 arg - serial port string
  if(len(sys.argv) != 2):
    print 'Example usage: python 1-D.py "/dev/ttyACM0"'
    exit(1)

 #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = sys.argv[1];

 # Get initial magnetic strength
  initial_sum = []

  # open serial port
  ser = serial.Serial(strPort, 9600)



  # Magnet at 30 mm from the sensor
  raw_input("Put the magnet at 30mm from the sensor and press ENTER")
  measure1_sum = []

  #   # open serial port
  # ser = serial.Serial(strPort, 9600)

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      measure1_sum.append(data_int)
      # print data_sum
      if len(measure1_sum)>50:
        B_measure1 = sum(measure1_sum[40:])/len(measure1_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 30mm from sensor:', B_measure1
      break

  # print 'Real time magnetic strength at 30mm from sensor:', B_measure1

    # close serial
  # ser.flush()
  # ser.close()

  # Magnet at 50 mm from the sensor
  raw_input("Put the magnet at 50mm from the sensor and press ENTER")
  measure2_sum = []

  # open serial port
  ser = serial.Serial(strPort, 9600)

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      measure2_sum.append(data_int)
      # print data_sum
      if len(measure2_sum)>50:
        B_measure2 = sum(measure2_sum[40:])/len(measure2_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 50mm from sensor:', B_measure2
      break

  # raw_input("Press ENTER to get real time magnetic strength:")
  # print 'Real time magnetic strength at 50mm from sensor:', B_measure2

  # Magnet at 80 mm from the sensor
  raw_input("Put the magnet at 80mm from the sensor and press ENTER")
  measure3_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      measure3_sum.append(data_int)
      # print data_sum
      if len(measure3_sum)>50:
        B_measure3 = sum(measure3_sum[40:])/len(measure3_sum[40:])
      # B_measure3 = sum(measure3_sum)/len(measure3_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 80mm from sensor:', B_measure3
      break

  # Magnet at 80 mm from the sensor
  raw_input("Put the magnet at 120mm from the sensor and press ENTER")
  measure4_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      measure4_sum.append(data_int)
      # print data_sum
      if len(measure4_sum)>50:
        B_measure4 = sum(measure4_sum[40:])/len(measure4_sum[40:])
      # B_measure4 = sum(measure4_sum)/len(measure4_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 120mm from sensor:', B_measure4
      break

  # Magnet at 200 mm from the sensor
  raw_input("Put the magnet at 200mm from the sensor and press ENTER")
  measure5_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      measure5_sum.append(data_int)
      # print data_sum
      if len(measure5_sum)>50:
        B_measure5 = sum(measure5_sum[40:])/len(measure5_sum[40:])
      # B_measure5 = sum(measure5_sum)/len(measure5_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 200mm from sensor:', B_measure5
      break


  xdata = [30, 50, 80, 120, 200]
  # ydata = [B_measure1-B0, B_measure2-B0, B_measure3-B0, B_measure4-B0, B_measure5-B0]
  ydata = [B_measure1, B_measure2, B_measure3, B_measure4, B_measure5]
  # x0 = x - (B_measure - B0)^(1/3)

  raw_input('Press ENTER to get the relation between distance from sensor and magnetic strength with least square method')

  # xdata = np.array(x)
  # ydata=np.array(B_measure)

  # define our (line) fitting function
  fitfunc = lambda p, x: (p[0] * (x-p[1])**(-3))+p[2]
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  pinit = [1000000, 0.1, 1.0]
  out = optimize.leastsq(errfunc, pinit,
                         args=(xdata, ydata), full_output=1)
  # print 'out', out

  pfinal = out[0]
  # print 'pfinal', pfinal

  b = pfinal[0]
  xinit = pfinal[1]
  C = pfinal[2]

  print 'b', b
  print 'C', C
  print 'x0', xinit

  # print '%g * x ** (%g)'%(A, power)

  # print "Would you like to do a test?"
  # print "1: YES"
  # print "0: NO"
  # if :
  #   pass

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx1_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx1_sum.append(data_int)
      # print data_sum
      if len(Bx1_sum)>50:
        Bx1 = sum(Bx1_sum[40:])/len(Bx1_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx1
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx1), full_output=1)

      dfinal = out[0]

      d1 = dfinal[0]

      print 'd1 = ', d1
      print 'The magnet is at', d1, 'mm from the sensor'
      break

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx2_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx2_sum.append(data_int)
      # print data_sum
      if len(Bx2_sum)>50:
        Bx2 = sum(Bx2_sum[40:])/len(Bx2_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx2
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx2), full_output=1)

      dfinal = out[0]

      d2 = dfinal[0]

      print 'd2 = ', d2
      print 'The magnet is at', d2, 'mm from the sensor'
      break

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx3_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx3_sum.append(data_int)
      # print data_sum
      if len(Bx3_sum)>50:
        Bx3 = sum(Bx3_sum[40:])/len(Bx3_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx3
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx3), full_output=1)

      dfinal = out[0]

      d3 = dfinal[0]

      print 'd3 = ', d3
      print 'The magnet is at', d3, 'mm from the sensor'
      break

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx4_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx4_sum.append(data_int)
      # print data_sum
      if len(Bx4_sum)>50:
        Bx4 = sum(Bx4_sum[40:])/len(Bx4_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx4
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx4), full_output=1)

      dfinal = out[0]

      d4 = dfinal[0]

      print 'd4 = ', d4
      print 'The magnet is at', d4, 'mm from the sensor'
      break

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx5_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx5_sum.append(data_int)
      # print data_sum
      if len(Bx5_sum)>50:
        Bx5 = sum(Bx5_sum[40:])/len(Bx5_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx5
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx5), full_output=1)

      dfinal = out[0]

      d5 = dfinal[0]

      print 'd5 = ', d5
      print 'The magnet is at', d5, 'mm from the sensor'
      break

  raw_input("Put the magnet wherever you like within the range of the engineering paper and press ENTER")
  Bx6_sum = []

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx6_sum.append(data_int)
      # print data_sum
      if len(Bx6_sum)>50:
        Bx6 = sum(Bx6_sum[40:])/len(Bx6_sum[40:])
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', Bx6
      # logx = log10(x)
      fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
      errfunc = lambda p, x, y: (y - fitfunc(p, x))

      p0 = [1]
      out = optimize.leastsq(errfunc, p0,
                             args=(-3,Bx6), full_output=1)

      dfinal = out[0]

      d6 = dfinal[0]

      print 'd6 = ', d6
      print 'The magnet is at', d6, 'mm from the sensor'
      break

  print "d =", [d1, d2, d3, d4, d5, d6]

  # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
