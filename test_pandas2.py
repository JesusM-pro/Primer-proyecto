people = int(input('how many people? '))
s_category= int(input('how many catogories you want to type today ?   '))
categories = []
def get_category():
    for category in range(s_category):
        category= input('What are the categories? ')
        categories.append(category)

    return categories
categories = get_category()

# print(len(categories))
for i in range(len(categories)):
    file = open('names.txt','a')
    if i < (len(categories)-1):
        file.write(f"{categories[i]},")
        file.close()
    else:
        file.write(f"{categories[i]}\n")
        file.close()
# print(categories)
for j in range(people):
    for i in range(len(categories)):
        question= input(f'what is your {categories[i]}? ')
        file = open('names.txt','a')
        if i < (len(categories)-1):    
            file.write(f"{question},")
            file.close()
        else:
            file.write(f"{question}\n")
            file.close()
# for i in range(3):
#     if i < 2:
#         print('this less than 5')
#     elif i >=2:
#         print("hi")
#     else:
#         break