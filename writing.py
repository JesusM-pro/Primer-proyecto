import pandas as pd

# with open('names.txt','r') as file:
#     lines=file.readlines()
#     print(lines[0])

file= open('names.txt','r')
lines= file.readlines()
del lines[0]
file= open('names.txt','w')
for line in lines:
    file.write(line)
file.close()

# del lines[1]
# file= open('names.txt','w')
# for line in lines:
#     file.write(line)
#     file.close()

# file = open('names.txt','r')
# lines= file.readlines()
# print(lines[1])
# path="/Users/jesusmejia/Desktop/mejia python/names.txt"
# df=pd.read_csv(path,header=1)
# print(df.head())
# print(df["name"])