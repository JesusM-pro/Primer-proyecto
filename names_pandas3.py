import pandas as pd
path="/Users/jesusmejia/Desktop/mejia python/names.txt"
df=pd.read_csv(path,header=0)
c_area =3000000
c_population = 25000000
new_dt= df.loc[(df['area'] >= c_area) |code (df['population'] >= c_population)]
print(new_dt[['name','area','population']])
        
