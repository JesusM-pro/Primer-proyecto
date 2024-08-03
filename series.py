import pandas as pd
import numpy as np
Dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
dict_2 = pd.Series(Dict1)
dic_3 = np.array(dict_2).tolist()
print(dic_3)

# print(dict_2)

# arr1 =[10,20, 30, 40 ,50]
# arr2 = pd.Series(arr1)

# print(arr2)
# numpyArray = arr2.to_numpy()
# print('this is numpy array\n',numpyArray)

# print('this is the type of a numpy\n',type(numpyArray))

