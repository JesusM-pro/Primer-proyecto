import numpy as np
import pandas  as pd

# a = np.array([0,1,2,3,4])
# for i in range(len(a)):
#     print(f'a[{a[i]}] : ', i)

# print(np.__version__)
# c = np.array([20, 1, 2, 3, 4])
# arr= np.array([1,2,3,4,5,6,7])
# print(arr[1:5:2])
# select = [0,1,2,3]
# d=c[select]
# c[select]= 1000

u = np.array([1,0])
v = np.array([0,1])

print(u-v)

Arr1=np.array ([1, 2, 3, 4, 5])
Arr2 = np.array ([1, 0, 1, 0, 1])
arr3 = Arr1 * Arr2

import time
import sys
import numpy as np
# import matplotlib as plt
import matplotlib.pyplot as plt

# def Plotvec2(a,b):
#     ax= plt.axes() # to generate the full window axes
#     ax.arrow(0,0,*a,head_with = 0.05, color = 'r',head_length = 0.1) # Add an arrow to A axes with 0.05, color red and arrow head lenght 0.1
#     plt.text(*(a+0.1),'a')
#     ax.arrow(0,0,*b, head_width= 0.05, color ='b', head_length = 0.1)#Add an arrow to the B Axes with arrow head width 0.05, color blue and arrow length 0.1
#     plt.text(*(b+ 0.1),"b")
#     plt.ylim(-2,2) #set the ylim to the botton(-2),top(2)
#     plt.xlim(-2,2)#set the xlim to left(-2), right (2)

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Arr1 =np.array([-1,1])
# Arr2 =np.array([1,1])
# Plotvec2(Arr1,Arr2)
# print(plt.show())
# print('The dot product is', np.dot(Arr1,Arr2))

ArrA = np.array([10,11,12,13,14,15])
ArrB = ArrA + 10

print(ArrA + ArrB)

a = np.array([10,20,30])
b=np.array([5,10,15])
c = np.subtract(a,b)
print(c)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3= np.subtract(arr1,arr2)
# print(arr3)

# x = np.linspace(5,4, num=6)
# print(x)

# arr1 = np.array([1,2,3])
# print(arr1)

# for x in arr1:
#     print(x)
    
u = np.array([1,0])
v= np.array([0,1])

w= u-v
print(w)

z = np.array([2,4])
print(z*-2)

list1= np.array([1,2,3,4,5])
list2 =np.array([1,0,1,0,1]) 

a = list1 *list2
print(a)

import time
import sys
import numpy as np
import matplotlib.pyplot as plt

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0,0,*a, head_width = 0.05 , color ='r', head_length = 0.1)#Add and arrow to the A Axes with arrow head with 0.05, color red
    plt.text(*(a+0.1),'a')
    ax.arrow(0,0,*b,head_width =0.05, color='b',head_length =0.1) #Add an arrow to the B axes with arrow head with 0.05, color blue
    plt.text(*(b+0.1),'b')
    plt.ylim(-2,2) # set to ylim to bottomm(-2), top(2)
    plt.xlim(-2,2)#set to xlimt to left(-2), right (2)

arr1= np.array([-1,1])
arr2= np.array([1,1])
Plotvec2(arr1,arr2)
print('The dot produt is', np.dot(arr1,arr2))
print(plt.show())