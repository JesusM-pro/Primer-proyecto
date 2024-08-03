# size = int(input('how many lines you want to type today ?   '))
# s_category= int(input('how many catogories you want to type today ?   '))
def get_category():
    for i in range(3):
        categories= input('What are the categories? ')
        file = open("names.txt","a")
        if i< 3:
            file.write(f"{categories},")
            file.close()
        else:
            file.write(f"{categories}\n")
            file.close()
    return [categories]


def main():
    categories=  get_category()
    for i in range(3):
        name = input(f'What is your {categories[i]}?' )
        file = open('names.txt', 'a')
        file.write(f'{name},\n')
        file.close
main()
# for i in range(3):
#     if i < 2:
#         print('this less than 5')
#     elif i >=2:
#         print("hi")
#     else:
#         break