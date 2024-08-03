import pandas as pd
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)
# print(df.head())

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
# print(df.head())

# x= df[['Length']]
# print(type(x))

# # y= df.loc[[4:5],['Length','Artist','Genre','Album']]
# # print(y)

# y= df.loc[2:5,'Artist':'Rating']
# print(y)

print(df)
new_index=['a','b','c','d','e','f','g','h']

df_new=df
df_new.index=new_index
df_new.loc['a','Artist']
df_new.loc['a':'d','Artist']
print(df_new.loc['a':'d','Artist'])