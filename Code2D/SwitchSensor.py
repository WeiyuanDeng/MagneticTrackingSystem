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
    print 'Example usage: python 2-D.py "/dev/ttyACM0"'
    exit(1)

 #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = sys.argv[1];

 # Get initial magnetic strength
  initial_sum1 = []

  # open serial port
  ser = serial.Serial(strPort, 9600)
  sleep(1)

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 1")
  print "Your choice: sensor", sensor

  ser.write(sensor)

  # ser.flush()

  while True:
    if len(initial_sum1) < 100:
    # try:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      initial_sum1.append(data_int)
      # initial_sum.append(data)
      # print data_sum
        # B10 = sum(initial_sum[20:])/len(initial_sum[20:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    # except KeyboardInterrupt:
    else:
      p = len(initial_sum1) - 1
      q = len(initial_sum1) - 11
      B10 = sum(initial_sum1[q:p])/10
      print 'Initial magnetic strength:', B10
      break

  initial_sum2 = []

  print '1 stands for sensor 1.'
  print '2 stands for sensor 2.'
  sensor = raw_input("Please choose sensor 2")
  print "Your choice: sensor", sensor

  ser.write(sensor)
  # ser.flush()

  while True:
    # try:
    if len(initial_sum2) < 100:
      line = ser.readline()
      data = [float(val) for val in line.split()]
      data_int = data[0]
      print data_int
      initial_sum2.append(data_int)
      # initial_sum.append(data)
      # print data_sum
      # if len(initial_sum)>22:
      #   B20 = sum(initial_sum[20:])/len(initial_sum[20:])
      # print data
      # if(len(data) == 2):
      #   analogData.add(data)
      #   analogPlot.update(analogData)
    # except KeyboardInterrupt:
    else:
      p = len(initial_sum2) - 1
      q = len(initial_sum2) - 11
      B20 = sum(initial_sum2[q:p])/10
      print 'Initial magnetic strength:', B20
      break

    # close serial
  ser.flush()
  ser.close()

# call main
if __name__ == '__main__':
  main()
