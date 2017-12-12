from collections import namedtuple
Person = namedtuple('Person', 'firstname lastname')
shankar = Person('Shankar', 'Natarajan')
print(shankar.firstname)
