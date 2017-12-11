#!/usr/bin/env python
import sys
import serial
import numpy as np
import time
from time import sleep
from collections import deque
from matplotlib import pyplot as plt

import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize

x = [30, 50, 80, 120, 160, 200]
B0 = [14, 14, 14, 14, 14, 14]
B_measure = [1214.09, 270.29, 79.22, 33.43, 22.69, 18.64]
B_real = B_measure - B0

A=(x.^2).^2.5;
B= [(3*x.*z)./A,(3*y.*z)./A,-(x.^2+y.^2)./A+2*z.^2./A];
















B_measure = B0 + A * (x + x0) ^(-3)

B_predict = B0 + A * (x + x0) ^(-3)

meandiff_sum = sum((B_measure - B_predict)^2)
