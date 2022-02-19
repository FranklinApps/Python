x = [ [5,2,3], [10,8,9] ] 
students_A = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 20} ]

for value in sports_directory.values():
    print(value)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


for dic in students:
    for key in dic:
        print(dic[key])

def FName(keynamen, students):
    for x in range (len(students)):
        for key, val in students[x].items():
            if key == keynamen:
                print(f"{val}")

FName("first_name", students)

def FName(keynamen, students):
    for x in range (len(students)):
        for key, val in students[x].items():
            if key == keynamen:
                print(f"{val}")

FName("last_name", students)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(len(some_dict['locations']), "LOCATIONS")
    for location in some_dict['locations']:
        print(location)
    print()
    print(len(some_dict['instructors']), "INSTRUCTORS")
    for instructors in some_dict['instructors']:
        print(instructors)
        
printInfo(dojo)