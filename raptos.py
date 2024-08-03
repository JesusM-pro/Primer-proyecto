# from random import randint as rnd

# members= 'Members.txt'
# exMemb= 'inactive.txt'
# fee =('yes','no')
# print(fee)

# def genFiles(members,exMemb):
#     with open(members,'w+') as writefile: 
#         writefile.write('Membership No  Date Joined  Active  \n')
#         data = "{:^13}  {:<11}  {:<6}\n"

#         for rowno in range(20):
#             date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
#             writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))


#     with open(exMemb,'w+') as writefile: 
#         writefile.write('Membership No  Date Joined  Active  \n')
#         data = "{:^13}  {:<11}  {:<6}\n"
#         for rowno in range(3):
#             date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
#             writefile.write(data.format(rnd(10000,99999),date,fee[1]))
    
# print(genFiles(members,exMemb))

members = 'Members.txt'
exMemb= 'inactive.txt'

def cleanFiles(members, exMemb):
    # open the membersMem as in r+ mode
    with open(members,'r+') as writeFile:
        with open(exMemb,'a+') as appenFile:
            lines= writeFile.readlines()

        #get the data
        writeFile.seek(0)
        members =writeFile.readlines()
        #remove header
        header = members[0]
        members.pop(0)

        inactive = [member for member in members if ('no' in member)]

        # ' '' for member in members:
        #     if 'no' in member:
        #         inactive.append(member)'''
        writeFile.seek(0)
        writeFile.write(header)
        for member in members:
            if (members in inactive):
                appenFile.write(member)
            else:
                writeFile.write(member)
        writeFile.truncate()

    
members= 'Members.txt'
exMemb= 'inactive.txt'
cleanFiles(members,exMemb)

headers= "Membership no date joined active \n"
with open(members,'r') as readFile:
    print('Active Members: \n\n')
    print(readFile.read())

with open(exMemb,'r') as readfile:
    print('Inactive Members: \n\n')
    print(readfile.read())