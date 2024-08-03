# i = 1
# for i in range(11):
#     print(i)
#     i += 1

# row = 3
# for i in range(1,row +1, 1):
#     for j in range (1, i+1):
#         print(j,end='')
#     print('')

# numbers=6
# j = 5
# for i in range(j,numbers +j):
#     print(i, end=" ")
# print('')


# N_numbers=5
# start= 0
# for i in range(start,N_numbers+start,2):
#     for j in range(start,i +1):
#         print(j, end=' ')
#     print()

# s= 0
# number =10
# for i in range (number + 1):
#     s += i
# print(s)


# number = 2
# final_number =10
# for i in range(final_number):
#     print(f'this is the multiplication for {number} times {i}: ',number * i)
#     i += 1


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i %5 ==0 and i <= 150 and i <= 500:
#         print(i)


# number = 5
# row = 5
# for i in range(row):
#     for j in range(number-i,number-number,-1):
#         i =+ 1
#         print(j,end='')
#     print('')

# list1 =[10, 20, 30, 40, 50]
# print(len(list1))
# for i in range(4,-1,-1):
#     print(list1[i])


#Display numbers from -10 to -1 using loop

# for i in range(-10,0,1):
# #     print(i)
# i =0
# while i <= 5:
#     print(i)
#     i+=1
# print('done')

 
# num_1 = 0
# num_2 =1
# while num_1 <= 10:
#     print(num_1,end='')
#     rest = num_1 + num_2
#     num_1 = num_2
#     num_2= rest

# factorial = 5
# for i in range(1, factorial):
#     factorial = factorial *i
# print(factorial)


# number = 9192
# number_list = []
# for i in str(number):
#     number_list.append(i)
#     number_list.reverse()
# print(*number_list)


# num = 9192
# reverse_number = 0


# print('given number ,', num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print('reverse number, ', reverse_number)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in my_list[1::2]:
#     print(i,'',end='')
# print('')

# input_number = 6
# size = 6
# for i in range(size):
#     print(f'the current number is:{i} and the cube is {i*i*i}')
# print('')


# n = 5
# start = 2
# sum_seq = 0

# for i in range(n):
#     if  i == n-1:
#         print(start)
#         sum_seq += start
#         start =start* 10 + 2 
#     else:
#         print(start, end='+')
#         sum_seq += start
#         start =start* 10 + 2 
# print('\n sum of above series is :,',sum_seq)

# height= 4
# width= 10
# number = 2
# for i in range(height):
#     print(width*str(number))
#     number += 1


new_hires = [('Mark Adams', 'SQL Analyst', 4000),
             ('Leslie Burton', 'HR Specialist', 2300),
             ('Dorothy Castillo', 'UX Designer', 3100)]

# def remov_sql(people_list):
#     for person in people_list:
#         if "SQL" in person:
#             people_list.remove(person)
#             print(people_list)
#         else:
#             break

exam_results = {
'Dominic Vargas': 67,
'Marion Riley': 89,
'Candice White': 45,
'Doreen Goodwin': 82,
'Janet Hunter': 98,
'Jaime Page': 32,
'Neil Fernandez': 76,
'Jana Frank': 28,
'Adrienne Perkins': 98,
'Rosa Mccarthy': 34
}



def get_results(list_students):
    max = 0
    min = 100
    for values in list_students.values():
        if values > max:
            max =values
        elif values < min:
            min = values
        else:
            break
    return max - min


def main():
    hi = get_results(exam_results)
    print(hi)

if __name__ == "__main__":
    main()


 

