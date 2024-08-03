# def delete_line(fileName, line_number):
#     with open(fileName) as file:
#         lines = file.readlines()
#     if line_number <= len(lines):
#         del lines[line_number-1]
#         with open(fileName,'w') as file:
#             for line in lines:
#                 file.write(line)
#         with open(fileName,'r') as file:
#             return print(file.readlines())
#     else:
#         print('haha')

# fileName= 'example.txt'
# delete_line_number = int(input('Line: '))
# delete_line(fileName,delete_line_number)

file = 'example.txt' 
with open (file,"a+") as testWriteFile:
    print('initial location: {}'.format(testWriteFile.tell()))
    data = testWriteFile.read()
    if(not data):# empty strings
        print('Nothing')
    else:
        print(testWriteFile.read())

    
    testWriteFile.seek(0,0)
    print('\nNew Location: {}'.format(testWriteFile.tell()))
    data= testWriteFile.read()
    if(not data):
        print('Read nothing')
    else:
        print(data)

    print('Location after read: {}'.format(testWriteFile.tell()))