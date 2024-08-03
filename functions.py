def main():
    student = get_student()
    # if student['Name'] == 'Fatima':
    #     student['House'] = 'Jesus house'
    #     print(f"{student['Name']} from {student['House']}")
    # else:  
    #     print(f"{student['Name']} from {student['House']}")
    print(student)

def get_student():
    student = {}
    student['House']= input('House: ')
    student['Name']= input ('Name')
    return student

if __name__ == "__main__":
    main()