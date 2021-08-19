import pandas as pd

data=pd.read_csv('C:/Users/subar/Desktop/data/gapminder_all.csv', index_col='country') #creates datafrae

oceania=pd.read_csv( 'C:/Users/subar/Desktop/data/gapminder_gdp_oceania.csv', index_col='country')
 

americas=pd.read_csv('C:/Users/subar/Desktop/data/gapminder_gdp_oceania.csv', index_col='country')



data.to_csv('C:/Users/subar/Desktop/data/write.csv') #creates output file

europe=pd.read_csv('C:/Users/subar/Desktop/data/gapminder_gdp_europe.csv', index_col='country')


data.iloc[0,0] #retrieves data from location

data.loc['Austria', 'gdpPercap_1952'] #retrieves data from location

print(data.loc['Austria', :])

GDPmax=data.loc['Austria':'Hungary'].max()
print(GDPmax)  #shows max value for each column...but doesn't show which row data came from

mask10000=oceania>10000 #gives true and false value at each datapoint
oceania[mask10000] #if true keeps original value, if false becomes not available

GDP10000 = data[mask10000].describe() #shows statistics for values which are true only

#splitting data by higher and lower than mean

mask_higher=europe>europe.mean() #shows true if value is higher than mean

wealth_score=mask_higher.aggregate('sum', axis=1)/len(europe.columns)   #not quite sure what this does, but it outputs a number between0-1 for each country depending on wealth

europe.groupby(wealth_score). sum()  #groups countries that have same wealth scores and sums their total gdp for each year

#How to print Serbia's 2007gdpcap
print(europe.loc['Servia','gdpPercap_2007'])

#how to print array of data
print(europe.iloc[0:2,0:2])
#or
print(europe.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])

#finds rows with min value
print(europe.idxmin())
#and max
print(europe.idxmax())

