import pandas  as pd
import numpy as np

data_source = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

#from pyodide.http import pyfetch

async def download (url, filename):
    response = await pyfetch (url)
    if response.status == 200:
        with open(filename,'wb') as f:
            f.write(await response.bytes())
    
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(path, header=None)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
print(df.head())
'''''
df1 = df.replace('?',np.NaN)
df = df1.dropna(subset = "price",axis = 0)
                
#df.to_csv('/Users/jesusmejia/Desktop/mejia python/fatima.csv', index=False)
#print(df.describe(include='all'))
'''