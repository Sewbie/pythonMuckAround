# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:17:29 2021

@author: subar
"""

import matplotlib.pyplot as plt
time=[0,1,2,3]
position=[0,100,200,300]
plt.plot(time,position)
plt.xlabel("Time hr")
plt.ylabel("Position km")

import pandas as pd
oceania=pd.read_csv('C:/Users/subar/Desktop/data/gapminder_gdp_oceania.csv', index_col='country')

years=oceania.columns.str.strip('gdpPercap_') #removes 'gdpPercap_'

oceania.columns=years. astype(int) #changes years to integer


oceania.loc['Australia'].plot() #prints the graph

plt.style.use('ggplot')
oceania.T.plot()
plt.ylabel('GDP per Capita')
plt.xlabel('year')
#prints both aus and nz

oceania.T.plot(kind='bar') #for setting up barcharts

gdp_australia=oceania.loc['Australia']
gdp_nz=oceania.loc['New Zealand']
plt.plot(years, gdp_australia, 'g--', label='Aust')#green dash line

plt.plot(years, gdp_nz, 'b-', label='NZ')#blue solid line

plt.legend(loc='upper left') #creates legend

plt.scatter (gdp_australia, gdp_nz)  #scatterplot

plt.savefig('my_graph.png') #to save a graph
