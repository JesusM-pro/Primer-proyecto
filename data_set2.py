import pandas as pd
import numpy as np

file_path="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(file_path,names = headers)
#replace '?' to 'NaN'
df.replace('?', np.nan, inplace= True)
missing_data = df.isnull()

# for column in missing_data.columns.tolist():
#     print(column)
#     print(missing_data[column].value_counts())
#     print('')

avg_norm_loss = df['normalized-losses'].astype('float').mean(axis = 0)
#print('Average of normalized-losses:' , avg_norm_loss)
df['normalized-losses'].replace(np.nan, avg_norm_loss,inplace= True)

#calculate the mean value for the 'bore' column

avg_bore = df['bore'].astype ('float').mean(axis=0)
print('Average of bore:', avg_bore)

#replace 'NaN' with the mean value in the 'bore' column

df['bore'].replace(np.nan, avg_bore, inplace= True)
avg_stroke = df['stroke'].astype('float').mean(axis=0)
#print('this is fuck fatima',f'\n##################\n{avg_stroke}')

df['stroke'].replace(np.nan,avg_stroke, inplace=True)
#print(df['stroke'][30:60])

#calculate the mean value for the 'horsepower' colum

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
#print('Average horsepower: ', avg_horsepower)

#replace'NaN' with the mean value in the 'horsepower' column

df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

#calculate the mean value for 'peak - rpm' column

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
#print('Average peak rpm: ', avg_peakrpm)

#replace 'nan' with the man valuer in the 'peak-rpm' column

df['peak-rpm'].replace(np.nan,avg_peakrpm, inplace =True)

df['num-of-doors'].value_counts()
#print(df['num-of-doors'].value_counts().idxmax())

#replace the missing 'num-of-doors' values by the most frequent
df['num-of-doors'].replace(np.nan,'four',inplace=True)


#reset index, because we droped two rows
df.dropna(subset=['price'],axis=0, inplace=True)

df.reset_index(drop=True, inplace=True)

df[['bore', 'stroke']] = df[['bore', 'stroke']].astype('float')
df[['noramlized-losses']] = df[['normalized-losses']].astype('int')
df[['price']]= df[['price']].astype('float')
df[['peak-rpm']]= df[['peak-rpm']].astype('float')

df['city-L/100km'] = 235/df['city-mpg']
#print(df.head(5))


df['$$$highway-L/100km2'] = 235/df['highway-mpg']

#print('after  transfromation \n', df.head(5))

#replace (original value) by somenthing else

df['length'] = df ['length']/ df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()
#print(df[['length','width', 'height']].head())

df['horsepower'] = df['horsepower'].astype(int, copy=True)

import matplotlib as plt
from matplotlib import pyplot


plt.pyplot.hist(df['horsepower'])
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')
