import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "/Users/jesusmejia/Downloads/automobileEDA (2).csv"
df = pd.read_csv(file_path,header=0)

# print(df.head())
# print(df.columns)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
x = df[['highway-mpg']]
y =df[['price']]

# print(lm.fit(x,y))
# Yhat = lm.predict(x)
# print(Yhat[0:7])
# print('#########\n', lm.intercept_)
# print('######################\n', lm.coef_)

lm1 = LinearRegression()
print('#########\n', lm1)

x2 = df[['engine-size']]
y2 = df[['price']]

lm1.fit(x2,y2)
print(lm1)

# b= int(lm1.coef_)
# a= int(lm1.intercept_)
# print ('this is a', a)
# print('this is b',b)
# Yhat2 =lm1.predict(x2)
# print(Yhat2[0:5])

print('this is index 50', df['price'][99:100])


# engine_size =(int(df.iloc[99]['engine-size']))
# print('this is engine size',engine_size)
# price_car = a + (b*engine_size)
# print(f'this the car price for a vehicule of {engine_size} is ', price_car, '$')

# print(int(df.iloc[1]['engine-size']))
# # print(int(df['engine-size'][1:2]))

z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm.fit(z,df['price'])

index = 3

prueba =df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']][[1]]
print('this is INDEX', df['price'][index])
index_horse = df['horsepower'][index]
index_curb = df['curb-weight'][index]
index_engine = df['engine-size'][index]
index_highway = df['highway-mpg'][index]

interceptor = lm.intercept_
coeficientt= lm.coef_

print (f'{interceptor}+{index_horse*coeficientt[0]} + {index_curb*coeficientt[1]} + {index_engine*coeficientt[2]} + {index_highway*coeficientt[3]}')
precio_new_car= interceptor + index_horse*coeficientt[0] + index_curb*coeficientt[1] + index_engine*coeficientt[2] + index_highway*coeficientt[3]
print('this is new CAR price',precio_new_car)

print('this is the interceptor',lm.intercept_)
print('this is the coeficiente',*lm.coef_)

lm2 = LinearRegression()
lm2.fit(df[['normalized-losses', 'highway-mpg']], df[''])