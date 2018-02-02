list_python = ['zain', 'huzaifa', 'aejaz', 'mohsin', 'zaheer', 'abrar'] #list of student names in python

list_webapp = ['zain', 'huzaifa', 'gani', 'humaize', 'aejaz', 'shahbaz'] # list of student names in web application

familiar = []               #creating string for common and uncommon students
unfamiliar = []

for student in list_python:     # iterating through the students in python list

    if student in list_webapp:      #if condition true appending result to familiar string
        familiar.append(student)

    else:
        unfamiliar.append(student)  # appending result to unfamiliar string

for student1 in list_webapp:
    if student1 not in list_python:
        unfamiliar.append(student1)

print('Students Taking Python and Web Application: ')
print('\n'.join(familiar))
print('\nStudents Not Common in Python And Web Application:')
print('\n'.join(unfamiliar))