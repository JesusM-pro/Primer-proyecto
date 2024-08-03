import pandas as pd

# x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
#       'Salary':[100000, 80000, 50000, 60000]}
# df= pd.DataFrame(x)
# print(df)
#casting the diction
Data2 = {'Student':['David','Samuel','Terry','Evan'],'Age':['27','24','22','32'],'Country':['UK','Canada','China','USA'],'Course': ['Python', 'Data structures','Machine learning','Web devolpment'],'Marks':['85','72','89', '76']}

df2= pd.DataFrame(Data2)

df3= df2.set_index('Student')
# ›
print(df3.loc['Evan','Age'])