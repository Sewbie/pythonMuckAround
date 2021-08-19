# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:07:06 2021

@author: subar
"""

pressure = [0.27, 0.456, 0.33333, 0.7, 1.4]  #making a list

print ('pressure:',pressure)   #print

pressure[1]


pressure.append(0.543333333) # append adds another value to the list

#adding another list within the list
pressure.append([0.43, 2.7, 0.665])

print(pressure)

pressure1 = [0.27, 0.456, 0.33333, 0.7, 1.4]

pressure1.extend([0.43, 2.7, 0.665])
