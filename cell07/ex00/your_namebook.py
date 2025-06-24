#!/usr/bin/env python3

# • Create a script called your_namebook.py.
# • It should contain a method called array_of_names.
# • This method takes a dictionary associating first names with last names as a param-
# eter.
# • It will build an array with the full names of the people, with the first letter capi-
# talized. It returns this array. Refer to the example.
# • For example, the following script:
# # your method definition here
# persons = {
# "jean": "valjean",
# "grace": "hopper",
# "xavier": "niel",
# "fifi": "brindacier"
# }
# print(array_of_names(persons))
# Will produce the following output:
# ?> ./your_namebook.py
# ['Jean Valjean', 'Grace Hopper', 'Xavier Niel', 'Fifi Brindacier']
# ?>

def array_of_names(names):
    return [first.capitalize() + " " + last.capitalize() for first, last in names.items()]


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))

    
