import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore", category=UserWarning) 

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod2.csv"
df = pd.read_csv(path, header=0)
print('these are the first 5 rows', '\n', df.head())

lm= LinearRegression()
X= df[['CPU_frequency']]
Y= df[['Price']]
lm.fit(X, Y)
Yhat = lm.predict(X)

aX1 = sns.distplot(df['Price'], hist=False, color="r", label="Actual Value")

# Create a distribution plot for predicted values
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=aX1)

plt.title('Actual vs Fitted Values for Price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
plt.legend(['Actual Value', 'Predicted Value'])
# plt.show()




aX1= sns.distplot(df['Price'], hist=False, color= 'y', label='Actual Value')

#create a distribution plot for predicted values

sns.distplot(Yhat, hist= False, color = 'w', label = 'Fitted Values', ax = aX1)
# plt.title('Actual vs Fitted Values for price')
# plt.Xlabel('Price')
# plt.ylabel('Proportion of laptops')
# plt.legend( ['Actual value', 'Predicted Value'])
# # plt.show()

mse_slr = mean_squared_error(df['Price'], Yhat)
r2_score_slr = lm.score(X,Y)
# print('The R-square for linear Regression is:', r2_score_slr)
# print('The mean square error of price and predicted value is: ', mse_slr)

#Task 2 multiple linear regression
lm1 = LinearRegression()
z = df[['CPU_frequency', 'RAM_GB', 'Storage_GB_SSD', 'CPU_core', 'OS','GPU','Category']]
lm1.fit(z,Y)
Y_hat = lm1.predict(z)


# aX1 = sns.distplot(df['Price'], hist= False, color='r', label='Actual Value')
# sns.distplot(Y_hat, hist=False, color='b', label='Fitted Values', aX=aX1)

# plt.title('Actual vs fitted Values for price')
# plt.Xlabel('Price')
# plt.ylabel('Proportion of laptops')
# # plt.show()


aX2 = sns.distplot(df['Price'], hist = False, color= 'y', label='Actual Value')
sns.distplot(Y_hat, hist=False, color='w',label='Fitted Values', ax=aX2)
plt.title('Actual vs Fitted values for price')
plt.xlabel('Price')
plt.ylabel('Proportion of laptops')
# plt.show()


X = X.to_numpy().flatten()
p = np.polyfit(X, Y, 1)
p1 = np.poly1d(p)

f3 = np.polyfit(X, Y, 3)
# p3 = np.poly1d(f3)

f5 = np.polyfit(X, Y, 5)
# p5 = np.poly1d(f5)

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(independent_variable.min(),independent_variable.max(),100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title(f'Polynomial Fit for Price ~ {Name}')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of laptops')

#calling the function
print(PlotPolly(p1, X, Y, 'CPU_frequency'))