import numpy as np  
import matplotlib.pyplot as plt  
from pylsl import StreamInlet, resolve_byprop  
import utils 
import pyautogui
import time

dW = band_powers[Band.Delta]
aW = band_powers[Band.Alpha]
bW = band_powers[Band.Beta]
tW = band_powers[Band.Theta]

allValues.append(dW)
 print("Delta: {}".format(dW))

                
a = False

if (dW >= 1 and allValues[-2] <= 1) or (dW >= 1.7 and allValues[-2] >= 1):
  print("Blink!")
  input_times.append(time.time()) 
  a = True # Update current_time here

  if len(input_times) > 1 and a:
    difference = input_times[-1] - input_times[-2]
    if difference <= 1.5:
      counter.append('-')
      a = False
    elif 1.5 < difference <= 2.5:
      counter.append('.')
      a = False
    elif 2.5 < difference <= 3:
      counter.append('s')
    else:
      break 
a = False
