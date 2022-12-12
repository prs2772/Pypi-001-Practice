from io import StringIO

class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Add(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()
def modifyElement(list, target, newVal):
  if(target in list):
    list[target] = newVal
    return True
  else:
    return False


my_dictionary = {}
print(type(my_dictionary))

my_dictionary = {
  'Plane' : 'Air transport',
  'Name' : 'Kubuntu',
  'Special' : 'See all',
  'Size' : 'Enormous'
}

print(my_dictionary)
print(len(my_dictionary))

print(my_dictionary['Plane'])
# Get and if not exists, the program doesn't break
print(my_dictionary.get('Sub name'))

# Looks if exists
print('Fly' in my_dictionary)
print('Size' in my_dictionary)
print('\n\n')

person = {
  'Name' : 'Paris',
  'LastName' : 'R',
  'Languages' : ['JS', 'Dart', 'C#', 'Java', 'C', 'C++'],
  'Age' : 21
}

message = StringBuilder()
message.Add('Person: ' + str(person))
message.Add('\n')
message.Add('->Name: ' + str(person.get('Name')) + '\n')
message.Add('->LastName: ' + str(person.get('LastName')) + '\n')
message.Add('->Languages: ' + str(person.get('Languages')) + '\n')
message.Add('->Age: ' + str(person.get('Age')) + '\n')
print('Before modify the person: \n', message)

message = StringBuilder()

print('Items\n', person.items())
print('Keys\n', person.keys())
print('Values\n', person.values())

print(modifyElement(person,'LastName', 'Ramírez'))
print(modifyElement(person,'LastNames', 'S')) # LastNames does not exist
modifyElement(person,'Age', person['Age'] + 1 if('Age' in person) else 33)
person['Languages'].append('Python')
# delete without pop
del person['Name']

# Print person
message.Add('Person: ' + str(person))
message.Add('\n')
message.Add('->Name: ' + str(person.get('Name')) + '\n')
message.Add('->LastName: ' + str(person.get('LastName')) + '\n')
message.Add('->Languages: ' + str(person.get('Languages')) + '\n')
message.Add('->Age: ' + str(person.get('Age')) + '\n')
print('After modify the person: \n', message)



