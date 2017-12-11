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

  # while True:
  #   str1 = ser.read(1)
  #   if str1 == '':
  #       print 'no data on line'
  #   else:
  #       data_sum.append(int(str1))

  # ave = sum(data_sum)/len(data_sum)
  # print ave
  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 1")
  print "Your choice: sensor", sensor

  ser.write(sensor)

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      initial_sum.append(data_int)
      # initial_sum.append(data)
      # print data_sum
      if len(initial_sum)>22:
        B0 = sum(initial_sum[20:])/len(initial_sum[20:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Initial magnetic strength:', B10
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      initial_sum.append(data_int)
      # initial_sum.append(data)
      # print data_sum
      if len(initial_sum)>22:
        B20 = sum(initial_sum[20:])/len(initial_sum[20:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Initial magnetic strength:', B20
      break

  # close serial
  # ser.flush()
  # ser.close()

  # raw_input("Press ENTER to get initial magnetic strength:")
  # print 'Initial magnetic strength:', B0

 # Minimization difference

  # B1 = measure(30)

  # B2 = measure(50)

  # # open serial port
  # ser = serial.Serial(strPort, 9600)

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)
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
        B1_measure1 = sum(measure1_sum[40:])/len(measure1_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 30mm from sensor:', B1_measure1
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)
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
        B2_measure1 = sum(measure1_sum[40:])/len(measure1_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 30mm from sensor:', B2_measure1
      break

  # print 'Real time magnetic strength at 30mm from sensor:', B_measure1

    # close serial
  # ser.flush()
  # ser.close()

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B1_measure2 = sum(measure2_sum[40:])/len(measure2_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 50mm from sensor:', B1_measure2
      break


  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B2_measure2 = sum(measure2_sum[40:])/len(measure2_sum[40:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 50mm from sensor:', B2_measure2
      break

  # raw_input("Press ENTER to get real time magnetic strength:")
  # print 'Real time magnetic strength at 50mm from sensor:', B_measure2

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B1_measure3 = sum(measure3_sum[40:])/len(measure3_sum[40:])
      # B_measure3 = sum(measure3_sum)/len(measure3_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 80mm from sensor:', B1_measure3
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B2_measure3 = sum(measure3_sum[40:])/len(measure3_sum[40:])
      # B_measure3 = sum(measure3_sum)/len(measure3_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 80mm from sensor:', B2_measure3
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B1_measure4 = sum(measure4_sum[40:])/len(measure4_sum[40:])
      # B_measure4 = sum(measure4_sum)/len(measure4_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 120mm from sensor:', B1_measure4
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

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
        B2_measure4 = sum(measure4_sum[40:])/len(measure4_sum[40:])
      # B_measure4 = sum(measure4_sum)/len(measure4_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 120mm from sensor:', B2_measure4
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)
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
        B1_measure5 = sum(measure5_sum[40:])/len(measure5_sum[40:])
      # B_measure5 = sum(measure5_sum)/len(measure5_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 200mm from sensor:', B1_measure5
      break

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)
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
        B2_measure5 = sum(measure5_sum[40:])/len(measure5_sum[40:])
      # B_measure5 = sum(measure5_sum)/len(measure5_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength at 200mm from sensor:', B2_measure5
      break

  xdata = [30, 50, 80, 120, 200]
  x0data=[5,5,5,5,5,5]
  x2data=np.add(xdata,x0data)
  ydata = [30, 50, 80, 120, 200]
  d1data=np.sqrt((np.square(xdata) + np.square(ydata)))
  print 'd1',d1data
  d2data=np.sqrt((np.square(x2data) + np.square(ydata)))
  print 'd2',d2data
  BZ1data = [B1_measure1-B10, B1_measure2-B10, B1_measure3-B10, B1_measure4-B10, B1_measure5-B10]
  BZ2data = [B2_measure1-B20, B2_measure2-B20, B2_measure3-B20, B2_measure4-B20, B2_measure5-B20]
  # x0 = x - (B_measure - B0)^(1/3)

  raw_input('Press ENTER to get the relation between distance from sensor and magnetic strength with least square method')

  # xdata = np.array(x)
  # ydata=np.array(B_measure)

  logx1 = log10(d1data)
  logx2 = log10(d2data)
  logy1 = log10(BZ1data)
  logy2 = log10(BZ2data)

  # define our (line) fitting function
  fitfunc = lambda p, x: p[0] + p[1] * x
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  pinit1 = [1.0, -1.0]
  out1 = optimize.leastsq(errfunc, pinit1,
                         args=(logx1, logy1), full_output=1)
  print 'out1', out1

  pfinal1 = out1[0]
  print 'pfinal1', pfinal1

  # covar = out[1]
  # print 'covar', covar

  power1 = pfinal1[1]
  b1 =pfinal1[0]
  A1 = 10.0**pfinal1[0]

  print 'amp1:',A1, 'power1', power1



  logx2 = log10(d2data)
  logy2 = log10(BZ2data)

  # define our (line) fitting function
  fitfunc = lambda p, x: p[0] + p[1] * x
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  pinit2 = [1.0, -1.0]
  out2 = optimize.leastsq(errfunc, pinit2,
                         args=(logx2, logy2), full_output=1)
  print 'out2', out2

  pfinal2 = out2[0]
  print 'pfinal2', pfinal2

  # covar = out[1]
  # print 'covar', covar

  power2 = pfinal2[1]
  b2 =pfinal2[0]
  A2 = 10.0**pfinal2[0]

  print 'amp2:',A2, 'power2', power2



  raw_input("Put the magnet wherever you like within the range 300mm and press ENTER")
  Bx_sum = []

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx_sum.append(data_int)
      # print data_sum
      if len(Bx_sum)>50:
        BZ1 = sum(Bx_sum[40:])/len(Bx_sum[40:])
      # Bx = sum(Bx_sum)/len(Bx_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', BZ1

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)

  print 'Please wait for 10 sec and use keyboard interrupt'

  while True:
    try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      # print data_int
      Bx_sum.append(data_int)
      # print data_sum
      if len(Bx_sum)>50:
        BZ2 = sum(Bx_sum[40:])/len(Bx_sum[40:])
      # Bx = sum(Bx_sum)/len(Bx_sum)
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    except KeyboardInterrupt:
      print ' '
      print 'Real time magnetic strength is:', BZ2


  logy3 = log10(BZ1)

        # define our (line) fitting function
  fitfunc = lambda p, x: b + x * p[0]
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  p0 = [-1.0]
  out = optimize.leastsq(errfunc, p0,
                         args=(power1,logy3), full_output=1)

  dfinal1 = out[0]
        # covar = out[1]

        # power = pfinal[1]
  d1 = 10**dfinal1[0]

  print d1


  logy2 = log10(BZ2)

        # define our (line) fitting function
  fitfunc = lambda p, x: b + x * p[0]
  errfunc = lambda p, x, y: (y - fitfunc(p, x))

  p0 = [-1.0]
  out = optimize.leastsq(errfunc, p0,
                         args=(power2,logy2), full_output=1)

  dfinal2 = out[0]
        # covar = out[1]

        # power = pfinal[1]
  d2 = 10**dfinal2[0]

  print d2

  x1 = (d2**2 - d1**2-(x0data[0])**2)/x0data[0]/2
  y1 = (d1**2 - x1**2)**(1/2)

  print '(%g,%g)', x, y


  # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
