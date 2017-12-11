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

def getAverage(S):
  p = len(S) - 1
  q = len(S) - 11
  return sum(S[q:p])/10

# main() function
def main():
  # expects 1 arg - serial port string
  if(len(sys.argv) != 2):
    print 'Example usage: python 1-D.py "/dev/ttyACM0"'
    exit(1)

 #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = sys.argv[1];

  # open serial port
  ser = serial.Serial(strPort, 9600)
  sleep(1)

  # Magnet at 200 mm from the sensor
  raw_input("Put the magnet at 200mm from the sensor and press ENTER")
  measure1_sum = []

  while True:
    if len(measure1_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      measure1_sum.append(data_int)
    else:
      B_measure1 = getAverage(measure1_sum)
      print 'Magnet at 200mm from the sensor, magnetic strength:', B_measure1
      break

  # Magnet at 120mm from the sensor
  raw_input("Put the magnet at 120mm from the sensor and press ENTER")
  measure2_sum = []

  while True:
    if len(measure2_sum) < 40:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      measure2_sum.append(data_int)
    else:
      B_measure2 = getAverage(measure2_sum)
      print 'Initial magnetic strength:', B_measure2
      break

  # # Magnet at 80mm from the sensor
  # raw_input("Put the magnet at 80mm from the sensor and press ENTER")
  # measure3_sum = []

  # while True:
  #   if len(measure3_sum) < 40:
  #     line = ser.readline()
  #     data = [float(val) for val in line.split()]
  #     data_int = data[0]
  #     print data_int
  #     measure3_sum.append(data_int)
  #   else:
  #     B_measure3 = getAverage(measure3_sum)
  #     print 'Initial magnetic strength:', B_measure3
  #     break

  # # Magnet at 50mm from the sensor
  # raw_input("Put the magnet at 50mm from the sensor and press ENTER")
  # measure4_sum = []

  # while True:
  #   if len(measure4_sum) < 40:
  #     line = ser.readline()
  #     data = [float(val) for val in line.split()]
  #     data_int = data[0]
  #     print data_int
  #     measure4_sum.append(data_int)
  #   else:
  #     B_measure4 = getAverage(measure4_sum)
  #     print 'Initial magnetic strength:', B_measure4
  #     break

  # # Magnet at 30mm from the sensor
  # raw_input("Put the magnet at 30mm from the sensor and press ENTER")
  # measure5_sum = []

  # while True:
  #   if len(measure5_sum) < 40:
  #     line = ser.readline()
  #     data = [float(val) for val in line.split()]
  #     data_int = data[0]
  #     print data_int
  #     measure5_sum.append(data_int)
  #   else:
  #     B_measure5 = getAverage(measure5_sum)
  #     print 'Initial magnetic strength:', B_measure5
  #     break


  # d_data = [200, 120, 80, 50, 30]
  # B_data = [B_measure1, B_measure2, B_measure3, B_measure4, B_measure5]

  # # define our (line) fitting function
  # fitfunc = lambda p, x: (p[0] * (x-p[1])**(-3))+p[2]
  # errfunc = lambda p, x, y: (y - fitfunc(p, x))

  # pinit = [1000000, 0.1, 1.0]
  # out = optimize.leastsq(errfunc, pinit,
  #                        args=(d_data, B_data), full_output=1)

  # pfinal = out[0]

  # b = pfinal[0]
  # dinit = pfinal[1]
  # C = pfinal[2]

  # print 'b', b
  # print 'C', C
  # print 'd0', dinit

  # print '%g * (x + %g) ** (-3) + %g'%(b, dinit, C)


  # raw_input("Put the magnet wherever you like within range of engineering paper and press ENTER")
  # B_dunknown_sum = []

  # while True:
  #   if len(B_dunknown_sum) < 40:
  #     line = ser.readline()
  #     data = [float(val) for val in line.split()]
  #     data_int = data[0]
  #     print data_int
  #     B_dunknown_sum.append(data_int)
  #   else:
  #     B_dunknown = getAverage(B_dunknown_sum)
  #     print 'Initial magnetic strength:', B_dunknown
  #     break

  #         # define our (line) fitting function
  # fitfunc = lambda p, x: b * (p[0]-xinit)**(x) + C
  # errfunc = lambda p, x, y: (y - fitfunc(p, x))

  # p0 = [1]
  # out = optimize.leastsq(errfunc, p0,
  #                          args=(-3,B_dunknown), full_output=1)

  # dfinal = out[0]

  # d = dfinal[0]

  # print 'The magnet is at %gmm from the sensor'%(d)
  # print 'Thank you!'

  # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
