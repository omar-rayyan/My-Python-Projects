# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]] 
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15  # Change the value 10 in x to 15

students[0]['last_name'] = 'Bryant' # Change the last_name of the first student from Jordan to Bryant

sports_directory['soccer'][0] = 'Andres'  # In the sports_directory, change 'Messi' to 'Andres'

z[0]['y'] = 30  # Change the value 20 in z to 30




# Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(dict):
    for dictionary in dict:
        for key, value in dictionary.items():
            print(f"{key} - {value}")

iterateDictionary(students)




# Get Values From a List of Dictionaries
def iterateDictionary2(key_name, lst):
    for dictionary in lst:
        print(dictionary[key_name])




# Iterate Through a Dictionary with List Values
def printInfo(dict):
    for key, value in dict.items():
        print(f"{len(value)} {key.upper()}")
        for location in value:
            print(location)
                
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)