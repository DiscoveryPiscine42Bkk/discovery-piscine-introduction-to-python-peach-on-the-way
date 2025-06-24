#!/usr/bin/env python3

# • Create a script called persons_of_interest.py.
# • It will contain a method called famous_births.
# • This method will take a dictionary representing historical figures as a parame-
# ter. Each entry in the dictionary is itself a dictionary with the keys: :name and
# :date_of_birth.
# • The method will sort the dictionary passed as a parameter in order of birth dates,
# and then display each entry (see the example below).
# • For example, the following script:
# # your method definition here
# women_scientists = {
# "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
# "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
# "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
# "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
# }
# famous_births(women_scientists)
# will have the following output:
# ?> ./persons_of_interest.py
# Ada Lovelace is a great scientist born in 1815.
# Lise Meitner is a great scientist born in 1878.
# Cecila Payne is a great scientist born in 1900.
# Grace Hopper is a great scientist born in 1906.
# ?>

def famous_births(women_births):
    date_of_births = { d["date_of_birth"]: d["name"] for d in women_births.values() }
    for date_of_birth in sorted(date_of_births.keys()):
        name = date_of_births[date_of_birth]
        print(f"{name} is a great scientist born in {date_of_birth}")


women_scientists = {
    "ada":     { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise":    { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace":   { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
