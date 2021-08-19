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


#this merges list into one list
pressure1 = [0.27, 0.456, 0.33333, 0.7, 1.4]

pressure1.extend([0.43, 2.7, 0.665])




#delete
del pressure1[0]

empty=[1,"rrrrrr", 1.2345]

del empty[1]


#for loops
subjects = ['cats', 'dogs', 'goldfish', 'Jacob']

for i in subjects:  
    print('I really like', i)
    

for number in [2,3,4]:
    print('the value of number x=', number*2)

#all indented lines are included in loop
print('Subaru')




# primes = [2,3,5]
# for p in primes:
#         squared = p **2
#         cubed = p **3
#         print('original:',p,'squared:',squared,'cubed:', cubed)
        
        
primes = [2,3,5]
squared=[]
cubed=[]

for p in primes:
    sqr=p**2
    squared.append(sqr)
    cbd=p**3
    cubed.append(cbd)


for i in range(0,len(primes),1):
    print('the value of i in this loop is:', primes[i])
    
    
#if statements
mass=10.02
if mass>3.0 and mass <= 10.0: 
    print(mass, 'is large')
if mass >=3.0 and mass> 10.0:
    print(mass,'is ridiculously large')
else:
    print(mass, 'is not large')
    