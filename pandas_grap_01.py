# test Create Graph Data with pandas simulate data in variable

from pandas import *
import numpy
import matplotlib.pyplot as plt

print(pandas.__version__) # แสดง pandas version\

# sample data for dataframe
data = {
	'Name':['Boey','Aey','Tou','Aon','Chai'],
	'Age':['27','27','25','27','26'],
	'Gender':['Male','Female','Male','Male','Male'],
	'State':['Bangkok','Bangkok','Bangkok','Bangkok','Bangkok'],
	'num_child':[2,0,0,1,0],
	'num_pet':[1,0,10,0,0]

	}
# test print dataframe for show data

# ทดสอบแสดงกราฟแบบจุด
df = DataFrame(data)
df.plot(kind='scatter', x='num_child', y='num_pet', color='red')
plt.show()


# plot multiple line
ax = plt.gca()
df.plot(kind='line', x='Name', y='num_child', ax=ax)
df.plot(kind='line', x='Name', y='num_pet', color='red', ax=ax)


# ------------------------------------------
# Plot data with Line Chart 
# วิธีเขียนแบบที่ 1
data2 = pandas.DataFrame({
	'Year':[1992,1993,1994,1995,1996],
	'Unemployment_Rate':[9.8,12,8,7.2,6.9]

	})
data2.plot(kind='line', x='Year', y='Unemployment_Rate')
plt.show()


# วิธีเขียนแบบที่ 2
data3 = {
	'Year':[1992,1993,1994,1995,1996],
	'Unemployment_Rate':[9.8,12,10,7.2,6.9]

	}

df = DataFrame(data3)
df.plot(kind='line', x='Year', y='Unemployment_Rate')
plt.show()

# ------------------------------------------

# Plot data with Bar Chart
data_4 = {
	'Country':['USA','Thailand','Lao','Chaina'],
	'GDP':[40000,40,20000,50000]
}

df = DataFrame(data_4)
df.plot(kind='bar', x='Country', y='GDP')
plt.show()

































