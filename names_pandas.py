import pandas as pd
# print('hi')
path="/Users/jesusmejia/Desktop/mejia python/names.txt"

dt=pd.read_csv(path,header=0)
def country_big(country_name):
    country_index=dt.index[dt['name']== country_name]
    population=dt['population'][country_index]
    area = dt['area'][country_index]
    if population.item() >= c_population or area.item() >= c_area:
        return True
c_area =3000000
c_population = 25000000

for country in dt["name"]:
    is_big = country_big(country)
    country_index=dt.index[dt['name']== country].to_list()
    if is_big == True:
        New_df = dt.iloc[country_index][['name','area', 'population']]
        print(New_df,'\n')


